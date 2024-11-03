from flask import render_template

from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/login')
def index():
    return render_template("login.html")




@app.route('/contact')
def contact():
    return render_template("contact.html")





