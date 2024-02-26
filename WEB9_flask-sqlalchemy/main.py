import datetime

from flask import Flask, render_template, request, make_response, session
from data import db_session
from data.users import User
from data.news import News
from data.category import Category
from util.random_data import get_random_name, get_random_email, get_random_password
from flask_login import LoginManager, login_required

import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta( days=14)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/user/<int:id>')
def user(id):
    user = db_sess.query(User).filter(User.id==id).first()
    return render_template('user.html', user=user)

@app.route("/cookie_test")
@login_required
def cookie_test():
    '''visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 14)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 недели")
        res.set_cookie("visits_count", '1',
                       max_age=60 * 60 * 24 * 14)
    return res'''

    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")


if __name__ == '__main__':
    db_session.global_init('db/blog.db')
    db_sess = db_session.create_session()

    '''
    categorys = [Category(name=n) for n in ['first', 'second', 'txvxfb']]
    for cat in categorys:
        db_sess.add(cat)


    users = [User(
        name=get_random_name(),
        lastname=get_random_name(8),
        email=get_random_email(),
        hashed_password=get_random_password()
    ) for i in range(5)]

    for user in users:
        db_sess.add(user)

    for i in range(10):
        user = random.choice(users)
        cat = random.choice(categorys)
        new = News(
                title=f'New {i + 1}',
                content=f'descriptoin new {i + 1}',
                user=user
            )
        new.categories.append(cat)
        db_sess.add(new)
    db_sess.commit()
    '''

    '''
    cat = db_sess.query(Category).filter(Category.id == 3).first()
    print(cat)
    news = list(filter(lambda x: cat in x.categories, db_sess.query(News).all()))
    print(news)
    '''
    app.run(host='127.0.0.1', port=8000)