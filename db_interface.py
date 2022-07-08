import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="usuario", password="senha")

cursor = mydb.cursor()
cursor.execute("USE bank_db")


class dB_Cursor:
    def __init__(self):
        self.cursor = cursor

    def create_table(self, table_name: str):

        self.cursor.execute(
            f"CREATE TABLE {table_name}(id int PRIMARY KEY AUTO_INCREMENT)"
        )

    def create_data(self, table_name: str):

        self.cursor.execute(f"INSERT INTO {table_name} VALUES()")

    def drop_table(self, table_name: str):

        self.cursor.execute(f"DROP TABLE {table_name}")

    def init_database_with_data(self):

        self.cursor.execute(
            "CREATE TABLE Clients (CPF varchar(11), \
                        client_id int NOT NULL AUTO_INCREMENT,\
                        PRIMARY KEY (client_id), \
                        UNIQUE KEY CPF (CPF)) ENGINE=InnoDB \
                        AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 \
                        COLLATE=utf8mb4_unicode_ci;"
        )

        for i in range(1, 10):
            self.cursor.execute(
                f"INSERT INTO Clients (CPF) VALUES (0102030405{str(i)})"
            )

        self.cursor.execute(
            "CREATE TABLE Transactions (value int NOT NULL, \
                        date datetime NOT NULL, \
                        transaction_id int NOT NULL AUTO_INCREMENT, \
                        client_id int NOT NULL, \
                        PRIMARY KEY (transaction_id), \
                        UNIQUE KEY transaction_id (transaction_id), \
                        KEY client_id (client_id), \
                        FOREIGN KEY(client_id) \
                        REFERENCES Clients (client_id)) ENGINE=InnoDB AUTO_INCREMENT=1 \
                        DEFAULT CHARSET=utf8mb4;"
        )

        for i in range(1, 10):
            self.cursor.execute(
                f"INSERT INTO Transactions (value,date,client_id) VALUES (9.99, '2000-10-10 22:22:22', {str(i)})"
            )

        print("Database initiated with data")

    def clean_database(self):

        self.cursor.execute("USE bank_db")
        self.cursor.execute("DROP TABLES Transactions")
        self.cursor.execute("DROP TABLES Clients")

    def create_new_client(self, CPF):

        cursor.execute(f"INSERT INTO Clients (CPF) VALUES('{CPF}')")
        print("\n New client registered.")

    def client_exists(self, CPF):
        """
        Check there is a client registered on db with given
        value of CPF
        """
        cursor.execute(f"SELECT * from Clients WHERE CPF={CPF};")
        return len(cursor.fetchall()) > 0

    def insert_transaction_in_db(self, value: int, date: str, client_id: int):
        """"""
        cursor.execute(
            f"INSERT INTO Transactions (value, date, client_id) VALUES({value},'{date}',{client_id})"
        )

    def search_id_from_CPF(self, CPF):
        """ """
        cursor.execute(f"SELECT client_id FROM Clients WHERE CPF={CPF}")
        return cursor.fetchall()[0][0]

    def obtain_extract(self, id: int) -> list:

        cursor.execute(f"SELECT value,date FROM Transactions WHERE client_id={id}")

        return cursor.fetchall()

    def calculates_balance(self, id: int) -> int:

        cursor.execute(f"SELECT SUM(value) FROM Transactions WHERE client_id={id}")
        balance = cursor.fetchall()[0][0]
        if balance == None:
            return 0
        else:
            return int(balance)

    def commit(self):
        """ """
        mydb.commit()
