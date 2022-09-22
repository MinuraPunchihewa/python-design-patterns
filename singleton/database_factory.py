from singleton import SQLConnectionManager
import sqlalchemy as sa
from sqlalchemy.engine import Engine


class DatabaseFactory:
    engine: Engine

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance') or not cls.instance:
          cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, db_connection_str: str, table_schema: str) -> None:
        self.engine = sa.create_engine(db_connection_str)
        self.metadata = sa.MetaData(bind=None)
        self.table_schema = table_schema

    def _get_table_metadata(self, table_name: str):
        table = sa.Table(
            table_name,
            self.metadata,
            autoload=True,
            autoload_with=self.engine,
            schema=self.table_schema
        )
        return table

    def _fetch_all(self, query):
        with SQLConnectionManager(self.engine) as connection:
            # execute query using connection 
            result = connection.execute(query).fetchall()
            return [dict(r) for r in result]

    def _fetch_one(self, query):
        with SQLConnectionManager(self.engine) as connection:
            # execute query using connection 
            result = connection.execute(query).one()
            return dict(result)

    def dispose(self):
        """ Disposes of the connection pool used by the Engine """
        self.engine.dispose()