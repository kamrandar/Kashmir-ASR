import sqlite3
conn = sqlite3.connect('kashmir_TEXT_DB')
c = conn.cursor()

def read_from_db():
    c.execute('SELECT s_no,Text,Male_North,Female_Center FROM Ktext_TABLE where s_no <= 10 AND Male_north ISNULL')

    #data=c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row[0])
    c.close()
    conn.close()

read_from_db()