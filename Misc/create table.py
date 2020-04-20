import sqlite3
conn = sqlite3.connect('kashmir_TEXT_DB')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Ktext_TABLE(s_no INTEGER,Text text, Male_North real, Female_North real, Male_center real, Female_Center real, Male_South real, Female_South real)')
    conn.commit()
    c.close()
    conn.close()
'''def data_entry():
    c.execute("insert into audio values (1,'تہٕ')")'''


create_table()
#data_entry()