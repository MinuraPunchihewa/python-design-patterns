from borg import Borg
import sqlalchemy as sa
from sqlalchemy.engine import Engine
from sql_connection_manager import SQLConnectionManager


class DatabaseManager(Borg):
    engine: Engine

    def __init__(self, db_connection_str: str = None, table_schema: str = None) -> None:
        super().__init__()
        if db_connection_str and table_schema and not hasattr(self, 'engine'):
            self.engine = sa.create_engine(db_connection_str)
            self.metadata = sa.MetaData()
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
        self.engine.dispose()