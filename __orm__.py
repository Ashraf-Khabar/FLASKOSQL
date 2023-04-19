from __db__ import Connect

class ORM:
        
    def __init__(self, db_connection):
        self.db_connection = db_connection
        
    def save(self, obj):
        
        cursor = self.db_connection.cursor()

        # Extract the data from the object and construct an INSERT query
        # Example assumes the object has attributes corresponding to the column_names
        query = "INSERT INTO {} ({}) VALUES ({})".format(table_name, ", ".join(column_names), ":" + ", :".join(column_names))
        data = {column_name: getattr(obj, column_name) for column_name in column_names}

        # Execute the INSERT query with the data
        cursor.execute(query, data)
        self.db_connection.commit()

        cursor.close()
        
    def update(self, obj):
        # Implement logic to update the object in the database
        pass

    def delete(self, obj):
        # Implement logic to delete the object from the database
        pass

    def get(self, obj_id):
        # Implement logic to retrieve an object from the database by ID
        pass

    def get_all(self):
        # Implement logic to retrieve all objects from the database
        pass

    # Other common ORM methods such as filtering, querying, and transactions
