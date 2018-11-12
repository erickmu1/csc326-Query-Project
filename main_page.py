from bottle import run, route, request, template, static_file, redirect, default_app, error, url
from collections import Counter
from database_access import find_urls
import json
import httplib2
import urllib

# Libraries for Google Login
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

# Library for Beaker session management
from beaker.middleware import SessionMiddleware

# Library for Database Management
import sqlite3
import database_access

# Python version: 3.5.6 (3.7)
# To run: type in 'python main_page.py'

# url link to home page
home_url = ""

# holds entire list of words that have been searched
# total_list = Counter()

# holds list of words user inputted last
prev_list = Counter()

# keyword to be used to search for URLs
searched_word = ""

# holds list for all URLs given the first word in user's input
total_url_list = [] 

# holds list for up to 5 URLs depending on the page 
current_page_urls =[]

# search history
# popular_list = []

# holds the current session
user_session = None
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(default_app(), session_opts)

# holds credentials
storage = Storage('auth_credentials')
if storage.get() is not None:
    storage.delete()

# Database Connection
db_conn = sqlite3.connect('dbFile.db')


@route('/')
def keywords():
    global home_url
    home_url = request.url
    return template('webpages/home_page', user_input=None, current_page_urls=current_page_urls, 
                    total_url_list=total_url_list, start_site=True, user=user_session)


@route('/', method='POST')
def display_keywords():

    # Enable user "Sign In" through google accounts
    if request.forms.get('SignIn') is not None:

        # If already authorized, no need to re-authorize
        if storage.get() is not None:
            # Refresh access token
            credentials = storage.get()
            credentials.get_access_token()

            # Create session
            redirect('/sign_in')

        # AUTHORIZATION
        # Create Flow object from client_secrets.json
        flow = flow_from_clientsecrets('client_secret.json',
                                       scope=['https://www.googleapis.com/auth/plus.me',
                                              'https://www.googleapis.com/auth/userinfo.email'],
                                       redirect_uri='http://localhost:8080/redirect')

        # Retrieve authorization server URI generated by flow
        auth_uri = flow.step1_get_authorize_url()

        # Redirect user to auth_uri (to get user authorization)
        redirect(str(auth_uri))

    # Sign Out
    elif request.forms.get('SignOut') is not None:
        redirect('/sign_out')

    # POST received keyboard input
    global current_page_urls
    global total_url_list
    global prev_list
    global searched_word
    global home_url
    home_url = request.url

    keywords_input_raw = request.forms.get('keywords')
    user_input = None
    keywords_list = []

    # NOTE. form submissions may not only pertain to the search bar
    if keywords_input_raw is not None:
        # lower() makes it turn into lowercase
        # removed leading, ending and duplicate spaces
        keywords_input = " ".join(keywords_input_raw.split()).lower()

        # error checking for no user input
        if keywords_input == "":
            user_input = None
            keywords_list = prev_list

        else:
            
            user_input = keywords_input_raw

            # separating string into words and putting it into an array
            keywords_original_list = keywords_input.split(" ")

            # recording number of occurrences for each word
            keywords_list = Counter(keywords_original_list)
            prev_list = keywords_list

            # getting first word of user's input 
            searched_word = keywords_original_list[0]
            total_url_list = find_urls(db_conn, searched_word)


            # Check if file exists. If not, create a new one
            with open('json/url_results.json', 'w') as outfile:
                json.dump(total_url_list, outfile)



    return template('webpages/home_page', user_input=user_input, current_page_urls=current_page_urls, 
                    total_url_list=total_url_list, start_site=False, user=user_session)


@route('/sign_in')
def sign_in():

    # Create new session
    global user_session

    # Session should not exist prior to this one
    if user_session is not None:
        print('ERROR HERE!')

    user_session = request.environ.get('beaker.session')

    # Retrieve data from Google (granted access) and store
    credentials = storage.get()
    http = httplib2.Http()
    http = credentials.authorize(http)

    # Get user email
    users_service = build('oauth2', 'v2', http=http)
    user_document = users_service.userinfo().get().execute()
    user_session['email'] = user_document['email']
    # user_session['picture'] = user_document['picture']
    # print(user_document)

    redirect('/')


@route('/redirect')
def redirect_page():

    # User authorizes Google account access
    code = request.query.get('code', '')

    # Request access using the received code
    with open('client_secret.json', 'r') as read_file:
        data = json.load(read_file)
    data = data['web']

    flow = OAuth2WebServerFlow(client_id=data['client_id'],
                               client_secret=data['client_secret'],
                               scope=['https://www.googleapis.com/auth/plus.me',
                                      'https://www.googleapis.com/auth/userinfo.email'],
                               redirect_uri=data['redirect_uris'][0])

    del data

    # Exchange code for access token
    global storage

    credentials = flow.step2_exchange(code)
    print(credentials)
    storage.put(credentials)
    # token = credentials.id_token['sub']

    redirect('/sign_in')


@route('/sign_out')
def sign_out():

    # Clear session (Credentials remain)
    global user_session

    user_session.delete()
    user_session = None

    redirect('/')


@error(404)
def error_handler_404(error):
    return template('webpages/error_page', home_url=home_url, user=user_session)

# Static CSS Files
@route('/style/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='style')

# Static JavaScript Files
@route('/js/<filename:re:.*\.js>')
def send_javscript(filename):
    return static_file(filename, root='js')

# Static txt files
@route('/json/<filename:re:.*\.json>')
def send_txt(filename):
    return static_file(filename, root="json")

# Static jpg files
@route('/images/<filename:re:.*\.jpg>')
def send_img(filename):
    return static_file(filename, root="images")

    
run(app, host='localhost', port=8080, debug=True)


