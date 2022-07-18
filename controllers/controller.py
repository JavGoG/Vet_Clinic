from flask import Flask, render_template, Blueprint, request, redirect
# from models.vet import vet_list
import repositories.user_repository as user_repository
from repositories.user_repository import User
tasks_blueprint = Blueprint("vets",__name__ )

# INDEX
@tasks_blueprint.route("/users")
def index():
    users = user_repository.select_all()
    return render_template("users/index.html", users = users)

@tasks_blueprint.route("/users", methods=['POST'])
def users():
    user_id = request.form['id']
    name = request.form['name']
    pet_name = request.form['pet_name']
    phone = request.form['phone']
    user = user_repository.select(user_id)
    instance_user = User(pet_name, user, name, phone)
    user_repository.save(instance_user)
    return redirect("/users")

@tasks_blueprint.route("/bookings")
def book():
    clinic = Clinic(animal, user)
    return render_template("users/index.html", users = users)

# @tasks_blueprint.route("/bookings", methods=['POST'])
# def booking():
#     user_id = request.form['id']
#     name = request.form['name']
#     pet_name = request.form['pet_name']
#     phone = request.form['phone']
#     user = user_repository.select(user_id)
#     instance_user = User(pet_name, user, name, phone)
#     user_repository.save(instance_user)