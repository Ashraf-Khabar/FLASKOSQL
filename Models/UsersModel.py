from __field__ import Field
from __model__ import Model

# Define the main table:
class Users(Model):
    id = Field("id", "NUMBER", primary_key=True)
    name = Field("name", "VARCHAR2(100)", nullable=False)
    last_name = Field("last_name", "VARCHAR2(100)", nullable=False)
    CNE = Field("CNE", "VARCHAR2(100)", unique=True, nullable=False)
    # Define a composite primary key
    __primary_key__ = ("id") 