from flask import Blueprint, render_template,send_file
from flask_login import login_required, current_user,login_user,logout_user
from . import db
from flask import Flask,render_template,url_for,flash,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.file import FileField
from wtforms import SubmitField
import sqlite3
from flask_wtf import Form
from io import BytesIO
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('intro.html')
@main.route('/home')
@login_required
def home():
    return render_template('index.html',name=current_user.name)
@main.route('/team')
def team():
    return render_template('team.html')

@main.route('/contact')
def contact():
    return render_template('form.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',name=current_user.name,email=current_user.email)

@main.route("/handle_data",methods=['POST','GET'])
def handle_data():
    projectpath = request.form['projectFilepath']
    if(projectpath=='mathematics'):
        posts=['calculus','probability','differential equations','linearalgebra']
        return render_template('courseview.html',post=posts)
    elif(projectpath=='design'):
        posts=['systems thinking','concepts in engineering design','design history']
        return render_template('courseview.html',post=posts)
    elif(projectpath=='computers'):
        posts=['computerorganisation','algorithms','dbms','c programming','datastructures','discrete structures for computing']
        return render_template('courseview.html',post=posts)



