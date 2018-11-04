# csc326-Query-Project
CSC326 lab
Python 3

LAB 1
- to run the website: run "main_page.py" and go to "http://localhost:8080/"
- to test the crawler run "test_crawler.py". Can modify the input URLs in source code by changing the .txt file
- test cases for the crawler can be found in the urls folder

LAB 2
- public IP address: 52.44.172.143
- benchmark setup: 
    - have apache installed
    - have dstat installed
    - run: ab -n 150 -c 50 http://52.44.172.143:80/?keywords=helloworld+foo+bar
- Enabled Google APIs: NONE

LAB 3
- How to test backend:
    - to print pagerank scores in greatest-to-least order: run "run_backend_test.py"
    - to print out all data from SQL database: run "crawler.py"
- BONUS:
    - multithreading: NOT IMPLEMENTED YET
    - script demonstrating increase in performance: "dne.py"
    - Observed Performance Gain: None
