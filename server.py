from flask_app import app

# remember to import controller here

from flask_app.controllers import users

if __name__ == "__main__":
    app.run(debug=True)
