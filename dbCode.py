# dbCode.py
# Author: Nick Martin
# Helper functions for database connection and queries

from creds import host, user, password, db
import pymysql

def get_conn():
    return pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=db,
        cursorclass=pymysql.cursors.DictCursor
    )

def get_inventory():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Inventory")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results