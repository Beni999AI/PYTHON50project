import sqlite3
import datetime

def get_db():
    db = sqlite3.connect("flights.db")
    create_table(db)
    return db

def create_table(db):
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS flights (
                flight TEXT PRIMARY KEY,
                airline TEXT,
                from TEXT,
                to TEXT,
                scheduled_departure DATETIME,
                scheduled_arrival DATETIME,
                status TEXT,
                saved_at DATETIME)""")
    db.commit()

def save(db, flight, airline, from_, to, scheduled_departure, scheduled_arrival, status):
    saved_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur = db.cursor()
    cur.execute("INSERT INTO flights (flight, airline, from, to, scheduled_departure, scheduled_arrival, status, saved_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (flight, airline, from_, to, scheduled_departure, scheduled_arrival, status, saved_at))
    db.commit()

def view(db, flight):
    cur = db.cursor()
    cur.execute("SELECT * FROM flights WHERE flight = ?", (flight,))
    result = cur.fetchone()
    if result:
        return {
            "flight":result[0],
            "airline" : result[1],
            "from" : result[2],
            "to" : result[3],
            "scheduled_departure":result[4],
            "scheduled_arrival":result[5],
            "status":result[6],
            "saved_at":result[7]
        }
    else:
        return None


