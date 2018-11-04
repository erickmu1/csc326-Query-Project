# Runs Crawler and PageRank Algorithm
# Prints PageRank scores sorted from greatest-to-least
import pprint
import sqlite3
from crawler import crawler

# TEST SCRIPT

# Initialize Database
db_conn = sqlite3.connect('dbFile.db')

# Run Crawler --> Calls PageRank --> Populates database
bot = crawler(db_conn, 'urls/urls.txt')
bot.crawl(depth=1)

# Print PageRanks sorted in greatest-to-least order from database
print('\nPAGE RANKS sorted greatest-to-least by scores (left column) with their corresponding doc_ids (right column)\n')
data = []
for row in db_conn.cursor().execute("SELECT * FROM page_rank ORDER BY rank_score DESC"):
    data.append(row)
pprint.pprint(data)

# Delete tables and close Database
db_conn.cursor().execute("DROP TABLE lexicon")
db_conn.cursor().execute("DROP TABLE document_idx")
db_conn.cursor().execute("DROP TABLE inverted_idx")
db_conn.cursor().execute("DROP TABLE page_rank")

db_conn.commit()
db_conn.close()
