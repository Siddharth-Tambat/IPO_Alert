import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DB_PATH = os.getenv('DB_PATH')

# Database connection
def connect_db():
    return sqlite3.connect(DB_PATH)

# Function to insert IPO data into the database
def insert_ipo(ipo_name, open_dt, close_dt, status=0):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ipos (ipo_name, open_dt, close_dt, status)
        VALUES (?, ?, ?, ?)
    ''', (ipo_name, open_dt, close_dt, status))
    conn.commit()
    conn.close()

# Function to check if a specific IPO (by name and open date) exists in the database
def ipo_exists(ipo_name, open_dt):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT COUNT(*) FROM ipos WHERE ipo_name = ? AND open_dt = ?
    ''', (ipo_name, open_dt))
    exists = cursor.fetchone()[0] > 0  # If count > 0, the IPO exists
    conn.close()
    return exists

# Function to get IPOs with pending alerts (status = 0)
def get_pending_ipos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT ipo_name, open_dt, close_dt FROM ipos WHERE status = 0")
    pending_ipos = cursor.fetchall()
    conn.close()
    return pending_ipos

# Function to update the IPO status to 1 after sending alert
def update_ipo_status(ipo_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE ipos SET status = 1 WHERE ipo_name = ?
    ''', (ipo_name,))
    conn.commit()
    conn.close()
