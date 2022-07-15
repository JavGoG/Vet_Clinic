from flask import Flask, render_template, Blueprint, request, redirect

vets_blueprint = Blueprint("vets",__name__ )

# INDEX
@vets_blueprint.route("/vets")
def index():
    return render_template("vets/index.html")

