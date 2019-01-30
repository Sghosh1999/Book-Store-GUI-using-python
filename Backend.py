import sqlite3

def connect():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text,author text,year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,ISBN):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,ISBN))
    conn.commit()
    conn.close()

def view():
     conn = sqlite3.connect("books.db")
     cur = conn.cursor()
     cur.execute("SELECT * FROM book")
     rows = cur.fetchall()
     conn.close()
     return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book where id = ?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,ISBN):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author =?, year = ?,ISBN = ? WHERE id=?",(title,author,year,ISBN,id))
    conn.commit()
    conn.close()

def search(title,author,year,ISBN):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title =? OR author =? OR year = ? OR ISBN = ?",(title,author,year,ISBN))
    rows = cur.fetchall()
    conn.commit()
    return rows
    conn.close()



connect()

print(view())
