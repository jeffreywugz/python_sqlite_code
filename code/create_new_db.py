# Sebastian Raschka, 2014
# Creating a new SQLite database

import sqlite3

sqlite_file = ''
table_name = ''
new_field = 'my_1st_column'
field_type = 'INTEGER'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column 
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name, nf=new_field, ft=field_type))

# Creating a new SQLite table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('CREATE TABLE {dn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_name, nf=new_field, ft=field_type))

conn.commit()
conn.close()
