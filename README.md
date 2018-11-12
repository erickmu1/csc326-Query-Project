# csc326-Query-Project
CSC326 lab
Python 3

LAB 1
- to run the website: run "main_page.py" and go to "http://localhost:8080/"
- to test the crawler run "test_crawler.py". Can modify the input URLs in source code by changing the .txt file
- test cases for the crawler can be found in the urls folder

LAB 2
- public IP address: 18.211.236.148
- benchmark setup: 
    - have apache installed
    - have dstat installed
    - run: ab -n 150 -c 50 http://52.44.172.143:80/?keywords=helloworld+foo+bar
    - run: dstat (on another computer)

LAB 3
Frontend:
- To run website: run "multicrawler.py". Then run "main_page.py" and go to http://18.211.236.148
- BONUS: JavaScript and AJAX for dynamic changing of links (Completed)

Backend:
- To populate database "dbFile.db" run either crawler.py or multicrawler.py (multi-threaded crawler)
- To run backend to demonstrate required functionality run "run_backend_test.py"
- The following information can be found in the following tables"
    - lexicon in **lexicon** table
    - document_index (doc_id --> word_id(s)) & inverted_index (word_id --> doc_id(s)) in **page_content** table
    - page_ranks in **document** table
    - resolved_inverted_index in **resolved_map** table
- BONUS: multi-threaded crawler (Completed)
    - Can test it by running "performance_test.py"
    - Performance results:
    - given urls: https://www.google.ca/, http://www.eecg.utoronto.ca/, https://www.facebook.com/ & depth: 1
    - execution times are Single: 34.754450423 s & Multi: 9.073222797999996 s

Benchmark Discussion:
It was very apparent that the time per request between the functionality of the two websites for lab 2 and 3 were different. Lab 2 involved creating a new data structure and adding onto it as the user inserted more inputs to search. Lab 3, however, used its crawler to identify and store the URL links before the webpage is run, and remains unchanged throughout the duration of the webpage, until crawler is ran again. From there on, the website looks to its cache to return the designated URLs instead of creating and storing data in data structures, which takes a lot of time and memory should there be countles inputs. 

See more details inside the RESULT.txt
