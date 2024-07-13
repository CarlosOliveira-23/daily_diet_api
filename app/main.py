from flask import Blueprint, request, jsonify
from .crud import get_user, get_users, create_user, get_meals, create_meal
from .schemas import UserSchema, MealSchema

main_bp = Blueprint('main', __name__)
user_schema = UserSchema()
meal_schema = MealSchema()


@main_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = create_user(data['name'], data['email'])
    return user_schema.jsonify(user)


@main_bp.route('/users', methods=["GET"])
def liist_users():
    users = get_users()
    return user_schema.jsonify(users, many=True)


@main_bp.route('/users/<int:user_id>/meals', methods=['POST'])
def add_meal(user_id):
    data = request.get_json()
    meal = create_meal(data['name'], data['calories'], user_id)
    return meal_schema.jsonify(meal)

@main_bp.route('/meals', methods=["GET"])
def list_meals():
    meals = get_meals()
    return meal_schema.jsonify(meals, many=True)
