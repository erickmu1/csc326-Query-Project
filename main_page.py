from bottle import run, route, request, template, response
from collections import Counter

total_list = Counter()

#with the line below, it's used for the server to find the site for hosting AND
#it takes the route below it to be the first page the user sees
@route('/') 
def keywords():
    return template('website_template', keywords_list=[], popular_list=[])

#does the method in the function have to match the method of the form in HTML?
@route('/', method='POST')
def display_keywords():

    global total_list
    num_words = 20

    #get string from query submission
    #lower() makes it turn into lowercase
    keywords_input_raw = request.forms.get('keywords').lower()
    keywords_input = " ".join(keywords_input_raw.split())

    #separating string into words and putting it into an array
    keywords_original_list = keywords_input.split(" ")

    #recording number of occurrences for each word 
    keywords_list = Counter (keywords_original_list)

    #can add counter objects together 
    total_list += keywords_list


    popular_list = total_list.most_common(num_words)

    # for keyword in keywords_list:

        # for popular in popular_list:

    
    return template('website_template', keywords_list=keywords_list, popular_list=popular_list)

#WHY IS THE TOTAL NUMBER OF POPULAR WORD OCCURRENCES DOUBLING EACH TIME???
#Figure out how to not include empty answers 

run(host='localhost', port=8080, debug = True)

