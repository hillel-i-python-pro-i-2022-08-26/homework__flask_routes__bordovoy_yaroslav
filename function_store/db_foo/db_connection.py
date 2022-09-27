import sqlite3

from function_store.path_settings import DB_PATH


class DBConnection:

    # Initiating a database connection
    def __int__(self):
        self._connection: sqlite3.Connection

    # Establishing a connection to the database
    def __enter__(self):
        self._connection = sqlite3.connect(DB_PATH)
        self._connection.row_factory = sqlite3.Row
        return self._connection

    # Closing the database connection
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()
