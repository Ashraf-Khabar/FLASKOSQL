# FlaskoSQL

[![PyPI version](https://img.shields.io/badge/flaskos-2.1.4-green.svg)](https://pypi.org/project/flaskosql/)
[![GitHub code source](https://img.shields.io/badge/Code-Source-orange.svg)](https://github.com/Ashraf-Khabar/FLASKOSQL)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<p align="center">
    <img src="./img/flaskos.png" height = "130">
</p>

**NEW :** *Support MySQL DBMS.*

Description
-----------

The Package Name is a Python package that provides an Object-Relational Mapping (ORM) solution for relational databases (Oracle and MySQL), specifically designed for use in Flask APIs. It simplifies the interaction with an Oracle and MySQL database by providing an intuitive interface for querying, inserting, updating, and deleting data.

Features
--------

-   Easy integration with Flask: Seamlessly integrate the ORM into your Flask application for database operations.
-   Simplified querying: Perform complex queries using an expressive API, allowing you to focus on your application logic rather than database intricacies.
-   Model-based approach: Define your database schema using Python classes, reducing the need for manual SQL queries and keeping your code organized.
-   Transaction support: Manage database transactions easily, ensuring data consistency and integrity.

Installation
------------

You can install the Package Name package using pip:

`pip install flaskosql`

Usage
-----

1.  Import the necessary classes and functions from the package:

`from flaskosql.db import Connect`<br>
`from flaskosql.field import Field`<br>
`from flaskosql.model import Model`<br>

1.  Create a model class that represents a table in your Oracle database. Define the table schema using the `Field` class:

```py
from flaskosql.model import Model
from flaskosql.field import Field

class Roles(Model):
    ID = Field("id", "NUMBER", primary_key=True)
    NAME = Field("name", "VARCHAR2(100)", nullable=False)
```
We can use also other table to create a realtion one to many : 
```py
from flaskosql.model import Model
from flaskosql.field import Field

class Users(Model):
    ID = Field("id", "NUMBER", primary_key=True)
    NAME = Field("name", "VARCHAR2(100)", nullable=False)
    ROLE_ID = Field("role_id", "NUMBER", foreign_key=("roles", "id"))
```
We should always put the names of fileds in upercase `(it's obligatory)`
1. Create a database connection : 

```py
from flaskosql.db import Connect

connection = Connect('orm', 'ormpw', 'localhost', '1521', 'orcl').get_connection()
```

2. Initialize the database connection:

```py
from flaskosql.db import Connect
from flaskosql.model import Model

# Setup the connection : 
connection = Connect('orm', 'ormpw', 'localhost', '1521', 'orcl').get_connection()
# CReate the connection for the model  :
Model.set_connection(connection=connection)
```
1.  Perform database operations using the model:

# Creation of tables (migrations) : 
```py
def migrate():
    Roles.create_table()
    Users.create_table()

migrate()
```
We must create Roles table before Users because we already defined a `foreing_key` constraint . 

# Filter users by a condition
```py
role = Roles.get(id=1, name="ASHRAF")
```
and we can display the value :
```py
if role:
    print(f"The id :{role.ID}")
    print(f"The name : {role.NAME})
```

# Insert a new user
```py
# Creating a user:
role = Roles(id=1, name="ASHRAF")
role.save()
```

# Update a user's email
```py
role.name = "SAMI"
role.update()
```

# Delete a user
```py
role.delete()
```

For more details on using the Package Name package, please refer to the [documentation](https://achrafkhabar.com/flaskoSQL).

License
-------

This package is licensed under the MIT License. See the [LICENSE]() file for more information.

* * * * *

Feel free to modify this template according to your needs. Remember to replace "Package Name" with the actual name of your package and update the relevant sections with the appropriate details about your ORM and its usage with Flask and Oracle databases.

Make sure to also include the actual installation instructions, usage examples, and any other relevant information in your README file to provide a comprehensive guide for users of your package.
