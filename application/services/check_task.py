import datetime
from sqlalchemy.sql import func
from application import db
from application.models import Task, Habit, Statistic


def task_check(user_id):
    tasks = db.session.query(Task, Habit).filter_by(
        user_id=user_id).join(Habit).all()
    date_now = datetime.date.today()
    weekday_now = datetime.datetime.today().strftime('%A')
    ids = []
    for task, habit in tasks:
        static_game = Statistic.query.filter_by(task_id=task.id).with_entities(
            func.sum(Statistic.life).label('total')).first().total
        if static_game != None:
            Task.query.get(task.id).total_lifes = task.life - static_game
            db.session.commit()
        static = Statistic.query.filter_by(
            task_id=task.id).filter_by(created=date_now).first()
        if static == None or static.life == 1:
            if task.start_period <= date_now:
                for day in task.weekdays:
                    if day == weekday_now:
                        ids.append(task.id)
                        if static_game != None and task.life - static_game == 0:
                            Statistic.query.get(task.id).status = 'game over'
                            db.session.commit()
                        if static == None or static.task_id != task.id and static.created != date_now:
                            statistic_data = Statistic(
                                weekdays=weekday_now,
                                task_id=task.id,
                                user_id=user_id,
                                status='in process'
                            )
                            try:
                                db.session.add(statistic_data)
                                db.session.commit()
                            except:
                                db.session.rollback()
    return ids