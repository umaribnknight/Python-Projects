import sqlite3

         
conn = sqlite3.connect('test.db')

with conn:
     cur = conn.cursor()
   
  cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
         ID INTEGER PRIMARY KEY AUTOINCREMENT, \
         co1_fname TEXT, \
         co1_lname TEXT, \
         co1_email TEXT \
         )")
     conn.commit()
conn.close()



