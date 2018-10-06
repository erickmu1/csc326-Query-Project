from bottle import run, route, request, template, response
from collections import OrderedDict

#with the line below, it's used for the server to find the site for hosting AND
#it takes the route below it to be the first page the user sees
@route('/') 
def keywords():
    return template('website_template')

#does the method in the function have to match the method of the form in HTML?
@route('/', method='POST')
def display_keywords():

    #get string from query submission
    #lower() makes it turn into lowercase
    keywords_input = request.forms.get('keywords').lower().rstrip()

    #separating string into words and putting it into an array
    keywords_original_list = keywords_input.split(" ")

    keywords_list=[]

    for word in keywords_original_list:
        keywords_count = keywords_input.count(word)

        #creating a pair of str and int
        keyword_pair = (word, keywords_count)
        keywords_list.append(keyword_pair)

    # retains order of words from input after duplicates are removed
    keywords_list = sorted(set(keywords_list),key=keywords_list.index)

    for pair in keywords_list:
        print ('Word is ' + pair[0] + ' and count is ' + str(pair[1]))
    

    # return template('table_template', keywords_list = keywords_list)


run(host='localhost', port=8080, debug = True)

