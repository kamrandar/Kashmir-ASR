import sqlite3
conn = sqlite3.connect('kashmir_TEXT_DB')
c = conn.cursor()

def slect_table():
    c.execute("Select * from Ktext_TABLE")
    print(c.fetchall())
    #c.execute("DELETE FROM Ktext_TABLE WHERE TEXT_DATA !=''")


    conn.commit()
    conn.close()

slect_table()