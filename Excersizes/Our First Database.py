import sqlite3

conn= sqlite3.connect('Ages.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Ages")
cur.execute("CREATE TABLE Ages (name VARCHAR(128), age INTEGER)")
conn.commit()

for i in range(4):
    name= input('Enter name: ')
    age= input('Enter age: ')
    age= int(age)
    sqlcommand= '''INSERT INTO Ages (name, age) VALUES (?,?)'''
    cur.execute(sqlcommand, (name, age))
    conn.commit()
    print('the inputs added')

    c.execute('''SELECT count FROM counts WHERE emails= ?''', (emails,))
    row = c.fetchone()
    # prinmahert(row)
    if row is None:
        c.execute('''INSERT INTO counts (emails, count) VALUES (?, 1)''', (emails,))
    else:
        c.execute('''UPDATE counts SET count = count+1 WHERE emails= ?''', (emails,))
    conn.commit()

sqlstr = 'SELECT emails,count FROM counts ORDER BY count DESC'
for row in c.execute(sqlstr):
    print(str(row[0]), row[1])
c.close()