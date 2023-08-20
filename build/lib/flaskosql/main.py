from flaskosql.db import Connect
from flaskos.model import Model
from flaskosql.field import Field


# Setup the connection : 
connection = Connect('orm', 'ormpw', 'localhost', '1521', 'orcl').get_connection()
# CReate the connection for the model  :
Model.set_connection(connection=connection)

class Roles(Model):
    ID = Field("id", "NUMBER", primary_key=True)
    NAME = Field("name", "VARCHAR2(100)", nullable=False)
    AGE = Field("age", "VARCHAR2(100)", nullable=False)
    
    

role1 = Roles(id=1, name="ASHRAF", age = 22)
role2 = Roles(id=2, name="SAMI", age = 22)
role3 = Roles(id=3, name="KARIM", age = 22)
role4 = Roles(id=4, name="HASSAN", age = 22)

role1.save()
role2.save()
role3.save()
role4.save()




role = Roles.get(id = 3)
if role :
    print(f"The name : {role.NAME}")

roles = Roles.getAll()
for role in roles:
    print(role.NAME, role.AGE)
    
roles = Roles.fetchAll()
for role in roles:
    print(role.NAME, role.AGE)
    
count = Roles.count()
print(count)

count = Roles.countAll()
print(count)

count = Roles.countDistinct("age")
print(count)

results = Roles.groupBy("AGE")
for result in results:
    print(result[0], result[1])

roles = Roles.having("COUNT(*) > 2")
for role in roles:
    print(role.NAME, role.AGE)


    
# roles = Roles.countAll()