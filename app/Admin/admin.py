# Here is the views for the admin
from flask import Flask, render_template, redirect, request, session, url_for, flash
from app import app


@app.route('/Admin/Dashboard')
def dashboard():
    if not 'admin_email' in session:  # Check if the user is logged in (session exists)

        return render_template('Admin/dashboard.html')
    else:
        return redirect(url_for('Admin_login'))  # Redirect to login if not logged in


@app.route('/Admin/login', methods=['GET', 'POST'])
def Admin_login():
    if request.method == 'POST':
        Admin_email = request.form.get('Admin_email')
        Admin_pass = request.form.get('Admin_pass')

        # Replace this with actual authentication logic (e.g., checking a database)
        if Admin_email == "Garsame@gmail.com" and Admin_pass == "123":
            session['admin_email'] = Admin_email  # Set session data
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password. Please try again.", "error")  # Flash error message

    return render_template('Admin/login.html')


