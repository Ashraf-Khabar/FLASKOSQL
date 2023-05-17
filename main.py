from flask import Flask, jsonify
from __db__ import Connect
from __field__ import Field
from __model__ import Model
import Models.UsersModel as Model

app = Flask(__name__)

# Initialize the model, the field, and the Flask API:

Model.Users.create_table()
users = Model.Users(id=1, name="Ashraf", last_name="KHABAR", CNE="1234ER5")

# Creation of users : 
def create_users():
    # Create a new user
    users.save()
    
# Updating the user :
def update_users():
    users.name = "Asharf"
    print("test")
    # Call the update() method to save the changes to the database
    users.update()


def main():
    connection = Connect()
    if connection.connect():
        print("Connected")
    else:
        print("Not connected")

if __name__ == "__main__":
    create_users()
    update_users()
    main()
