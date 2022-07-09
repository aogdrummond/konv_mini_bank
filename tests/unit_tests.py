import sys
from pathlib import Path

sys.path.append(str(Path(sys.path[0]).parent))

from db_interface import mydb, dB_Cursor

cursor = dB_Cursor()


def test_connection_with_db():

    assert mydb.is_connected()


def test_create_table():

    cursor.execute("USE bank_db")
    cursor.execute("SHOW TABLES")
    n_initial_tables = len(cursor.fetchall())

    cursor.create_table(cursor, table_name="tab")
    cursor.execute("SHOW TABLES")
    n_final_tables = len(cursor.fetchall())
    cursor.drop_table(cursor, table_name="tab")

    assert n_initial_tables < n_final_tables


def test_create_data():

    cursor.create_table(cursor, table_name="tab")
    cursor.create_data(cursor, table_name="tab")
    cursor.execute("SELECT * FROM tab")
    n_data = len(cursor.fetchall())

    cursor.drop_table(cursor, table_name="tab")

    assert n_data > 0


if __name__ == "__main__":

    test_connection_with_db()
    test_create_table()
    test_create_data()

    print("All passed")


# Testar depositar valor negativo
# Testar sacar valor negativo
# Testar sacar mais que o saldo
# Testar depositar valor char, bool, etc...
