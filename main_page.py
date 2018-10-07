from bottle import run, route, request, template, response
from collections import Counter

#hold entire list of words that have been searched
total_list = Counter()

@route('/') 
def keywords():
    return template('website_template', keywords_list=[], popular_list=[])

@route('/', method='POST')
def display_keywords():

    global total_list
    num_words = 20

    #lower() makes it turn into lowercase
    keywords_input_raw = request.forms.get('keywords').lower()

    #removed leading, ending and duplicate spaces
    keywords_input = " ".join(keywords_input_raw.split())

    #separating string into words and putting it into an array
    keywords_original_list = keywords_input.split(" ")

    #recording number of occurrences for each word 
    keywords_list = Counter (keywords_original_list)

    #can add counter objects together 
    total_list += keywords_list

    #take the top 20 most popular words
    popular_list = total_list.most_common(num_words)

    
    return template('website_template', keywords_list=keywords_list, popular_list=popular_list)


run(host='localhost', port=8080, debug = True)

