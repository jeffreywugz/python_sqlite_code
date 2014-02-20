python_sqlite_code
==================

Code for working with SQLite databases in Python


### Script for printing a database summary

Script: [./code/print_db_info.py](./code/print_db_info.py)

**Example output:**
<pre>
 Total rows: 140059029

 Column Info:
 ID, Name, Type, NotNull, DefaultVal, PrimaryKey
 (0, 'molecule_id', 'TEXT', 0, None, 0)
 (1, 'purchasable', 'INT', 0, None, 0)
 (2, 'db_origin', 'TEXT', 0, None, 0)

 Number of entries per column:
 molecule_id: 140059029
 db_origin: 6059029
 purchasable: 6059029
</pre>

### Creating a new SQLite database

Script: [./code/create_new_db.py](./code/create_new_db.py)



### Adding a new column

Script: [./code/add_new_column.py](./code/add_new_column.py)



### Creating an index on a column with unique! values
Boosts performance for data base operations, but assumes that  
values are unique in the indexed column.

Script: [./code/create_unique_index.py](./code/create_unique_index.py)




### Getting column names 

Script: [./code/get_columnnames.py](./code/get_columnnames.py)




### Selecting row entries

Script: [./code/selecting_entries.py](./code/selecting_entries.py)




### Updating row entries

Script: [./code/updating_rows.py](./code/updating_rows.py)




### Inserting or updating records
Update records or insert them if they don't exist.  
Note that this is a workaround to accomodate for missing  
SQL features in SQLite.  

Script: [./code/update_or_insert_records.py](./code/update_or_insert_records.py)
