# Sebastian Raschka, 2014
# Creating an index on a column with unique! values
# Boosts performance for data base operations.

import sqlite3

sqlite_file = ''
table_name = ''
column_name = '' # name of the column that should be indexed 
index_name = ''	 # some name for the new unique index

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating an unique index
c.execute('CREATE INDEX {ix} on {tn}({cn})'\
        .format(ix=index_name, tn=table_name, cn=column_name))

# Dropping the unique index
# E.g., to avoid future conflicts with update/insert functions
c.execute('DROP INDEX {ix}'.format(ix=index_name))

conn.commit()
conn.close()
