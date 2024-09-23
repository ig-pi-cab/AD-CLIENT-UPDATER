import sqlite3

class ClientManager:
    def __init__(self, db_name='clients.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS clients (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    user TEXT NOT NULL,
                                    ip TEXT NOT NULL,
                                    target_dir TEXT NOT NULL,
                                    adempiere_dir TEXT NOT NULL)''')

    def add_client(self, name, user, ip, target_dir, adempiere_dir):
        with self.conn:
            self.conn.execute('''INSERT INTO clients (name, user, ip, target_dir, adempiere_dir)
                                 VALUES (?, ?, ?, ?, ?)''', (name, user, ip, target_dir, adempiere_dir))

    def get_clients(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM clients')
        return cursor.fetchall()

    def update_client(self, client_id, name, user, ip, target_dir, adempiere_dir):
        with self.conn:
            self.conn.execute('''UPDATE clients SET name = ?, user = ?, ip = ?, target_dir = ?, adempiere_dir = ?
                                 WHERE id = ?''', (name, user, ip, target_dir, adempiere_dir, client_id))

    def delete_client(self, client_id):
        with self.conn:
            self.conn.execute('DELETE FROM clients WHERE id = ?', (client_id,))
