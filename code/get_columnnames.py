# Sebastian Raschka, 2014
# Getting column names of an SQLite database table

import sqlite3

sqlite_file = ''
table_name = ''

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('PRAGMA TABLE_INFO({})'.format(table_name))

# every column will be repr. by a tuples with the following attributes:
# (id, name, type, notnull, default_value, primary_key)

names = [tup[1] for tup in c.fetchall()]
# collect names in a list
# e.g., [col1_name, col2_name, col3_name, ...]

conn.close()
