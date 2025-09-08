import sqlite3
import re
from typing import List, Tuple

# regex for validating table names (to avoid SQL injection)
class Database:

    def __init__(self, db_path: str, table_name):
        self.db_path = db_path
        self.table_name = table_name
        self._VALID_TABLE = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$')
        self.new_id = None        

    def _validate_table_name(self, table_name) -> None:

        if not self._VALID_TABLE.match(table_name):
            raise ValueError(f"Invalid table name: {table_name!r}")

    def create_database(self) -> None:
        """
        Create the SQLite database file (if it doesn't exist) 
        and create the table if it's missing.
        """
        self._validate_table_name(self.table_name)
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                company TEXT,
                link TEXT
            );
            """)
            conn.commit()

    def clean_database(self) -> None:
        """
        Delete all rows from a table (but keep the table itself).
        """
        self._validate_table_name(self.table_name)
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(f"DELETE FROM {self.table_name};")
            conn.commit()

    def reset_database(self) -> None:
        """
        Drop all user tables in the database (full reset).
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [r[0] for r in cur.fetchall()]

        for t in tables:
            if t == "sqlite_sequence":   # skip SQLite internal table
                continue
            conn.execute(f"DROP TABLE IF EXISTS {t};")
        conn.commit()


    def add_to_database(self, title, company: str, link: str) -> int:
        """
        Insert one row into the table and return the row ID.
        """
        self._validate_table_name(self.table_name)
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                f"INSERT INTO {self.table_name} (title, company, link) VALUES (?, ?, ?);",
                (title, company, link)
            )
            conn.commit()
            self.new_id = cur.lastrowid

    def get_all_jobs(self) -> List[Tuple]:
        """
        Fetch all rows from the jobs table.
        Returns a list of tuples (id, title, company, link).
        """
        self._validate_table_name(self.table_name)
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT id, title, company, link FROM {self.table_name};")
            return cur.fetchall()


def main():
    pass
if __name__ == "__main__":
    main()
