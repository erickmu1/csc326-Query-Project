# Runs Crawler and PageRank Algorithm
# Prints PageRank scores sorted from greatest-to-least
import pprint
import sqlite3
from crawler import crawler
from multicrawler import multicrawler

# TEST SCRIPT

# Initialize Database
db_conn = sqlite3.connect('dbFile.db')

# Run Crawler --> Calls PageRank --> Populates database
# bot = crawler(db_conn, 'urls/urls.txt')
bot = multicrawler(db_conn, 'urls/urls.txt')
bot.crawl(depth=1)

# Print PageRanks sorted in greatest-to-least order from database
print('\nPAGE RANKS sorted greatest-to-least by scores (left column) with their corresponding DOC_IDs (right column)\n')
data = []
for row in db_conn.cursor().execute("SELECT * FROM document ORDER BY page_rank DESC"):
    data.append(row)
pprint.pprint(data)

# print("\nLEXICON")
# data = []
# for row in db_conn.cursor().execute("SELECT * FROM lexicon"):
#     data.append(row)
# pprint.pprint(data)
#
# print("\nDOC IDX")
# data = []
# for row in db_conn.cursor().execute("SELECT * FROM page_content"):
#     data.append(row)
# pprint.pprint(data)
#
# print("\nPAGE RANK")
# data = []
# for row in db_conn.cursor().execute("SELECT * FROM document"):
#     data.append(row)
# pprint.pprint(data)
#
# print("\nMAPPING")
# data = []
# for row in db_conn.cursor().execute("SELECT * FROM resolved_map"):
#     data.append(row)
# pprint.pprint(data)

# Delete tables and close Database
db_conn.cursor().execute("DROP TABLE lexicon")
db_conn.cursor().execute("DROP TABLE page_content")
db_conn.cursor().execute("DROP TABLE document")
db_conn.cursor().execute("DROP TABLE resolved_map")

db_conn.commit()
db_conn.close()
