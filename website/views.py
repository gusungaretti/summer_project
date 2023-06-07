from flask import Blueprint, render_template

views = Blueprint('views', __name__)


#when you go to the url and navigate to the url that ends in "/" in this case, or whatever you want the url to end with, it runs all the code below it
@views.route('/')
def home():
  return render_template("home.html")
