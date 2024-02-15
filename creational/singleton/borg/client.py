from database_manager import DatabaseManager


if __name__ == "__main__":
    db_manager1 = DatabaseManager("sqlite:///:memory:", "public")
    db_manager2 = DatabaseManager("sqlite:///:memory:", "public")

    print(db_manager1 is db_manager2) # False because multiple instances are created with Borg, but the state is shared
    print(db_manager1.engine is db_manager2.engine)
    print(db_manager1.metadata is db_manager2.metadata)
    print(db_manager1.table_schema is db_manager2.table_schema)