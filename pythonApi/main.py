from flask import Flask, request, jsonify

# Importing necessary modules from Flask: Flask for creating the web application,
# request for handling incoming requests, and jsonify for returning JSON responses.
# These modules are essential for building APIs using Flask.

app = Flask(__name__)

# Creating a Flask application instance. '__name__' is a special Python variable
# that represents the name of the current module (this script).

@app.route("/get-user/<user_id>")  
def get_user(user_id):
    # This decorator @app.route("/get-user/<user_id>") registers a new route 
    # in the application. When a request is made to "/get-user/<user_id>", 
    # Flask will invoke the decorated function (get_user) and pass <user_id>
    # as an argument.

    user_data = {
        "user_id": user_id,
        "name": "Robin Wick",
        "email": "Robin.wick@example.com"
    }
    # Creating a dictionary user_data containing basic information about a user.

    extra = request.args.get("extra") 
    # Using request.args.get("extra") to retrieve the 'extra' parameter from 
    # the query string of the URL. This allows additional data to be passed
    # with the request.

    if extra:
        user_data["extra"] = extra
        # If 'extra' parameter is provided in the request, add it to user_data.

    return jsonify(user_data), 200
    # Returning user_data as a JSON response using jsonify() and specifying
    # HTTP status code 200 (OK) indicating successful request.

if __name__ == "__main__":
    app.run(debug=True)
    # This conditional block ensures that the Flask web server is started only
    # when this script is executed directly (not when imported as a module).
    # Running the server in debug mode (debug=True) provides helpful debugging
    # information on errors.

# THE FOLLOWING IS A POST REQUEST
@app.route("/create-user", methods=["POST"])
def create_user():
    # Adding another route using @app.route decorator. This route handles 
    # POST requests to "/create-user". The 'methods' parameter specifies that 
    # this route only accepts POST requests.

    data = request.get_json()
    # Using request.get_json() to extract JSON data from the incoming POST request.
    # This function parses the incoming JSON payload and returns it as a Python dictionary.

    return jsonify(data), 201
    # Returning the received JSON data as a JSON response with HTTP status code 201 
    # (Created), indicating successful creation of a resource.