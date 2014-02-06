# Sebastian Raschka, 2014
# Update records or insert them if they don't exist.
# Note that this is a workaround to accomodate for missing
# SQL features in SQLite.

import sqlite3

sqlite_file = ''
table_name = ''
id_column = ''
column_name = ''

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Tries to insert an ID (if it does not exist yet)
# with a specific value in a second column 
c.execute('INSERT OR IGNORE INTO {tn} (idf, cn) VALUES (idv, val)'.\
        format(tn=table_name, idf=id_column, cn=column_name, idv=id_value, val=value))

# Updates the newly inserted or pre-existing entry            
c.execute('UPDATE {tn} SET {cn}={val} WHERE {idf}={idv}'.\
        format(tn=table_name, cn=column_name, val=value, idf=id_column idv=id_value))

conn.commit()
conn.close()
