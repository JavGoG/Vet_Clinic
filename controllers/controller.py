from crypt import methods
from flask import Flask, render_template, Blueprint, request, redirect
from models.booking import Booking
import repositories.vet_repository as vet_repository
import repositories.user_repository as user_repository
from repositories.user_repository import User
import repositories.booking_repository as booking_repository
import repositories.animal_repository as animal_repository
from models.animal import  Animal


tasks_blueprint = Blueprint("vets",__name__ )

# INDEX
@tasks_blueprint.route("/")
def origin():
    return render_template("base.html")


@tasks_blueprint.route("/users")
def index():
    users = user_repository.select_all()
    return render_template("users/index.html", users = users)

@tasks_blueprint.route("/users/new")
def new_user():
    return render_template("/users/new.html")

@tasks_blueprint.route("/users", methods=['POST'])
def users():
    name = request.form['name']
    pet_name = request.form['pet_name']
    phone = request.form['phone']

    instance_user = User(name, pet_name, phone)
    user_repository.save(instance_user)
    return redirect("/users")

@tasks_blueprint.route("/bookings")
def bookings_index():
    # A list of all bookings
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings= bookings)

@tasks_blueprint.route("/bookings/new")
def new_booking():
    return render_template("bookings/new.html")

@tasks_blueprint.route("/bookings", methods=['POST'])
def booking():
    user_name = request.form['user_name']
    pet_name = request.form['pet_name']
    date_time = request.form['date_time']
    booking = Booking(user_name, pet_name, date_time)
    booking_repository.save(booking)
    return redirect("/bookings")

@tasks_blueprint.route("/vets")
def vet():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets=vets)

@tasks_blueprint.route("/services")
def service():
    return render_template("services/index.html")

@tasks_blueprint.route("/services/show")
def show():
    return render_template("services/show.html")

@tasks_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", animals= animals)

@tasks_blueprint.route("/animals/<id>")
def animal(id):
    animal = animal_repository.select(id)
    return render_template("animals/show.html", animal= animal)
    
@tasks_blueprint.route("/animals/new")
def new_animal():
    vets = vet_repository.select_all()
    return render_template("animals/new.html", vets= vets)

@tasks_blueprint.route("/animals/new", methods=["POST"])
def save_animal():
    
    vet_id = request.form["vet_id"]
    vet = vet_repository.select(vet_id)
    animal_name= request.form['pet_name']
    date_of_birth = request.form['date_of_birth']
    treatment= request.form['treatment']
    specie = request.form['specie']
    animal = Animal(animal_name, date_of_birth,specie, vet, treatment)
    animal_repository.save(animal)
    return redirect("/animals")
    
@tasks_blueprint.route("/animals/<id>/delete")
def delete_animal(id):
    animal_repository.delete(id)
    return redirect("/animals")

@tasks_blueprint.route("/animals/<id>/edit")
def edit_animal(id):
    vets = vet_repository.select_all()
    animal= animal_repository.select(id)
    return render_template("/animals/edit.html", animal=animal, vets=vets)  

@tasks_blueprint.route("/users/<id>/delete")
def delete_user(id):
    user_repository.delete(id)
    return redirect("/users")


