from function_store.db_foo.db_connection import DBConnection


def create_table():
    with DBConnection() as connection:
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS phones (
                    phoneID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    contactname VARCHAR NOT NULL,
                    phonevalue INTEGER NOT NULL
                )
            """
            )
