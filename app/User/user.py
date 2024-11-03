from app import app
from flask import render_template, request, jsonify, make_response,redirect ,url_for

from app.User.user_model import UserDatabase,UserModel,check_user_model_connection

@app.route('/sign-up')
def signup():
    return render_template("sign_up.html")

# # LOGIN HANDLING API's AND ALL
# @app.route('/getData_login', methods=['POST'])
# def get_data_login():
#     # Get the data from the request
#     data = request.get_json()  # Parses the incoming JSON data

#     if not data:

#         return jsonify({"error": "No data received"}), 400

#     # Extract email and password
#     email = data.get('email')
#     password = data.get('password')

#     print(f"Received email: {email}")
#     print(f"Received password: {password}")

#     # Validate email and password
#     if email != "Garsame@gmail.com":
#         my_response = {
#             'message': 'Invalid email address!',
#             'status': 'error'
#         }
#         return jsonify(my_response), 200

#     if password != "123":
#         my_response = {
#             'message': 'Passsword-kaagu waa khalad',
#             'status': 'error'
#         }
#         print("Xogtaadu way khaldan  tahay, Fadlan iska hubi")
#         return jsonify(my_response), 200

#     # If validation is successful

#     my_response = {
#         'message': 'Login successful!',
#         'status': 'success',
#         'data': {
#             'email': email,
#             'Password': password
#         }
#     }
#     print('Xogtaadu way saxan ytahay, Mahadsanid')
#     return make_response(jsonify(my_response), 200)


# ChatGPT
@app.route('/getData_login', methods=['POST'])
def get_data_login():
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

    # If validation is successful
    return jsonify({
        'message': 'Login successful!',
        'status': 'success',
        'data': {
            'email': email
        }
    }), 200




from flask import jsonify, request, make_response

@app.route('/getData_signup', methods=["POST"])
def get_signup_data():
    if request.method == 'POST':
        data = request.get_json()
        print("Received data:", data)

        if data.get('first_name') and data.get('second_name') and data.get('email') and\
            data.get('phone') and data.get('password') and data.get('second_name'):
            
            print('Connecting to the database...')
            # Checking database connectivity
            connection_status, user_model = check_user_model_connection() # True, False

            if connection_status:
                print('You are connected to the database successfully!')

                flag , result = user_model.register_user(data.get('first_name'),
                                         data.get('second_name'),
                                         data.get('email'),
                                         data.get('phone'),
                                         data.get('password'))
                

                
                # Check the data
                if flag:
                    print('Fiican, si saxan ayaa loo keydiyay xogta')
                    return jsonify({"status": "success", "message": "Fiican, si saxan ayaa loo keydiyay xogta"}), 400
                else:
                    print('Wax baa khaldamay , xogta lama xareyn')
                    return jsonify({"status": "Error", "message": "Wax baa khaldamay , xogta lama xareyn"}), 400



            else:
                print(f'Database Connection {user_model}')
                print('Wax baa khaldamay , kuma xirmi karno salka xogta!')
                return jsonify({"status": "Error", "message": "Wax baa khaldamay ,  kuma xirmi karno salka xogta!"}), 400



        else:
            return jsonify({"status": "Error", "message": "Xog diristaadu way khaldaneyd!"}), 400

            # Send a successful response
            return jsonify({"status": "Success", "message": "Data received"}), 200
    else:
        return jsonify({"status": "Error", "message": "Invalid request"}), 400







    # data = request.get_json()  # Parse JSON data from the request


    # # Extract data fields
    # f_name = data.get("first_name")
    # s_name = data.get("second_name")
    # my_email = data.get("email")
    # phone_num = data.get("phone")
    # password = data.get("password")
    # confirm_pass = data.get("confirm_password")

    # print(data)  # For debugging purposes

    # # Validation logic (customized messages)
    # if my_email != "Garsame@gmail.com":
    #     return jsonify({'message': 'Invalid email address!', 'status': 'error'}), 200
    # elif len(f_name) > 40 or len(s_name) > 40:
    #     return jsonify({'message': 'Magaca kowad ama labaad wa inuu ka yaraada 40 xaraf!', 'status': 'error'}), 200
    # elif len(password) < 6:
    #     return jsonify({'message': 'Password ku wa inuu ugu yaraan la ekaada 6 digit!.', 'status': 'error'}), 200
    # elif password != confirm_pass:
    #     return jsonify({'message': 'Passwords do not match!', 'status': 'error'}), 200
    # elif not phone_num.isdigit() or len(phone_num) > 13:
    #     return jsonify({'message': 'Phone number ku waa khalad!', 'status': 'error'}), 200

    # # Success response
    # response_data = {
    #     'message': 'Xogtaada si saxan ayaa loo xareeyay!',
    #     'status': 'Success',
    #     'data': {
    #         'first_name': f_name,
    #         'second_name': s_name,
    #         'email': my_email,
    #         'phone': phone_num
    #     }
    # }
    # return jsonify(response_data), 200

@app.route('/Users/Dashboard')
def open_user_dashboard():
    return render_template('Users/user_dashboard.html')