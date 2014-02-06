# Sebastian Raschka, 2014
# Adding a new column to an existing SQLite database

import sqlite3

sqlite_file = ''
table_name = ''
new_column = ''  # name of the new column
column_type = '' # E.g., INTEGER, TEXT, NULL, REAL, BLOB
default_val = '' # E.g., 1

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# A) Adding a new column without a row value
c.execute("ALTER TABLE {dn} ADD COLUMN '{cn}' {ft}"\
        .format(tn=table_name, cn=new_column, ct=column_type))

# B) Adding a new column with a default row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{fn}' {ft} DEFAULT {df}"\
        .format(tn=table_name, cn=new_column, ct=column_type, df=default_val))

conn.commit()
conn.close()
