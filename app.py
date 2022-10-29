import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


# from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "HACKTOBER"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Courses(db.Model):
    identifier = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    units = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(600), nullable=False)
    other = db.Column(db.String(400), nullable=False)


def __repr__(self):
    return f"identifier = {identifier}, name = {name}, units = {units}, description = {description}, other={other}"
