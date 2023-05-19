import cx_Oracle

class Connect:
    _connection = None

    def __init__(self, db_username, db_password, db_host, db_port, db_service_name):
        if not Connect._connection:
            try:
                dsn = cx_Oracle.makedsn(db_host, db_port, service_name=db_service_name)
                Connect._connection = cx_Oracle.connect(db_username, db_password, dsn=dsn)
                print("Connected to the database.")
            except cx_Oracle.Error as e:
                print(f"Error connecting to Oracle database: {e}")

    @staticmethod
    def get_connection():
        return Connect._connection
