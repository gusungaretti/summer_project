from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import pandas as pd
import csv


#tuition_by_program = "website\Average_Tuition_by_Program_Canada.csv"

tuition_data = pd.read_csv("Average_Tuition_by_Program_Canada.csv", on_bad_lines='skip')
tuition_data= pd.DataFrame(tuition_data[2:])

