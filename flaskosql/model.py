import cx_Oracle
from flaskosql.field import Field
import mysql.connector
from field import MySQLField

class Model:
    # Variable for getting the connection :
    _connection = None
    
    # Constructor : it takes two arguments (self ("this" in other languages and *kwargs wich can be translated to string of values))
    def __init__(self, **kwargs):
        # Initialize the object with provided attributes
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    # Method tha d¡set the connection : 
    @classmethod
    def set_connection(cls, connection):
        cls._connection = connection
    
    # Method to return that create a table with the same name as the class :
    @classmethod
    def create_table(cls, fresh=False):
        # Create the table with the same name as the class
        # This method is a static method (it could be called from the class without instance (read OOP concepts and the documentation))
        table_name = cls.__name__
        # The connect method takes no parameters, it loads the data from the .env file, but it can takes parametrs two (read the documentation)
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                if fresh:
                    # Drop the existing table if fresh is True
                    drop_query = f"DROP TABLE {table_name}"
                    cursor.execute(drop_query)
                    print(f"Table '{table_name}' dropped.")
                columns = []
                for attr_name, attr_value in cls.__dict__.items():
                    if isinstance(attr_value, (Field, MySQLField)):
                        columns.append(attr_value.get_column_definition())

                create_query = "CREATE TABLE {} ({})".format(table_name, ", ".join(columns))
                cursor.execute(create_query)
                connection.commit()
                print("Table '{}' created successfully!".format(table_name))
            except (cx_Oracle.Error, mysql.connector.Error) as e:
                print(f"Error creating table: {e}")
            finally:
                if cursor:
                    cursor.close()
                    # connection.close()
        else:
            print("Failed to connect to the database.")

    # Method that insert into the table : 
    def save(self):
        # Save the object to the database
        connection = self.__class__._connection
        if connection:
            try:
                cursor = connection.cursor()
                columns = []
                values = []
                placeholders = []
                for key, value in self.__dict__.items():
                    columns.append(key)
                    values.append(value)
                    placeholders.append(':{}'.format(key))

                table_name = self.__class__.__name__  # Get the table name from the class
                insert_query = "INSERT INTO {} ({}) VALUES ({})".format(
                    table_name, ", ".join(columns), ", ".join(placeholders))
                cursor.execute(insert_query, values)
                connection.commit()
                print("Object saved successfully!")
            except cx_Oracle.Error as e:
                print(f"Error saving object to database: {e}")
            finally:
                if cursor:
                    cursor.close()
                    # connection.close()
        else:
            print("Failed to connect to the database.")

    # Mthod that update a table :
    def update(self):
        # Update the object in the database
        connection = self.__class__._connection
        if connection:
            try:
                cursor = connection.cursor()
                set_values = []
                for key, value in self.__dict__.items():
                    set_values.append("{} = :{}".format(key, key))

                table_name = self.__class__.__name__  # Get the table name from the class
                update_query = "UPDATE {} SET {} WHERE id = :id".format(
                    table_name, ", ".join(set_values))
                cursor.execute(update_query, self.__dict__)
                connection.commit()
                print("Object updated successfully!")
            except cx_Oracle.Error as e:
                print(f"Error updating object in the database: {e}")
            finally:
                if cursor:
                    cursor.close()
                    # connection.close()
        else:
            print("Failed to connect to the database.")
    
    # Method that delete a a row from table : 
    def delete(self):
        # Delete the object from the database
        connection = self.__class__._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = self.__class__.__name__  # Get the table name from the class
                delete_query = "DELETE FROM {} WHERE id = :id".format(table_name)
                cursor.execute(delete_query, self.__dict__)
                connection.commit()
                print("Object deleted successfully!")
            except cx_Oracle.Error as e:
                print(f"Error deleting object from the database: {e}")
            finally:
                if cursor:
                    cursor.close()
                    # connection.close()
        else:
            print("Failed to connect to the database.")

    # Method that delete filter a table based on one condition or more : 
    @classmethod
    def get(cls, **conditions):
        # Retrieve an object from the database based on the specified conditions
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = cls.__name__  # Get the class name
                conditions_str = " AND ".join(f"{key} = :{key}" for key in conditions)
                select_query = f"SELECT * FROM {table_name} WHERE {conditions_str}"
                cursor.execute(select_query, conditions)
                result = cursor.fetchone()
                if result:
                    columns = [column[0] for column in cursor.description]
                    obj_data = dict(zip(columns, result))

                    # Create an instance of the class with dynamic attribute assignment
                    model_instance = cls(**obj_data)
                    return model_instance
                else:
                    print("Object not found in the database.")
                    return None
            except cx_Oracle.Error as e:
                print(f"Error retrieving object from the database: {e}")
                return None
            finally:
                if cursor:
                    cursor.close()
                    # connection.close()
        else:
            print("Failed to connect to the database.")
            return None

    # Method that get a list of elements from a table : 
    @classmethod
    def getAll(cls, **conditions):
        # Retrieve objects from the database based on the specified conditions
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = cls.__name__  # Get the class name
                conditions_str = " AND ".join(f"{key} = :{key}" for key in conditions)
                select_query = f"SELECT * FROM {table_name} WHERE {conditions_str}"
                cursor.execute(select_query, conditions)
                results = cursor.fetchall()
                if results:
                    columns = [column[0] for column in cursor.description]
                    objects = []
                    for row in results:
                        obj_data = dict(zip(columns, row))
                        model_instance = cls(**obj_data)
                        objects.append(model_instance)
                    return objects
                else:
                    print("No objects found in the database.")
                    return []
            except cx_Oracle.Error as e:
                print(f"Error retrieving objects from the database: {e}")
                return []
            finally:
                if cursor:
                    cursor.close()
        else:
            print("Failed to connect to the database.")
            return []
    
    @classmethod
    def fetchAll(cls):
        # Retrieve all objects from the database
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = cls.__name__  # Get the class name
                select_query = f"SELECT * FROM {table_name}"
                cursor.execute(select_query)
                results = cursor.fetchall()

                objects = []
                for result in results:
                    columns = [column[0] for column in cursor.description]
                    obj_data = dict(zip(columns, result))

                    # Create an instance of the class with dynamic attribute assignment
                    model_instance = cls(**obj_data)
                    objects.append(model_instance)

                return objects
            except cx_Oracle.Error as e:
                print(f"Error retrieving objects from the database: {e}")
                return []
            finally:
                if cursor:
                    cursor.close()
                    # connection.close()
        else:
            print("Failed to connect to the database.")
            return []

    @classmethod
    def count(cls, **conditions):
        # Count the number of rows in the database based on the specified conditions
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = cls.__name__  # Get the class name
                conditions_str = " AND ".join(f"{key} = :{key}" for key in conditions)
                select_query = f"SELECT COUNT(*) FROM {table_name} WHERE {conditions_str}"
                cursor.execute(select_query, conditions)
                result = cursor.fetchone()
                if result:
                    return result[0]  # Return the count
                else:
                    print("No rows found in the database.")
                    return 0
            except cx_Oracle.Error as e:
                print(f"Error counting rows in the database: {e}")
                return 0
            finally:
                if cursor:
                    cursor.close()
        else:
            print("Failed to connect to the database.")
            return 0
 
    @classmethod
    def countAll(cls):
        # Count the number of rows in the database based on the specified conditions
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = cls.__name__  # Get the class name
                select_query = f"SELECT COUNT(*) FROM {table_name}"
                cursor.execute(select_query)
                result = cursor.fetchone()
                if result:
                    return result[0]  # Return the count
                else:
                    print("No rows found in the database.")
                    return 0
            except cx_Oracle.Error as e:
                print(f"Error counting rows in the database: {e}")
                return 0
            finally:
                if cursor:
                    cursor.close()
        else:
            print("Failed to connect to the database.")
            return 0
    
    @classmethod
    def sum(cls, column, **conditions):
        # Calculate the sum of a column in the database based on the specified conditions
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = cls.__name__  # Get the class name
                conditions_str = " AND ".join(f"{key} = :{key}" for key in conditions)
                select_query = f"SELECT SUM({column}) FROM {table_name} WHERE {conditions_str}"
                cursor.execute(select_query, conditions)
                result = cursor.fetchone()
                if result:
                    return result[0]  # Return the sum
                else:
                    print("No rows found in the database.")
                    return 0
            except cx_Oracle.Error as e:
                print(f"Error calculating sum in the database: {e}")
                return 0
            finally:
                if cursor:
                    cursor.close()
        else:
            print("Failed to connect to the database.")
            return 0

    @classmethod
    def average(cls, column, **conditions):
        # Calculate the average of a column in the database based on the specified conditions
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = cls.__name__  # Get the class name
                conditions_str = " AND ".join(f"{key} = :{key}" for key in conditions)
                select_query = f"SELECT AVG({column}) FROM {table_name} WHERE {conditions_str}"
                cursor.execute(select_query, conditions)
                result = cursor.fetchone()
                if result:
                    return result[0]  # Return the average
                else:
                    print("No rows found in the database.")
                    return 0
            except cx_Oracle.Error as e:
                print(f"Error calculating average in the database: {e}")
                return 0
            finally:
                if cursor:
                    cursor.close()
        else:
            print("Failed to connect to the database.")
            return 0

    @classmethod
    def minimum(cls, column, **conditions):
        # Find the minimum value of a column in the database based on the specified conditions
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = cls.__name__  # Get the class name
                conditions_str = " AND ".join(f"{key} = :{key}" for key in conditions)
                select_query = f"SELECT MIN({column}) FROM {table_name} WHERE {conditions_str}"
                cursor.execute(select_query, conditions)
                result = cursor.fetchone()
                if result:
                    return result[0]  # Return the minimum value
                else:
                    print("No rows found in the database.")
                    return 0
            except cx_Oracle.Error as e:
                print(f"Error finding minimum value in the database: {e}")
                return 0
            finally:
                if cursor:
                    cursor.close()
        else:
            print("Failed to connect to the database.")
            return 0

    @classmethod
    def maximum(cls, column, **conditions):
        # Find the maximum value of a column in the database based on the specified conditions
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = cls.__name__  # Get the class name
                conditions_str = " AND ".join(f"{key} = :{key}" for key in conditions)
                select_query = f"SELECT MAX({column}) FROM {table_name} WHERE {conditions_str}"
                cursor.execute(select_query, conditions)
                result = cursor.fetchone()
                if result:
                    return result[0]  # Return the maximum value
                else:
                    print("No rows found in the database.")
                    return 0
            except cx_Oracle.Error as e:
                print(f"Error finding maximum value in the database: {e}")
                return 0
            finally:
                if cursor:
                    cursor.close()
        else:
            print("Failed to connect to the database.")
            return 0

    @classmethod
    def countDistinct(cls, column, **conditions):
        # Count the number of distinct values in a column based on the specified conditions
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = cls.__name__  # Get the class name
                conditions_str = " AND ".join(f"{key} = :{key}" for key in conditions)
                select_query = f"SELECT COUNT(DISTINCT {column}) FROM {table_name} WHERE {conditions_str}"
                cursor.execute(select_query, conditions)
                result = cursor.fetchone()
                if result:
                    return result[0]  # Return the count of distinct values
                else:
                    print("No rows found in the database.")
                    return 0
            except cx_Oracle.Error as e:
                print(f"Error counting distinct values in the database: {e}")
                return 0
            finally:
                if cursor:
                    cursor.close()
        else:
            print("Failed to connect to the database.")
            return 0

    @classmethod
    def groupBy(cls, column, **conditions):
        # Perform a GROUP BY query on a column based on the specified conditions
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = cls.__name__  # Get the class name
                conditions_str = " AND ".join(f"{key} = :{key}" for key in conditions)
                select_query = f"SELECT {column}, COUNT(*) FROM {table_name} WHERE {conditions_str} GROUP BY {column}"
                cursor.execute(select_query, conditions)
                results = cursor.fetchall()
                if results:
                    return results  # Return the grouped results
                else:
                    print("No rows found in the database.")
                    return []
            except cx_Oracle.Error as e:
                print(f"Error performing GROUP BY query in the database: {e}")
                return []
            finally:
                if cursor:
                    cursor.close()
        else:
            print("Failed to connect to the database.")
            return []

    @classmethod
    def having(cls, condition, **conditions):
        # Perform a HAVING query based on the specified condition and conditions
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = cls.__name__  # Get the class name
                conditions_str = " AND ".join(f"{key} = :{key}" for key in conditions)
                select_query = f"SELECT * FROM {table_name} WHERE {conditions_str} HAVING {condition}"
                cursor.execute(select_query, conditions)
                results = cursor.fetchall()
                if results:
                    columns = [column[0] for column in cursor.description]
                    objects = []
                    for row in results:
                        obj_data = dict(zip(columns, row))
                        model_instance = cls(**obj_data)
                        objects.append(model_instance)
                    return objects
                else:
                    print("No rows found in the database.")
                    return []
            except cx_Oracle.Error as e:
                print(f"Error performing HAVING query in the database: {e}")
                return []
            finally:
                if cursor:
                    cursor.close()
        else:
            print("Failed to connect to the database.")
            return []

        
        
    