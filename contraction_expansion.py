import contractions

# run()
# parameters:
#   text : string - the string for which contractions should be expanded
# returns:
#   text : string - the string containing the modified text
# description:
#   This function uses the contractions package to expand contractions, and
#       to modify slang to its actual form
def run (text):
    text = contractions.fix(text)
    return text
