from db import Connect
from model import Model
from field import MySQLField

connection = Connect.get_mysql_connection('root', '1453', 'localhost', 3306, 'mydb')
if connection:
    Model.set_connection(connection=connection)

    class Roles(Model):
        ID = MySQLField(column_name="id", data_type="INT", primary_key=True, auto_increment=True)
        NAME = MySQLField(column_name="name", data_type="VARCHAR(100)", nullable=False)
        AGE = MySQLField(column_name="age", data_type="VARCHAR(100)", nullable=False)

    # Create the table for the model
    Roles.create_table(fresh=True)

else:
    print("Failed to connect to the database.")