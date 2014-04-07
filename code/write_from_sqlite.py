import sqlite3

def write_from_query(db_name, table_name, condition, content_column, out_file):
    '''
    Writes contents from a SQLite database column to an output file
    
    Keyword arguments:
        db_name (str): Path of the .sqlite database file.
        table_name (str): Name of the target table in the SQLite file.
        condition (str): Condition for querying the SQLite database table.
        content_colum (str): Name of the column that contains the content for the output file.
        out_file (str): Path of the output file that will be written.

    '''
    # Connecting to the database file
    conn = sqlite3.connect('zinc12_drugnow_nrb(copy).sqlite')
    c = conn.cursor()

    # Querying the database and writing the output file
    c.execute('SELECT ({}) FROM {} WHERE {}'.format(content_column, table_name, condition))
    with open(out_file, 'w') as outf:
        for row in c:
            outf.write(row[0])

    # Closing the connection to the database
    conn.close()

if __name__ == '__main__':
    write_from_query(
        db_name='my_db.sqlite',
        table_name='my_table',
        condition='variable1=1 AND variable2<=5 AND variable3="Zinc_Plus"',
        content_column='variable4',
        out_file='sqlite_out.txt'
    )
        


