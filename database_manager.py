import sqlite3 as sql


def listExtension():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension").fetchall()
    con.close()
    return data


def insertContact(email, name):
    con = sql.connect("database/data_source.db")
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO contact_list (email,name) VALUES (?,?)", (email, name))
        con.commit()
    except sql.IntegrityError:
        con.rollback()
        return False
    finally:
        con.close()
    return True
    # integrityError
