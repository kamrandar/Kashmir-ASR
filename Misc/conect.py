import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial')
c = conn.cursor()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime("%y-%m-%d %H:%M:%S"))
    e_name = 'kamran'
    e_salary = random.randrange(0,10)

    c.execute("INSERT INTO employee (e_id, date , e_name, e_salary) VALUES(?,?,?,?)",
              (unix,date,e_name,e_salary))

    conn.commit()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
c.close()
conn.close()
