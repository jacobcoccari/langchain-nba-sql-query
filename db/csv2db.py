import sqlite3
import csv

# Define the input CSV file and the SQLite database file
input_csv = '/Users/jacob/src/consulting/MyRareData/nba_query_demo/db/nba_roster.csv'
database_file = '/Users/jacob/src/consulting/MyRareData/nba_query_demo/db/nba_roster.db'

# Connect to the SQLite database
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''CREATE TABLE IF NOT EXISTS nba_roster (
                    Team TEXT,
                    NAME TEXT,
                    Jersey TEXT,
                    POS TEXT,
                    AGE INT,
                    HT TEXT,
                    WT TEXT,
                    COLLEGE TEXT,
                    SALARY TEXT
                )''')

# Read data from the CSV file and insert it into the SQLite table
with open(input_csv, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header row
    
    for row in csv_reader:
        cursor.execute('INSERT INTO nba_roster VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', row)

# Commit the changes and close the database connection
conn.commit()
conn.close()

print(f'Data from {input_csv} has been successfully imported into {database_file}')
