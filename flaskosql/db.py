import cx_Oracle
import mysql.connector

class Connect:
    _connection = None

    @classmethod
    def get_oracle_connection(cls, db_username, db_password, db_host, db_port, db_service_name):
        if not cls._connection:
            try:
                dsn = cx_Oracle.makedsn(db_host, db_port, service_name=db_service_name)
                cls._connection = cx_Oracle.connect(db_username, db_password, dsn=dsn)
                print("Connected to the Oracle database.")
            except cx_Oracle.Error as e:
                print(f"Error connecting to Oracle database: {e}")
    
    @classmethod
    def get_mysql_connection(cls, db_username, db_password, db_host, db_port, db_name):
        if not cls._connection:
            try:
                db_config = {
                    'host': db_host,
                    'port': db_port,
                    'user': db_username,
                    'password': db_password,
                    'database': db_name
                }
                cls._connection = mysql.connector.connect(**db_config)
                print("Connected to the MySQL database.")
                return Connect._connection
            except mysql.connector.Error as e:
                print(f"Error connecting to MySQL database: {e}")
    
    @staticmethod
    def get_connection():
        return Connect._connection
