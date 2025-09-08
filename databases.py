import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# first initial push
def create_database():
    cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    link TEXT
)
""")

def add_to_database(title, company, link):
    cursor.execute("INSERT INTO jobs (title, company, link) VALUES (?, ?, ?)",
               (f"{title}", "{company}", "{href}"))



def main():
    create_database()
    add_to_database("cook", "529", "https://529.com") #example
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()




