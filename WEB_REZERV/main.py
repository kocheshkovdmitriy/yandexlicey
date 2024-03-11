import datetime
from  flask import Flask

from data.jobs import Jobs
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta( days=14)


def create_users():
    db_sess = db_session.create_session()

    user1 = User()
    user1.surname = "Scott"
    user1.name = 'Ridley'
    user1.age = 21
    user1.position = 'captain'
    user1.speciality = 'research engineer'
    user1.address = 'module_1'
    user1.email = 'scott_chief@mars.org'
    db_sess.add(user1)

    user2 = User(
        surname="Yin",
        name='Riddik',
        age=23,
        position='colonist',
        speciality='scientist',
        address='module_2',
        email='yinriddik@mars.org',
    )
    db_sess.add(user2)

    user3 = User(
        surname="Yin",
        name='Robert',
        age=20,
        position='colonist',
        speciality='scientist',
        address='module_2',
        email='yinrobert@mars.org',
    )
    db_sess.add(user3)

    db_sess.commit()


def create_jobs():
    db_sess = db_session.create_session()

    job1 = Jobs(
        team_leader=1,
        job='deployment of residential modules 1 and 2',
        work_size=15,
        collaborators='2, 3',
        start_date=datetime.datetime.now(),
        is_finished=False
        )
    db_sess.add(job1)
    db_sess.commit()




def main():
    name = input('Введите имя базы данных: ')
    db_session.global_init(name)
    db_sess = db_session.create_session()
    users = db_sess.query(User).filter(User.address=='module_1').all()
    for user in users:
        print(user)



if __name__ == '__main__':
    main()