import sqlite3

conn = sqlite3.connect('assignment.db')

with conn:
     cur = conn.cursor()
     cur.execute("CREATE TABLE IF NOT EXISTS tbl_animalia( \
         ID INTEGER PRIMARY KEY AUTOINCREMENT, \
         col_breed TEXT, \
         col_color TEXT, \
         col_name TEXT \
         )")
     conn.commit()
conn.close()


conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()

    cur.execute("INSERT INTO tbl_animalia(col_breed, col_color, col_name) VALUES (?,?,?) ", \
                    ('Poodle', 'Black', 'Susie'))
    cur.execute("INSERT INTO tbl_animalia(col_breed, col_color, col_name) VALUES (?,?,?) ", \
                    ('Chow', 'Tan', 'Jack'))
    cur.execute("INSERT INTO tbl_animalia(col_breed, col_color, col_name) VALUES (?,?,?) ", \
                    ('Beagle', 'White', 'Hank'))
        
        
    conn.commit()
conn.close()

conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_breed, col_color, col_name FROM tbl_animalia WHERE col_breed = 'Chow'")
    varAnimalia = cur.fetchall()
    for item in varAnimalia:
        msg = "Breed: ()nColor: ()\nName: ()".format(item[0],item[1],item[2])
        print(msg)


