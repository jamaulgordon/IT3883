# Program Name: Assignment5.py
# Course: IT3883/W02
# Student Name: Jamaul Gordon
# Assignment Number: 5
# Due Date: 04/15/25
# Purpose: Load temperature data into an SQLite database and calculate averages for Sunday and Thursday.
# Resources: Python docs, sqlite3 module

import sqlite3
from pathlib import Path

DB_NAME = 'temperatures.db'
INPUT_FILE = 'Assignment5input.txt'

def initialize_database(conn):
    # Resetting the table every time we run the script so it's clean
    with conn:
        conn.execute('DROP TABLE IF EXISTS Temperature_Readings')
        conn.execute('''
            CREATE TABLE Temperature_Readings (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Day_Of_Week TEXT NOT NULL,
                Temperature_Value REAL NOT NULL
            )
        ''')

def load_data_from_file(filepath, conn):
    #Reading the input file and loading valid rows into the database
    if not Path(filepath).is_file():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    with open(filepath, 'r') as file, conn:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 2:
                continue  # Skip anything that’s not formatted like "Day Temp"
            day, value = parts
            try:
                temp = float(value)
                conn.execute(
                    'INSERT INTO Temperature_Readings (Day_Of_Week, Temperature_Value) VALUES (?, ?)',
                    (day.capitalize(), temp)
                )
            except ValueError:
                continue  #Ignore lines with invalid numbers

def get_average_temp(conn, day):
    #Runs a basic SQL AVG query for the given day
    cursor = conn.execute(
        'SELECT ROUND(AVG(Temperature_Value), 2) FROM Temperature_Readings WHERE Day_Of_Week = ?',
        (day.capitalize(),)
    )
    result = cursor.fetchone()
    return result[0] if result and result[0] is not None else 0.0  #Return 0.0 if no data for the day

def main():
    print("Processing temperature data...\n")

    try:
        with sqlite3.connect(DB_NAME) as conn:
            initialize_database(conn)          # Set up the database from scratch
            load_data_from_file(INPUT_FILE, conn)  # Load data from the text file

            sunday_avg = get_average_temp(conn, 'Sunday')
            thursday_avg = get_average_temp(conn, 'Thursday')

            # Show the final results
            print(f"✅ Average Temp on Sunday: {sunday_avg}°F")
            print(f"✅ Average Temp on Thursday: {thursday_avg}°F")

    except Exception as e:
        # Catch anything weird that goes wrong
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()