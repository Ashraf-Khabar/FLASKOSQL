from __field__ import Field
from __model__ import Model

# Define the main table:
class Users(Model):
    ID1 = Field("id1", "NUMBER")
    ID2 = Field("id2", "NUMBER")
    NAME = Field("name", "VARCHAR2(100)", nullable=False)
    LAST_NAME = Field("last_name", "VARCHAR2(100)", nullable=False)
    CNE = Field("CNE", "VARCHAR2(100)", unique=True, nullable=False)
    __primary_key__ = ("id1", "id2")