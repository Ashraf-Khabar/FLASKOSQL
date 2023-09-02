from db import Connect  # Import your database connection module
from model import Model
from field import MySQLField

def main():
    # Establish a MySQL database connection
    connection = Connect.get_mysql_connection('root', '1453', 'localhost', 3306, 'mydb')
    if connection:
        Model.set_connection(connection=connection)

        # Define your model class and fields
        class Roles(Model):
            ID = MySQLField(column_name="id", data_type="INT", primary_key=True, auto_increment=True)
            NAME = MySQLField(column_name="name", data_type="VARCHAR(100)", nullable=False)
            AGE = MySQLField(column_name="age", data_type="INT", nullable=False)  # Corrected data_type

        # Create the table for the model
        Roles.create_table(fresh=True)

        # Insert a record
        new_role = Roles(NAME="Admin", AGE=30)
        new_role.save()

        # Fetch a record by condition
        fetched_role = Roles.get(NAME="Admin")
        if fetched_role:
            print(f"Fetched Role: {fetched_role.NAME}, Age: {fetched_role.AGE}")

        # Fetch all records
        all_roles = Roles.getAll()
        for role in all_roles:
            print(f"Role: {role.NAME}, Age: {role.AGE}")

    else:
        print("Failed to connect to the database.")

if __name__ == "__main__":
    main()
