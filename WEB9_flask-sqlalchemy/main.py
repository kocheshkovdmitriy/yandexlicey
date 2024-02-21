from flask import Flask, render_template
from data import db_session
from data.users import User
from data.news import News

import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/user/<int:id>')
def user(id):
    user = db_sess.query(User).filter(User.id==id).first()
    return render_template('user.html', user=user)




if __name__ == '__main__':
    db_session.global_init('db/blog.db')
    db_sess = db_session.create_session()

    '''
    users = db_sess.query(User).all()


    for i in range(10):
        user = random.choice(users)
        
        db_sess.add(
            News(
                title=f'New {i + 1}',
                content=f'descriptoin new {i + 1}',
                user=user
            )
        )
    db_sess.commit()
    '''


    app.run(host='127.0.0.1', port=8000)