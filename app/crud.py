from .models import User, Meal
from .database import db


def get_user(user_id):
    return User.query.get(user_id)


def get_users():
    return User.query.all()


def create_user(name, email):
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_meals():
    return Meal.query.all()


def create_meal(name, calories, user_id):
    new_meal = Meal(name=name, calories=calories, user_id=user_id)
    db.session.add(new_meal)
    db.session.commit()
    return new_meal
