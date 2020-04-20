import sqlite3
import time
import datetime
import random
conn = sqlite3.connect('tutorial')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS employee(e_id Real,date Text ,e_name Text,e_salary Real)')

def data_entry():
    unix = time.time()
    date=str(datetime.datetime.fromtimestamp(unix).strftime("%y-%m-%d %H:%M:%S"))
    keyword = 'kamran'
    val = random.randrange(0,10)
    c.execute("INSERT INTO employee(e_id, date , e_name, e_salary) VALUES (?,?,?,?)",
              (unix,date,keyword,val))
    conn.commit()
    c.close()
    conn.close()


create_table()
data_entry()