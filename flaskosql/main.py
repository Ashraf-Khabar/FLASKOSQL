from db import Connect
from model import Model
from field import MySQLField

connection = Connect.get_mysql_connection('root', '1453', 'localhost', 3306, 'mydb')
print(connection)
if connection:
    print("Connected to the MySQL database.")

    # Create the connection for the model:
    Model.set_connection(connection=connection)

    class Roles(Model):
        ID = MySQLField(column_name="id", data_type="INT", primary_key=True, auto_increment=True)
        NAME = MySQLField(column_name="name", data_type="VARCHAR(100)", nullable=False)
        AGE = MySQLField(column_name="age", data_type="VARCHAR(100)", nullable=False)

    # Create the table for the model
    Roles.create_table(fresh=False)

else:
    print("Failed to connect to the database.")