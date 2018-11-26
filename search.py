def spell_check(keyword, db_conn):

    # Retrieve all words in database
    word_list = []
    for row in db_conn.cursor().execute("SELECT word FROM lexicon"):
        word_list.append(row[0])

    # Calculate Levenshtein Distance
    closest_word = ''
    closest_dist = 100  # Make this infinity

    for word in word_list:
        # Make a (keyword x word) array
        row = [0] * len(word)     # Each row has "word" columns
        min_dist = row * len(keyword)   # There are "keyword" rows

        for row in range(len(keyword)):
            for col in range(len(word)):
                # Base Case
                if min(row, col) is 0:
                    min_dist[row][col] = max(row, col)
                # Sub-problem Optimization
                else:
                    min_dist[row][col] = min(min_dist[row-1][col] + 1, min_dist[row][col-1] + 1,
                                             min_dist[row-1][col-1] + (1 if keyword[row] == word[col] else 0))

        # Update closest word
        if min_dist[len(word) - 1][len(keyword) - 1] < closest_dist:
            closest_dist = min_dist[len(word) - 1][len(keyword) - 1]
            closest_word = word

    return closest_word
