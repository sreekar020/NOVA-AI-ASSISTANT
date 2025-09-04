import sqlite3

# Connect to (or create) the feedback.db file
conn = sqlite3.connect('feedback.db')
cursor = conn.cursor()

# Create the feedback table
cursor.execute('''
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT NOT NULL,
    stars INTEGER NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()

print("feedback.db created with feedback table.")
