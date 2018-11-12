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

LAB 3
- To run website: run "crawler.py". Then run "main_page.py" and go to http://localhost:8080/"
- BONUSs JavaScript and AJAX for dynamic changing of links (Completed)

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
