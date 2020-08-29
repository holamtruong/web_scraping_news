# NEWS APP
This application is design to collect and scrap news data from different sources in a unified way using the python packages 'newspaper3k'. Flask module is use to publish information via HTTP method. SQLite is choice as embedded database software for local storage in this application.
## Setup environment

### Install flask
    >>> pip install flask

### Install newspaper3k
    >>> pip install newspaper3k

### Clear DB (execute SQL)
    delete from news;    
    from sqlite_sequence where name='news';

## How to use:
- Run 'utils.py' to get and insert article.

- Run 'index.py' to start server.

- (Or) Run 'run.bat' to start server.



