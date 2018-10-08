from bottle import run, route, request, template, response, static_file
from collections import Counter

#Python version: 3.5.6
# To run: type in 'python main_page.py'

#hold entire list of words that have been searched
total_list = Counter()

@route('/') 
def keywords():
    return template('website_template', user_input=None, keywords_list=[], popular_list=[], start_site=True)

@route('/', method='POST')
def display_keywords():

    global total_list
    num_words = 20

    keywords_input_raw = request.forms.get('keywords')

    #lower() makes it turn into lowercase
    #removed leading, ending and duplicate spaces
    keywords_input = " ".join(keywords_input_raw.split()).lower()

    #error checking for no user input
    if keywords_input == "":
        user_input = None
        keywords_list =[]

    else:
        user_input = keywords_input_raw

        #separating string into words and putting it into an array
        keywords_original_list = keywords_input.split(" ")

        #recording number of occurrences for each word 
        keywords_list = Counter (keywords_original_list)

        total_list += keywords_list

    #take the top 20 most popular words
    popular_list = total_list.most_common(num_words)
    
    return template('website_template', user_input=user_input, keywords_list=keywords_list, popular_list=popular_list, start_site=False)

# Static CSS Files
@route('/static/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='static')

# Static jpg files
@route ('/images/<filename:re:.*\.jpg>')
def send_img(filename):
    return static_file(filename, root="images")

run(host='localhost', port=8080, debug = True)

