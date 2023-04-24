import cx_Oracle

class Connect:
    # __init__ function is the constructor of the class Connect .
    # in this constructor we initilize the fields (attributs) in order to use them in the connection 
    
    def __init__(self, db_username, db_password, db_host, db_port, db_service_name):
        self.db_username = db_username
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_service_name = db_service_name
       
    # This method id for establishing the connection with the database based on the parameters provided on the (__init__) function 
    def connect(self):
        try:
            dsn = cx_Oracle.makedsn(self.db_host, self.db_port, service_name=self.db_service_name)
            db_connection = cx_Oracle.connect(self.db_username, self.db_password, dsn)
            return db_connection
        except cx_Oracle.Error as e:
            print(f"Error connecting to Oracle database: {e}")
            return None
    

connexion = Connect('orm', 'ormpw', 'localhost', 1521, 'orcl')
if connexion.connect() : 
    print("Connected")
else :
    print("Not connected")
    
    
