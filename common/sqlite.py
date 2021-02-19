#!/usr/bin/python
import sqlite3
import time


class sqlitedb:
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()

    def execute(self, lang):
        self.cursor.execute(lang)

    def query(self, lang):
        return self.cursor.execute(lang)

    def __next__(self):
        item =  self.cursor.fetchone()
        if item is None:
            raise StopIteration
        else:
            return item

    def flush(self):
        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = sqlitedb('atom.db')

    '''
    db.execute('DROP TABLE IF EXISTS cmd')
    db.flush()
    '''

    db.execute('''CREATE TABLE IF NOT EXISTS cmd(
        `id`     INTEGER PRIMARY KEY   AUTOINCREMENT,
        `val`    TEXT              NOT NULL
    ) ''')

    '''
    for _ in range(10):
        db.execute('INSERT INTO cmd(val,type) VALUES("abcd","list")')
        db.flush()
        time.sleep(1)
    '''

    rows = db.query('''select id,val,type from cmd''')
    for row in rows:
        print(row)

