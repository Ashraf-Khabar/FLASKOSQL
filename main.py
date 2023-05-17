from flask import Flask, jsonify
from __db__ import Connect
from __field__ import Field
from __model__ import Model
import Models.UsersModel as Model

app = Flask(__name__)

# Initialize the model, the field, and the Flask API:

Model.Users.create_table()
student = Model.Users(id=1, name="Ashraf", last_name="KHABAR", CNE="1234ER5")

# Creation of student : 
def create_student():
    # Create a new user
    student.save()
    
# Updating the user :
def update_student():
    student.name = "Asharf"
    # Call the update() method to save the changes to the database
    student.update()


def main():
    connection = Connect()
    if connection.connect():
        print("Connected")
    else:
        print("Not connected")

if __name__ == "__main__":
    create_student()
    # update_student()
    main()
