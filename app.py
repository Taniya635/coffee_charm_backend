from flask import Flask, jsonify,request, render_template, session
import mysql.connector
import os

os.environ.get('KEY')

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Taniya@123',
    'database': 'taniyadb',
    'port': 3306 
}

def get_mysql_connection():
     return mysql.connector.connect(**db_config)
    

# print("Connection established")
app = Flask(__name__)
app.debug = True



# GET request for /

@app.route('/', methods=['GET'])
def get_data_from_mysql():
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Example query - replace this with your own query
        query = "SELECT * FROM soaps;"
        cursor.execute(query)

        # Fetch the data and jsonify the result
        data = cursor.fetchall()
        result = [dict(zip(cursor.column_names, row)) for row in data]

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return jsonify(result)
        # print(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

#POST request for /
@app.route('/', methods=['POST'])    
def add_data_to_mysql():
    try:

        new_data = request.get_json()


        conn = get_mysql_connection()
        cursor = conn.cursor()


        insert_query = "INSERT INTO soaps (images, title, description, price, category) VALUES (%s, %s, %s, %s,%s)"
        cursor.execute(insert_query, (new_data['images'], new_data['title'], new_data['description'], new_data['price'], new_data['category']))
        conn.commit()


        cursor.close()
        conn.close()

        return jsonify({'message': 'Record added successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


#PATCH request for /
@app.route('/update_data/<int:id>', methods=['PATCH'])
def update_data_in_mysql(id):
    try:
        # Get the new data from the request's JSON payload
        updated_data = request.get_json()

        # Establish connection and create cursor
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Check if the record with the given ID exists
        check_query = "SELECT * FROM soaps WHERE id = %s"
        cursor.execute(check_query, (id,))
        existing_record = cursor.fetchone()

        if not existing_record:
            return jsonify({'error': 'Record not found'}), 404

        # Update the record with the new data
        update_query = "UPDATE soaps SET images = %s, title = %s, description = %s, price= %s, category= %s WHERE id = %s"
        cursor.execute(update_query, (updated_data['images'], updated_data['title'], updated_data['description'], updated_data['price'], updated_data['category'], id))
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return jsonify({'message': 'Record updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

#DELETE request for /
@app.route('/delete_data/<int:id>', methods=['DELETE'])
def delete_data_from_mysql(id):
    try:
        # Establish connection and create cursor
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Check if the record with the given ID exists
        check_query = "SELECT * FROM soaps WHERE id = %s"
        cursor.execute(check_query, (id,))
        existing_record = cursor.fetchone()

        if not existing_record:
            return jsonify({'error': 'Record not found'}), 404

        # Delete the record with the given ID
        delete_query = "DELETE FROM soaps WHERE id = %s"
        cursor.execute(delete_query, (id,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'Record deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
############################################################################################################
    
#GET request for home
    
@app.route('/home', methods=['GET'])
def get_home():
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Example query - replace this with your own query
        query = "SELECT * FROM home_page;"
        cursor.execute(query)

        # Fetch the data and jsonify the result
        data = cursor.fetchall()
        result = [dict(zip(cursor.column_names, row)) for row in data]

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return jsonify(result)
        # print(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

#POST request for home    
    
@app.route('/home', methods=['POST'])    
def add_home():
    try:

        new_data = request.get_json()


        conn = get_mysql_connection()
        cursor = conn.cursor()


        insert_query = "INSERT INTO home_page (images, title, price, description, category) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (new_data['images'], new_data['title'], new_data['price'], new_data['description'], new_data['category']))
        conn.commit()


        cursor.close()
        conn.close()

        return jsonify({'message': 'Record added successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
#PATCH request for home
@app.route('/home/update_data/<int:id>', methods=['PATCH'])
def update_home(id):
    try:
        # Get the new data from the request's JSON payload
        updated_data = request.get_json()

        # Establish connection and create cursor
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Check if the record with the given ID exists
        check_query = "SELECT * FROM home_page WHERE id = %s"
        cursor.execute(check_query, (id,))
        existing_record = cursor.fetchone()

        if not existing_record:
            return jsonify({'error': 'Record not found'}), 404

        # Update the record with the new data
        update_query = "UPDATE home_page SET images = %s, title = %s, price = %s, description= %s, category= %s WHERE id = %s"
        cursor.execute(update_query, (updated_data['images'], updated_data['title'], updated_data['price'], updated_data['description'], updated_data['category'], id))
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return jsonify({'message': 'Record updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
#DELETE request for home
@app.route('/home/delete_data/<int:id>', methods=['DELETE'])
def delete_home(id):
    try:
        # Establish connection and create cursor
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Check if the record with the given ID exists
        check_query = "SELECT * FROM home_page WHERE id = %s"
        cursor.execute(check_query, (id,))
        existing_record = cursor.fetchone()

        if not existing_record:
            return jsonify({'error': 'Record not found'}), 404

        # Delete the record with the given ID
        delete_query = "DELETE FROM home_page WHERE id = %s"
        cursor.execute(delete_query, (id,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'Record deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


###################################################################################################################
    

#GET request for face
@app.route('/face', methods=['GET'])
def get_face_serums():
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Example query - replace this with your own query
        query = "SELECT * FROM face_serums;"
        cursor.execute(query)

        # Fetch the data and jsonify the result
        data = cursor.fetchall()
        result = [dict(zip(cursor.column_names, row)) for row in data]

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return jsonify(result)
        # print(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
#POST request for face
    
@app.route('/face', methods=['POST'])    
def add_face():
    try:

        face_data = request.get_json()


        conn_2 = get_mysql_connection()
        cursor = conn_2.cursor()


        insert_query = "INSERT INTO face_serums (images, title, price, description, category) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (face_data['images'], face_data['title'], face_data['price'], face_data['description'], face_data['category']))
        conn_2.commit()


        cursor.close()
        conn_2.close()

        return jsonify({'message': 'Record added successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
#PATCH request for face
@app.route('/face/update_data/<int:id>', methods=['PATCH'])
def update_face(id):
    try:
        # Get the new data from the request's JSON payload
        updated_data = request.get_json()

        # Establish connection and create cursor
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Check if the record with the given ID exists
        check_query = "SELECT * FROM face_serums WHERE id = %s"
        cursor.execute(check_query, (id,))
        existing_record = cursor.fetchone()

        if not existing_record:
            return jsonify({'error': 'Record not found'}), 404

        # Update the record with the new data
        update_query = "UPDATE face_serums SET images = %s, title = %s, price = %s, description= %s, category= %s WHERE id = %s"
        cursor.execute(update_query, (updated_data['images'], updated_data['title'], updated_data['price'], updated_data['description'], updated_data['category'], id))
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return jsonify({'message': 'Record updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
#DELETE request for face
@app.route('/face/delete_data/<int:id>', methods=['DELETE'])
def delete_face(id):
    try:
        # Establish connection and create cursor
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Check if the record with the given ID exists
        check_query = "SELECT * FROM face_serums WHERE id = %s"
        cursor.execute(check_query, (id,))
        existing_record = cursor.fetchone()

        if not existing_record:
            return jsonify({'error': 'Record not found'}), 404

        # Delete the record with the given ID
        delete_query = "DELETE FROM face_serums WHERE id = %s"
        cursor.execute(delete_query, (id,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'Record deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

###################################################################################################################
    

#GET request for oil
@app.route('/oil', methods=['GET'])
def get_oil():
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Example query - replace this with your own queryyy
        query = "SELECT * FROM oils_serums;"
        cursor.execute(query)

        # Fetch the data and jsonify the result
        data = cursor.fetchall()
        result = [dict(zip(cursor.column_names, row)) for row in data]

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return jsonify(result)
        # print(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
#POST request for oil
    
@app.route('/oil', methods=['POST'])    
def add_oil():
    try:

        oil_data = request.get_json()


        conn_3 = get_mysql_connection()
        cursor = conn_3.cursor()


        insert_query = "INSERT INTO oils_serums (images, title, price, description, category) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (oil_data['images'], oil_data['title'], oil_data['price'], oil_data['description'], oil_data['category']))
        conn_3.commit()


        cursor.close()
        conn_3.close()

        return jsonify({'message': 'Record added successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
#PATCH request for oils
@app.route('/oil/update_data/<int:id>', methods=['PATCH'])
def update_oil(id):
    try:
        # Get the new data from the request's JSON payload
        updated_data = request.get_json()

        # Establish connection and create cursor
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Check if the record with the given ID exists
        check_query = "SELECT * FROM oils_serums WHERE id = %s"
        cursor.execute(check_query, (id,))
        existing_record = cursor.fetchone()

        if not existing_record:
            return jsonify({'error': 'Record not found'}), 404

        # Update the record with the new data
        update_query = "UPDATE oils_serums SET images = %s, title = %s, price = %s, description= %s, category= %s WHERE id = %s"
        cursor.execute(update_query, (updated_data['images'], updated_data['title'], updated_data['price'], updated_data['description'], updated_data['category'], id))
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return jsonify({'message': 'Record updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
#DELETE request for oils

@app.route('/oil/delete_data/<int:id>', methods=['DELETE'])
def delete_oil(id):
    try:
        # Establish connection and create cursor
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Check if the record with the given ID exists
        check_query = "SELECT * FROM oils_serums WHERE id = %s"
        cursor.execute(check_query, (id,))
        existing_record = cursor.fetchone()

        if not existing_record:
            return jsonify({'error': 'Record not found'}), 404

        # Delete the record with the given ID
        delete_query = "DELETE FROM oils_serums WHERE id = %s"
        cursor.execute(delete_query, (id,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'Record deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

####################################################################################################################

#GET, POST for register
@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == 'POST':
            # Get the user data from the form
            username = request.form['username']
            password_hash = request.form['password']
            email = request.form['email']

            # Add the user to the database
            conn = get_mysql_connection()
            cursor = conn.cursor()
            query = "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, email, password_hash))
            conn.commit()
            conn.close()

            # Perform any other actions or validations as needed
            # Redirect the user to a success page or login page

            return f"Registration successful for {username}!"

        # If the request method is GET, return the registration form
        return render_template('register.html')

    except Exception as e:
        return f"An error occurred: {e}"
    
###################################################################################################################
        
        

#GET, POST for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the user data from the form
        username = request.form['username']
        password_hash = request.form['password']

        # Check user credentials against the database
        conn = get_mysql_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password_hash))
        user = cursor.fetchone()
        conn.close()
        if user:
            # User credentials are correct, perform any login actions or session management here
            return f"Login successful for {username}!"
        else:
            # Authentication failed, handle invalid login here (e.g., display an error message)
            return "Invalid login credentials"

    # If the request method is GET, return the login form
    return render_template('login.html')

####################################################################################################################


#GET, POST for cart
@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if 'cart' not in session:
        session['cart'] = []  # Initialize an empty cart list in the session

    if request.method == 'POST':
        product_id = int(request.form['product_id'])
        # You might fetch product details from the database based on the product_id
        # For simplicity, we'll just store the product_id in the cart.

        session['cart'].append(product_id)

    # Fetch the cart items and display them in the cart template
    cart_items = session['cart']
    product_names = []  # We'll fetch product names from the database here
    conn = get_mysql_connection()
    cursor = conn.cursor()

    product_names = []
    for product_id in cart_items:
        query = "SELECT quantity FROM cart WHERE product_id = %s"
        cursor.execute(query, (product_id,))
        product_name = cursor.fetchone()
        if product_name:
            product_names.append(product_name[0])

    conn.close()

    return render_template('cart.html', cart_items=product_names)

#####################################################################################################################

#GET, POST for payment
@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        # Simulate the payment process (assuming a successful payment)
        card_number = request.form['card_number']
        card_expiry = request.form['card_expiry']
        card_cvv = request.form['card_cvv']
        if 'cart' in session:
            # Save the order to the database before clearing the cart
            save_order_to_database(session['cart'])

            session.pop('cart', None)

        return "Payment successful! Thank you for your purchase!"

    # If the request method is GET, display the payment page
    return render_template('payment.html')


#for order
def save_order_to_database(cart_items):
    # Connect to the database and save the order details
    conn = get_mysql_connection()
    cursor = conn.cursor()

    # Assuming you have an 'orders' table with the necessary columns (e.g., user_id, product_id, quantity, etc.)
    for product_id in cart_items:
        user_id = 1  # Replace this with the actual user_id for the logged-in user
        quantity = 1  # Replace this with the actual quantity of the product in the cart

        # Insert the order details into the 'orders' table
        query = "INSERT INTO orders (user_id, product_id, quantity) VALUES (%s, %s, %s)"
        cursor.execute(query, (user_id, product_id, quantity))

    conn.commit()
    conn.close()
    return



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)