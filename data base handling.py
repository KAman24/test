import sqlite3

try:
    db = sqlite3.connect('Employee')  # Step2 Connection Object
    mycursor = db.cursor()  # Step3 Creating Cursor
    mycursor.execute('''create table  if not exists emp
    (empID int NOT NULL,
    empName text,
    dept text, 
    sal int, PRIMARY KEY (empID))''')  # Step4
except Exception as E:
    print('Unable to interact with db', E)
else:
    print('Table Created Successfully')
finally:
    db.close()  # Step6

