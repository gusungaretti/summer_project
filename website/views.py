from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .tuition import *


views = Blueprint('views', __name__)

#when you go to the url and navigate to the url that ends in "/" in this case, or whatever you want the url to end with, it runs all the code below it
@views.route('/')
def main():
  return render_template("main.html", user=current_user)

@views.route('/home')
@login_required
def home():
  return render_template("home.html", user=current_user, data= tuition_data.to_html())

@views.route('/university')
def university():
  return render_template("university.html", user=current_user)

@views.route('/college')
def college():
  return render_template("college.html", user=current_user)