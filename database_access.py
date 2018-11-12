# Functions allowing to retrieve data from our database


# Return a list of all urls ordered by page_rank matching a given keyword
def find_urls(db_conn, keyword):
    """Returns a list of all URLs ordered by page_rank matching KEYWORD from DATABASE"""

    url_list = []
    for row in db_conn.cursor().execute("SELECT url FROM resolved_inverted_index WHERE word = ? ORDER BY rank_score DESC", keyword):
        url_list.append(row[0])

    return url_list

