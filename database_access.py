# Functions allowing to retrieve data from our database


# Return a list of all urls ordered by page_rank matching a given keyword
def find_urls(db_conn, keyword):
    """Returns a list of all URLs ordered by page_rank matching KEYWORD from DATABASE"""

    url_list = []
<<<<<<< HEAD

    # for row in db_conn.cursor().execute("SELECT url FROM resolved_inverted_index WHERE word = ? ORDER BY rank_score DESC", (keyword,)):
    for row in db_conn.cursor().execute("SELECT DISTINCT url FROM resolved_inverted_index WHERE word = ? ORDER BY rank_score DESC", (keyword,)):
    
=======
    for row in db_conn.cursor().execute("SELECT url FROM resolved_map WHERE word = ? ORDER BY page_rank DESC", keyword):
>>>>>>> 895bfaabc0040a32379ae91cf8f6559b9bac0c4f
        url_list.append(row[0])


    return url_list

