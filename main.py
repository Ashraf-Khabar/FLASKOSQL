import cx_Oracle
from flask import Flask, jsonify
from __db__ import Connect
from __field__ import Field
from __model__ import Model

app = Flask(__name__)

# Define the main table:
class Students(Model):
    id = Field("id", "NUMBER", primary_key=True)
    name = Field("name", "VARCHAR2(100)", nullable=False)
    last_name = Field("last_name", "VARCHAR2(100)", nullable=False)
    CNE = Field("CNE", "VARCHAR2(100)", unique=True, nullable=False)
    __primary_key__ = ("id", "CNE")  # Define a composite primary key

# Initialize the model, the field, and the Flask API:
Students.create_table()
student = Students(id=1, name="Ashraf", last_name="KHABAR", CNE="1234ER5")

# Creation of student : 
def create_student():
    # Create a new user
    student.save()
    
# Updating the user :
def update_student():
    student.name = "Asharf AAA"
    # Call the update() method to save the changes to the database
    student.update()


def main():
    connection = Connect('orm', 'ormpw', 'localhost', 1521, 'orcl')
    if connection.connect():
        print("Connected")
    else:
        print("Not connected")
    # app.run()

if __name__ == "__main__":
    # create_student()
    update_student()
    main()
