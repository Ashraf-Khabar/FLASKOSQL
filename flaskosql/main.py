from flaskosql.db import Connect
from model import Model
from flaskosql.field import Field


# Setup the connection : 
connection = Connect('orm', 'ormpw', 'localhost', '1521', 'orcl').get_connection()
# CReate the connection for the model  :
Model.set_connection(connection=connection)

class Roles(Model):
    ID = Field("id", "NUMBER", primary_key=True)
    NAME = Field("name", "VARCHAR2(100)", nullable=False)
    AGE = Field("age", "VARCHAR2(100)", nullable=False)
    
    

Roles.create_table(fresh=True)

# roles = Roles.countAll()