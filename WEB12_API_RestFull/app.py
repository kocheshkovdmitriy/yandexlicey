from flask import Flask
from flask_restful import Api
from WEB12_API_RestFull.data import db_session, news_resources

app = Flask(__name__)
api = Api(app)


@app.route('/')
def main_page():
    return '<h1>Main Page</h1>'


db_session.global_init("db/blogs.db")
api.add_resource(news_resources.NewsListResource, '/api/v2/news')
api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')


app.run()

