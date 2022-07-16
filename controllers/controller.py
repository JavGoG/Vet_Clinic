from flask import Flask, render_template, Blueprint, request, redirect

tasks_blueprint = Blueprint("vets",__name__ )

# INDEX
@tasks_blueprint.route("/vets")
def index():
    return render_template("vets/index.html")

