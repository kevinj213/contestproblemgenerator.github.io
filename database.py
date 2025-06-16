import sqlite3 as sq
import csv

# Connect to SQLite database (creates it if it doesn't exist)
conn = sq.connect("problems.db")
cur = conn.cursor()

# Create table with a unique constraint to prevent duplicates
cur.execute("""
CREATE TABLE IF NOT EXISTS problems (
    Source TEXT,
    Year INTEGER,
    Round TEXT,
    Problem_Number INTEGER,
    Difficulty INTEGER,
    Topic TEXT,
    Subtopic TEXT,
    Problem_Statement TEXT,
    Hint TEXT,
    Answer TEXT,
    Solution TEXT,
    Link TEXT,
    UNIQUE(Source, Year, Round, Problem_Number)
)
""")

# Open and read the CSV file
with open('math_problems.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cur.execute('''
            INSERT OR IGNORE INTO problems (Source, Year, Round, Problem_Number, Difficulty, Topic, Subtopic, Problem_Statement, Hint, Answer, Solution, Link)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row['Source'],
            int(row['Year']),
            row['Round'],
            int(row['Problem Number']),
            int(row['Difficulty']),
            row['Topic'],
            row['Subtopic'],
            row['Problem Statement'],
            row['Hint'],
            row['Answer'],
            row['Solution'],
            row['Link']
        ))

print("Data imported successfully (duplicates skipped).")

conn.commit()
conn.close()