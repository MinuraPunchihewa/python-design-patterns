from sqlalchemy.engine import Engine


class SQLConnectionManager:
    engine: Engine

    def __init__(self, engine):
        """ SQL database connection context manager """
        self.engine = engine

    def __enter__(self):
        """ Open connection to a database using engine object """
        self.connection = self.engine.connect()
        return self.connection

    def __exit__(self, type, value, traceback):
        """ Close the open connection to the database """
        self.connection.close()