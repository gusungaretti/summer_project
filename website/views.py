from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

#when you go to the url and navigate to the url that ends in "/" in this case, or whatever you want the url to end with, it runs all the code below it
@views.route('/')
def main():
  return render_template("main.html", user=current_user)

@views.route('/home')
@login_required
def home():
  return render_template("home.html", user=current_user)

@views.route('/movies')
def movies():
  return render_template("movies.html", user=current_user)

@views.route('/television')
def television():
  return render_template("television.html", user=current_user)