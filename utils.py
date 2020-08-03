import sqlite3
from newspaper import Article
import newspaper


def get_all(query):
    conn = sqlite3.connect("data/newsdb.db")
    data = conn.execute(query).fetchall()
    conn.close()

    return data


def get_news_by_id(news_id):
    conn = sqlite3.connect("data/newsdb.db")
    sql = '''
    SELECT N.subject, N.description, N.image, N.original_url, C.name, C.url
    FROM news N INNER JOIN category C ON N.category_id=C.id
    WHERE N.id=?
    '''

    news = conn.execute(sql, (news_id,)).fetchone()
    conn.close()

    return news


def add_comment(news_id, content):
    conn = sqlite3.connect("data/newsdb.db")
    sql = '''
    INSERT INTO comment(content, news_id)
    VALUES (?, ?)
    '''
    conn.execute(sql, (content, news_id))
    conn.commit()
    conn.close()


def add_news(conn, url, category_id):
    sql = '''
    INSERT INTO news(subject, description, image, original_url, category_id)
    VALUES (?, ?, ?, ?, ?)
    '''

    article = Article(url)
    article.download()
    article.parse()

    conn.execute(sql, (article.title, article.text, article.top_image, article.url, category_id))
    conn.commit()


def get_news_url():
    cats = get_all("SELECT * from category")
    conn = sqlite3.connect("data/newsdb.db")

    for cat in cats:
        cat_id = cat[0]
        url = cat[2]
        cat_paper = newspaper.build(url, memoize_articles=True)

        print("\n \n=================== Size of " + str(url) + ": " + str(cat_paper.size()) + " =====================")

        for article in cat_paper.articles:
            try:
                print("===", article.url)
                add_news(conn, article.url, cat_id)
            except Exception as ex:
                print("ERROR: " + str(ex))
                pass

    conn.close()


if __name__ == "__main__":
    # print(get_all("SELECT * FROM category"))
    get_news_url()
