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

def add_user(first_name, last_name, genre):
    conn = get_conn()
    cur = conn.cursor()

    query = "INSERT INTO Users (first_name, last_name, favorite_genre) VALUES (%s, %s, %s)"
    cur.execute(query, (first_name, last_name, genre))

    conn.commit()
    cur.close()
    conn.close()


def get_all_users():
    conn = get_conn()
    cur = conn.cursor()

    query = "SELECT first_name, last_name, favorite_genre FROM Users"
    cur.execute(query)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results


def delete_user(first_name, last_name):
    conn = get_conn()
    cur = conn.cursor()

    query = "DELETE FROM Users WHERE first_name=%s AND last_name=%s"
    cur.execute(query, (first_name, last_name))

    conn.commit()
    cur.close()
    conn.close()

def update_user(old_first_name, old_last_name, new_first_name, new_last_name, new_genre):
    conn = get_conn()
    cur = conn.cursor()

    query = """
    UPDATE Users
    SET first_name = %s, last_name = %s, favorite_genre = %s
    WHERE first_name = %s AND last_name = %s
    """
    cur.execute(query, (new_first_name, new_last_name, new_genre, old_first_name, old_last_name))

    conn.commit()
    cur.close()
    conn.close()

def search_users_by_genre(genre):
    conn = get_conn()
    cur = conn.cursor()

    query = "SELECT first_name, last_name, favorite_genre FROM Users WHERE favorite_genre = %s"
    cur.execute(query, (genre,))
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results