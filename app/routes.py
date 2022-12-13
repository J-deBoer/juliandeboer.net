import os.path

from app import app
from flask import render_template, Flask, request, redirect, url_for




@app.route('/')
def home():
    return render_template('index.html', title='Home')
