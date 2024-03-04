from flask import Flask
from data import db_session, news_api


app = Flask(__name__)

@app.route('/')
def main_page():
    return '<h1>Main Page</h1>'



def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(news_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()