import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur  = conn.cursor()
    cur.execute("CREATE TABLE if not exists book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur  = conn.cursor()
    cur.execute("INSERT into book values(NULL, ?, ?, ?, ?)",(title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur  = conn.cursor()
    cur.execute("SELECT * from book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur  = conn.cursor()
    cur.execute("SELECT * from book where title = ? or author= ? or year= ? or isbn= ?",(title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur  = conn.cursor()
    cur.execute("delete from book where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur  = conn.cursor()
    cur.execute("update book set title=?, author=?, year=?, isbn=? where id =?",(title, author, year, isbn,id))
    conn.commit()
    conn.close()


connect()
#insert("Wings of Fire", "Kalam Sir", 2002,3242398)
#print(search("The Secret"))
#delete(4)
#update(1,"My Life Journey","APJ Sir", 2003,23494387098)

print(view())
