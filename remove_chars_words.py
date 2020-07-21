# remove_special_characters()
# parameters:
#   text : string - the text for conversion
# returns:
#   text : string - the converted string
# description:
#
def remove_special_characters (text):
    return text

# remove_reserved_words()
# parameters:
#   text : string - the tweet text
# returns:
#   text : string - the modified tweet text
# description:
#   This function splits a string into a list, and removes the reserved words
#       from that list and joins the modified list back into a string.
def remove_reserved_words (text):
    reserved_words = ["rt", "fav"]
    text = text.split()
    for word in reserved_words:
        text.remove(word)
    text = " ".join(text)
    return text

def remove_stopwords (text):
    return text
