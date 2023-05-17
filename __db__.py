import cx_Oracle
import os

db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_service_name = os.environ.get('DB_SERVICE_NAME')

class Connect:
    def __init__(self, db_username=db_username, db_password=db_password, db_host=db_host, db_port=db_port, db_service_name=db_service_name):
        self.db_username = db_username
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_service_name = db_service_name

    def connect(self):
        try:
            dsn = cx_Oracle.makedsn(self.db_host, self.db_port, service_name=self.db_service_name)
            db_connection = cx_Oracle.connect(self.db_username, self.db_password, dsn)
            print("Connected")
            return db_connection
        except cx_Oracle.Error as e:
            print(f"Error connecting to Oracle database: {e}")
            return None

    
    
