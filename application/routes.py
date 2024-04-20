from urllib import request
from flask.templating import render_template_string
from werkzeug.datastructures import RequestCacheControl
from application import app
from werkzeug.utils import redirect
from application import db
from flask import render_template, flash , request
from .forms import Classe
from .forms import Etudiant

@app.route("/")
def index():
    return render_template("view_classes.html", title = "Layout page")

@app.route("/add_class", methods=["POST", "GET"])
def add_class():
    if request.method == "POST":
       form = Classe(request.form)
       classe_name = form.name.data
       completed = form.completed.data
       
       db.etudiante_flask.insert_one({
           "name": classe_name,    
       })
       flash("Etudiant successfully added", "success")
       return redirect("/")
    else:
        form = Classe()
    return render_template("add_class.html", form = form)

@app.route("/")
def index():
    return render_template("view_etudiant.html", title = "Layout page")

@app.route("/add_etudiant", methods=["POST", "GET"])
def add_etudiant():
    if request.method == "POST":
       form = Etudiant(request.form)
       etudiant_name = form.name.data
       classe_name = form.nameE.data
       completed = form.completed.data
       
       db.etudiante_flask.insert_one({
           "name": etudiant_name,    
           "nameC":classe_name,    
       })
       flash("Etudiant successfully added", "success")
       return redirect("/")
    else:
        form = Etudiant()
    return render_template("add_etudiant.html", form = form)