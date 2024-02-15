from cache import Cache
from database_manager import DatabaseManager


if __name__ == "__main__":
    # database manager using Borg
    db_manager1 = DatabaseManager("sqlite:///:memory:", "public")
    db_manager2 = DatabaseManager("sqlite:///:memory:", "public")

    print(db_manager1 is db_manager2) # False because multiple instances are created with Borg, but the state is shared
    print(db_manager1.engine is db_manager2.engine)
    print(db_manager1.metadata is db_manager2.metadata)
    print(db_manager1.table_schema is db_manager2.table_schema)


    # cache using Borg
    cache1 = Cache(a=1)
    cache2 = Cache(b=2)

    print(cache1 is cache2) # False because multiple instances are created with Borg, but the state is shared
    print(cache1._shared_state is cache2._shared_state)
    print(cache1.b is cache2.b)