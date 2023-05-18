from flask import Flask, jsonify
from __db__ import Connect
from __field__ import Field
from __model__ import Model
import Models.UsersModel as Model

app = Flask(__name__)

# Initialize the model, the field, and the Flask API:
users = Model.Users()
users.create_table() 

# Creation of users : 
def create_users():
    user = users(1, "ASHRAF", "KHABAR", "HSY1425")
    # Create a new user
    user.save()
    
def get_user(user_id):
    # Retrieve a user by ID
    user = users.get(user_id)
    if user:
        print(f"User: {user.id}, {user.name}")
    else:
        print("User not found")
    
# Updating the user :
def update_users():
    users.name = "Asharf"
    print("test")
    # Call the update() method to save the changes to the database
    users.update()
   
def delete_user(user_id):
    # Delete a user by ID
    user = users.get(user_id)
    if user:
        user.delete()
        print("User deleted successfully")
    else:
        print("User not found")

   
create_users()

