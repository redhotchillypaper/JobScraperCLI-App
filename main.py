
from dotenv import load_dotenv
import os
from databases import Database as DB

def main():
    # Load .env file
    load_dotenv()  # by default looks for ".env" in the current directory

    
    
    
    #Databases
    db_path = os.getenv("DATABASE_PATH")


    table = "jobs"
    database = DB(db_path, table)
    database.create_database()
    # database.create_database(db, table)                       # create table if it doesn't exist
    database.add_to_database("cook", "529", "https://529.com")
    print(f"Inserted row id: {database.new_id}")

    rows = database.get_all_jobs()
    for r in rows:
        print(r)

    # database.clean_database()   # uncomment to clear the table
    # database.reset_database()   # uncomment to drop all tables



if __name__ == "__main__":
    main()




# TODO:
# connect scraper to database (OOP?)
# database of already found jobs
# scraper of linkedin (maybe some other resources attached)
# email automatio
# salary to hourly convert and preference in emaila






# ChatGPT suggested:

# 🎯 Core Features (MVP in ~1 week)

# CLI: User enters a keyword (e.g., “Python developer” or “Retail”).

# Script scrapes Indeed (or another site with jobs).

# Collect job titles + links into a list.

# Sends results to your email (via Gmail SMTP or similar).



# 🔧 Tools to Use

# requests → fetch job listings.

# BeautifulSoup4 → parse HTML.

# smtplib → send results to your email.

# (Optional later) schedule or cron → run daily.



# 🛠 Suggested Build Steps (Day-by-Day)

# Day 1 (today/tmr):

# Pick 1 job site (Indeed, Glassdoor, Workopolis).

# Write scraper that gets job title + link for a given search.

# Day 2:

# Package results into a clean list or table.

# Print results in terminal for testing.

# Day 3:

# Add email sending function → mail results to yourself.

# Day 4:

# Polish CLI (take keyword + location as input).

# Handle errors (e.g., no jobs found).

# Day 5:

# Clean code → add README.md, screenshots.

# Push to GitHub.

# Stretch Goal (Weekend):

# Automate with schedule → daily job report at 9 AM.

