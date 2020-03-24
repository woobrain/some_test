#!/bin/env python
import pyodbc
# print(pyodbc.drivers())
#
cnxn = pyodbc.connect('DRIVER={IBM INFORMIX ODBC DRIVER (64-bit)};SERVER=infor99;DATABASE=db0;UID=informix;PWD=980120',unicode_results=True)
cursor = cnxn.cursor()
# params = [ (1,'A'), (2,'B') ]
# for p in params:
# rows = cursor.execute("insert into test(id,name) values ('%d', '%s')"%(1,'A'))
rows = cursor.execute("select * from test").fetchall()
# cursor.execute("delete from test where id=1")
# cursor.commit()
# cursor.close()
print(rows)
# print(type(int(rows[0])))
