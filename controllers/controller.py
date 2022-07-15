from flask import Flask, render_template, request, redirect
from flask import Blueprint

tasks_blueprint = Blueprint("home", __name__)

@tasks_blueprint.route("/home")
def index():
    return render_template("index.html")

