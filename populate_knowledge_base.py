import sqlite3
import csv

# Connect to the database (it will create the database file if it does not exist)
conn = sqlite3.connect('hardware_knowledge_base.db')
cursor = conn.cursor()

# Create the knowledge table
cursor.execute('''CREATE TABLE IF NOT EXISTS knowledge
                  (question TEXT, answer TEXT)''')

# Function to add knowledge
def add_knowledge(question, answer):
    cursor.execute("INSERT INTO knowledge (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()

# Read the CSV file and populate the database
with open('hardware_knowledge_base.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        add_knowledge(row['question'], row['answer'])

print("Knowledge base created and populated from CSV.")
