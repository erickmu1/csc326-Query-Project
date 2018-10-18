# TESTING Correctness of the Crawler

# Have url .txt files in the same directory as this file and just run test_crawler.py in terminal
# Some test cases have been provided (names of files stated later in the code)
# This tester gives you an indication of possible errors and tests the correctness of the
# crawler by verifying the persistent data structures have been built correctly
from crawler import crawler


# Check that every word has a doc_id(s) associated to it [crawler]
# Note that by construction, every word has a word_id
def verify_lexicon(obj):
    """Verify that every word actually comes from a document"""

    res_inv_idx = obj.get_resolved_inverted_index()

    # Ensure each word has at least 1 URL attached to it
    for word in obj._word_id_cache:

        # print word, ": ", res_inv_idx[word]
        if word not in res_inv_idx:
            return False
        elif len(res_inv_idx[word]) == 0:
            return False

    return True


# Check that every url in text file has an index characterizing it
def verify_doc_idx(obj, url_file):
    """Verify that every processed URL is in the crawler's database"""

    # Read through all URLs provided in .txt file
    txt_file = open(url_file, "r")
    seen = set({})
    non_empty_urls = True

    for url in txt_file:

        # if duplicate URL, no need to check its index again
        if url not in seen:
            seen.add(url)
        else:
            continue

        print (obj._fix_url(url.strip(), ""), "has",)

        if obj._doc_id_cache[obj._fix_url(url.strip(), "")] in obj._doc_idx_cache:
            # Valid URL
            print (len((obj._doc_idx_cache[obj._doc_id_cache[obj._fix_url(url.strip(), "")]])), "words on its page")
        else:
            # URL has no doc_idx associated to it - means the URL is invalid or not parsed
            print ("nothing on its page")
            non_empty_urls = False

    return non_empty_urls


# Check that inverted_index == resolved_inverted_index
def verify_inverted_index(obj):
    """Verify that inverted_index and resolved_inverted_index agree"""

    inv_idx = obj.get_inverted_index()
    res_idx = obj.get_resolved_inverted_index()

    for keyword in res_idx:

        if obj._word_id_cache[keyword] not in inv_idx:
            # Check that every word in resolved_inverted_index has its word_id
            # in inverted_index
            print ("There is a word without a word_id!")
            return False

        else:
            for url in res_idx[keyword]:
                # Check that every URL in resolved_inverted_index has its doc_id
                # in inverted_index
                if obj._doc_id_cache[url] not in inv_idx[obj._word_id_cache[keyword]]:
                    print ("There is a URL without a doc_id OR mapped to the wrong keyword!")
                    return False

    return True


# TESTING
    # Provided URL test cases:
    #   urls.txt
    #   empty_urls.txt
    #   duplicate_urls.txt
    #   invalid_urls.txt

# Set file containing URLs - CHANGE ME!
url_files = "urls/urls.txt"

# Crawl the provided URLs
bot = crawler(None, url_files)
bot.crawl(depth=0)

# Run Test Cases!
print ("\nTESTING the CRAWLER for", url_files, "\n")

# Check that our lexicon is valid
if not verify_lexicon(bot):
    print ("\nThere is a word not associated to any document!\n")
else:
    print ("\nAll words in lexicon are associated to at least one document!\n")

# NOTE. invalid urls must be empty
# NOTE. if a url has no doc_idx, then it cannot be found since no words are associated to it
if not verify_doc_idx(bot, url_files):
    print ("\nThere is a URL that is empty!\n")
else:
    print ("\nAll URLs have words associated to them!\n")

# Check our inverted_index and resolved_inverted_index match
if not verify_inverted_index(bot):
    print ("\ninverted_index and resolved_index don't match!\n")
else:
    print ("\ninverted_index and resolved_index are the same!\n")

# OBSERVATIONS.
#   http and https are considered different URLs despite mapping to the same website
#   In _doc_id_cache, there are urls that have not been parsed for a doc_idx due to the restriction on depth
