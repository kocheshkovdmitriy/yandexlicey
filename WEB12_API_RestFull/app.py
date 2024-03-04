from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from WEB12_API_RestFull.data import db_session, news_resources
from WEB12_API_RestFull.data.news import News
from WEB12_API_RestFull.data.news_resources import abort_if_news_not_found

app = Flask(__name__)
api = Api(app)


@app.route('/')
def main_page():
    return '<h1>Main Page</h1>'


db_session.global_init("db/blogs.db")
api.add_resource(news_resources.NewsListResource, '/api/v2/news')
api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')


app.run()

