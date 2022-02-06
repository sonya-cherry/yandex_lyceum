from flask import Flask
from data import db_session
from data.__all_models import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/jobs.db")

    db_sess = db_session.create_session()

    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    work.col

    db_sess.commit()

    # app.run()


if __name__ == '__main__':
    main()
