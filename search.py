def spell_check(keyword, db_conn):
    """ Iterates through every word in lexicon database and calculates the Levenshtein distance(keyword, word)
        using Dynamic Programming formulation of the problem """

    # Calculate Levenshtein Distance
    closest_word = ''
    closest_dist = 100  # Make this infinity

    # Retrieve words from database
    for element in db_conn.cursor().execute("SELECT word FROM lexicon"):

        word = element[0]

        # Make a (keyword x word) array
        min_dist = [[0 for c in range(len(word) + 1)] for r in range(len(keyword) + 1)]

        # Calculate Levenshtein distance
        for row in range(len(keyword) + 1):
            for col in range(len(word) + 1):

                # Base Case
                if min(row, col) is 0:
                    min_dist[row][col] = max(row, col)

                # Sub-problem Optimization
                else:
                    min_dist[row][col] = min(min_dist[row-1][col] + 1, min_dist[row][col-1] + 1,
                                             min_dist[row-1][col-1] + (1 if keyword[row - 1] != word[col - 1] else 0))

        # Update closest word
        if min_dist[len(keyword)][len(word)] < closest_dist:
            closest_dist = min_dist[len(keyword)][len(word)]
            closest_word = word

    return closest_word


if __name__ == "__main__":

    import sqlite3

    # Set up db Connection
    db_conn = sqlite3.connect("dbFile.db")
    word = 'woogle'
    print("Given word: ", word)
    match = spell_check(word, db_conn)
    print("Closest match: ", match)
