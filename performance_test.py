# Demonstrates Performance increase of Multi-threaded Crawler
import sqlite3
import time
from crawler import crawler
from multicrawler import multicrawler

# Database Connection
db_conn1 = sqlite3.connect('file1.db')
db_conn2 = sqlite3.connect('file2.db')

# Create Single-Thread Crawler
bot1 = crawler(db_conn1, 'urls/urls.txt')

# Create Multi-Thread Crawler (uses up to 4 threads)
bot2 = multicrawler(db_conn2, 'urls/urls.txt')

depth = 1

# Time Single-Thread
print('\nRunning Single-Thread\n')
start = time.perf_counter()
bot1.crawl(depth=depth)
end = time.perf_counter()

time1 = end - start

# Time Multi-Thread
print('\nRunning Multi-Thread\n')
start = time.perf_counter()
bot2.crawl(depth=depth)
end = time.perf_counter()

time2 = end - start

# Print Elapsed time
print('Time for Single-Thread: ', time1)
print('Time for Multi-Thread: ', time2)
