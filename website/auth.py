#Movie and Television Tracker

from flask import Blueprint, render_template, request, flash
from .models import User

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():

  #when you but the submitted form into a variable (ie.data), it is stored as a list with tuples 
  #ie. [('email', 'liz@gmail.com'), ('password', '1234')]
  data= request.form
  return render_template("login.html", boolean=True)


@auth.route("/logout")
def logout():
  return "<p>Logout</p>"


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():

  if request.method== 'POST':
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    #address= email.find("@")

    # if email[(address + 1):] != "gmail.com" or  email[(address + 1):] != "yahoo.com" or  email[(address + 1):] != "hotmail.com":
    #   flash("Not a valid email adress", category= 'error')

    if len(email) < 4:
      flash("Email must be greater than 3 characters.", category= 'error')
    elif len(firstName) < 2:
      flash("First name must be greater than 1 character.", category= 'error')
    elif password1 != password2:
      flash("Passwords must be the same.", category= 'error')
    elif len(password1) < 7:
      flash("Password must be greater than 7 characters.", category= 'error')
    else:
      flash("Account create!", category= 'success')


  data= request.form
  return render_template("sign_up.html")

