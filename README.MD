# NEWS APP
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

- Run 'run.bat' to start server.


## Notes:
### Help:
    > flask run --help

### run on Linux: 
    > export FLASK_APP=index.py

### run on Windows: 
    > set FLASK_APP=index.py
    > $venv:FLASK_APP = "main"
    > flask run

### change port (debugger to view error):
    > flask run -p 1000 --reload --debugger


