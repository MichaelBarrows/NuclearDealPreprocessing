# run()
# parameters:
#   text : string - the string the URL's will be removed from
#   urls : list - list of URL's for removal
# returns:
#   new_text : string - the modified text
# description:
#   This function splits a string into each individual word, and loops over the
#       list of words. Each word is checked to see if it is present in the list
#       of URL's. If it is not present, it is added to a list which is then
#       converted to a string and returned.
def run (text, urls):
    new_text = []
    text = text.split()
    for word in text:
        if word not in urls:
            new_text.append(word)
    new_text = " ".join(new_text)
    return new_text
