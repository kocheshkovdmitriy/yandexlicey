import flask
from flask import jsonify, render_template, make_response, request

from . import db_session
from .category import Category
from .news import News

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/news', methods=['GET'])
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    return jsonify(
        {
            'news':
                [item.to_dict(only=('title', 'user.name'))
                 for item in news]
        }
    )

@blueprint.route('/api/news/<int:id>', methods=['GET'])
def get_detail_new(id):
    db_sess = db_session.create_session()
    new = db_sess.query(News).filter(News.id==id).first()
    if not new:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'new': new.to_dict(only=('categories.name', 'title', 'content', 'user.name', 'created_date'))
        }
    )

@blueprint.route('/api/news', methods=['POST'])
def create_news():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['title', 'content', 'user_id']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    new = News(
        title=request.json['title'],
        content=request.json['content'],
        user_id=request.json['user_id'],
    )
    cat = db_sess.query(Category).filter(Category.id==request.json.get('cat_id', 1)).first()
    print(cat)
    new.categories.append(cat)
    db_sess.add(new)
    db_sess.commit()
    return jsonify(new.to_dict(only=('id', 'categories.name', 'title', 'content', 'user.name', 'created_date')))