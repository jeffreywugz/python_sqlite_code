# Sebastian Raschka, 2014
# Selecting rows from an existing SQLite database

import sqlite3

sqlite_file = ''
table_name = ''
column_1 = ''
col_of_interest = ''

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


# All columns for row that match a certain value in column_1
c.execute("SELECT (*) FROM {tn} WHERE {cn}=1 ".\
        format(tn=table_name, cn=column_1)):
all_rows = c.fetchall()


# A particular column for rows that match a certain value in column_1 
c.execute("SELECT (coi) FROM {tn} WHERE {cn}=1 ".\
        format(coi=column_of_interest, tn=table_name, cn=column_1)):
all_rows = c.fetchall()


# Selecting only 10 rows that match a certain value in column_1
c.execute("SELECT (*) FROM {tn} WHERE {cn}=1 LIMIT 10".\
        format(tn=table_name, cn=column_1)):
ten_rows = c.fetchall()


conn.close()
