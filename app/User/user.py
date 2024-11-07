from app import app
from flask import render_template, request, jsonify, make_response, redirect, url_for, session
import os

from app.User.user_model import UserDatabase, UserModel, check_user_model_connection

app.secret_key = 'Gaabka'

# Route to display the signup page
@app.route('/sign-up')
def signup():
    if 'email' not in session:  # Check if email is in session
        return render_template('sign_up.html') # Redirect to signup/login if not logged in
    return redirect(url_for('open_user_dashboard'))
# Route to display the signup page, restricted for logged-in users
# @app.route('/sign-up')
# def signup():
#     if 'email' in session:  # If logged in, redirect to dashboard
#         return redirect(url_for('open_user_dashboard'))
#     return render_template("sign_up.html")  # If not logged in, show signup page
    




@app.route('/login')
def index():
    if 'email' not in session:  # Check if email is in session
        return render_template('login.html') # Redirect to signup/login if not logged in
    return redirect(url_for('open_user_dashboard'))
    

# Login route
@app.route('/getData_login', methods=['POST'])
def get_data_login():
    if not 'email' in session:

        data = request.get_json()  # Parse the incoming JSON data

        if not data:
            return jsonify({"error": "No data received"}), 400

        # Extract email and password
        email = data.get('email')
        password = data.get('password')

        # Check database connection
        connection_status, user_model = check_user_model_connection()
        if not connection_status:
            return jsonify({'message': 'Database connection failed', 'status': 'error'}), 500

        # Validate email and password with the database
        if not user_model.login_user(email, password):
            return jsonify({
                'message': 'Invalid email or password!',
                'status': 'error'
            }), 200

        # If validation is successful, add the user's email to the session
        session['email'] = email  # Store the email in the session

        return jsonify({
            'message': 'Login successful!',
            'status': 'success',
            'data': {
                'email': email
            }
        }), 200
    else:
        return redirect(url_for('index'))

# Logout route to clear session data
@app.route('/logout')
def logout():
    session.pop('email', None)  # Remove the email from the session
    return redirect(url_for('signup'))  # Redirect to the signup page (or login)

# Route to handle signup data
@app.route('/getData_signup', methods=["POST"])
def get_signup_data():
    if request.method == 'POST':
        data = request.get_json()
        print("Received data:", data)

        if data.get('first_name') and data.get('second_name') and data.get('email') and\
            data.get('phone') and data.get('password') and data.get('second_name'):

            print('Connecting to the database...')
            # Checking database connectivity
            connection_status, user_model = check_user_model_connection()

            if connection_status:
                print('You are connected to the database successfully!')

                flag, result = user_model.register_user(data.get('first_name'),
                                                        data.get('second_name'),
                                                        data.get('email'),
                                                        data.get('phone'),
                                                        data.get('password'))

                if flag:
                    print('Fiican, si saxan ayaa loo keydiyay xogta')
                    return jsonify({"status": "success", "message": "Fiican, si saxan ayaa loo keydiyay xogtaada, fadlan booqo login page si aad u hesho looxaaga"}), 200
                else:
                    print('Wax baa khaldamay, xogta lama xareyn')
                    return jsonify({"status": "Error", "message": "Wax baa khaldamay, xogta lama xareyn"}), 400

            else:
                print(f'Database Connection {user_model}')
                print('Wax baa khaldamay, kuma xirmi karno salka xogta!')
                return jsonify({"status": "Error", "message": "Wax baa khaldamay, kuma xirmi karno salka xogta!"}), 400

        else:
            return jsonify({"status": "Error", "message": "Xog diristaadu way khaldaneyd!"}), 400
    else:
        return jsonify({"status": "Error", "message": "Invalid request"}), 400


# User Dashboard 
@app.route('/Users/Dashboard')
def open_user_dashboard():
    if 'email' not in session:  # Check if email is in session
        return redirect(url_for('index'))  # Redirect to login if not logged in

    # Get the logged-in user's email
    email = session['email']

    # Connect to the database and get the user data
    connection_status, user_model = check_user_model_connection()
    if not connection_status:
        return jsonify({"error": "Database connection failed"}), 500

    # Fetch the user data using the email stored in the session
    sql = "SELECT first_name, second_name, email, phone_number FROM registration WHERE email = %s"
    user_model.cursor.execute(sql, (email,))
    user_data = user_model.cursor.fetchone()  # Fetch the user data from the database

    if not user_data:
        return redirect(url_for('index'))  # If no user data is found, redirect to login

    # Extract user information
    first_name = user_data[0]
    second_name = user_data[1]
    phone_number = user_data[3]

    return render_template('Users/user_dashboard.html', first_name=first_name, second_name=second_name, phone_number=phone_number, email=email)
