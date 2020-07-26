import helpers
import dataset as ds
import unicodedata
import contractions
import re
from nltk.corpus import stopwords
import pandas as pd

stop_words = set(stopwords.words('english'))

# lowercase_conversion()
# parameters:
#   text : string - the text to be converted to lowercase
# returns:
#   text : string - the lowercase text
# description:
#   This function converts a given piece of text to lowercase and returns it.
def lowercase_conversion (text):
    text = text.lower()
    return text

# remove_accents()
# parameters:
#   text : string - the text for which accents will be removed
# returns:
#   text : string - the text, without accents
# description:
#   This function removes accents from a given piece of text and returns the
#       text.
def remove_accents(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

# remove_usernames()
# parameters:
#   text : string - the text to remove the usernames from
# returns:
#   new_text : string - the text with usernames removed
# description:
#   This function removes usernames (prefixed with @) from the text and returns
#       the modified text.
def remove_usernames (text):
    text = text.split()
    new_text = []
    for word in text:
        if '@' not in word:
            new_text.append(word)
    new_text = " ".join(new_text)
    return new_text

# transform_hashtags()
# parameters:
#   text : string - the text containing hashtags for transformation
# returns:
#   new_text : string - the text with hashtags as ordinary words
# description:
#   This function removed the '#' symbol from hashtags and retains the text of
#       the hashtag.
def transform_hashtags (text):
    text = text.split()
    new_text = []
    for word in text:
        if '#' not in word:
            new_text.append(word)
        else:
            word = re.sub(r'#', '', word)
            new_text.append(word)
    new_text = " ".join(new_text)
    return new_text

# remove_urls()
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
def remove_urls (text):
    new_text = []
    text = text.split()
    for word in text:
        if '//t.co' not in word:
            new_text.append(word)
    new_text = " ".join(new_text)
    return new_text

# contraction_expansion()
# parameters:
#   text : string - the string for which contractions should be expanded
# returns:
#   text : string - the string containing the modified text
# description:
#   This function uses the contractions package to expand contractions, and
#       to modify slang to its actual form
def contraction_expansion (text):
    text = contractions.fix(text)
    return text

# remove_special_chars()
# parameters:
#   text : string - the text to be checked and modified
# returns:
#   text : string - the modified text
# description:
#   This function checks a given piece of text for a given set of special
#       characters, and removes them, returning the given text.
def remove_special_chars (text):
    special_chars_list = [['"'],
                          ["'"],
                          ['.', '\.'],
                          ['!'],
                          ['?', '\?'],
                          [','],
                          ['-'],
                          ['&amp;', '\&amp;'],
                          ['rt'],
                          ['&gt;', '\&gt;'],
                          ['&lt;', '\&lt;'],
                          ['&', '\&'],
                          ['\n', '\\n'],
                          ['$', '\$'],
                          [':', ':']]
    for special_char in special_chars_list:
        if special_char[0] in text:
            text = re.sub(special_char[-1], ' ', text)
    return text

# remove_stopwords
# parameters:
#   text : string - the text for which stopwords should be removed
# returns:
#   new_text : string - the text without stopwords
# description:
#   This function removes stopwords from text using NLTK's stopwords corpus.
#       The remaining text is returned.
def remove_stopwords (text):
    global stop_words
    text = text.split()
    new_text = []
    for word in text:
        if word not in stop_words:
            new_text.append(word)
    new_text = " ".join(new_text)
    return new_text


# load generic and specific datasets and merge them together
dfs = []
for df in ds.all_datasets:
    dfs.append(helpers.load_dataset(ds.dataset + df))
dfs = pd.concat(dfs, ignore_index=True)

# loop over dataframe, perform preprocessing on the tweet text
for index, row in dfs.iterrows():
    tweet_text = row.tweet_text
    tweet_text = lowercase_conversion(tweet_text)
    tweet_text = remove_accents(tweet_text)
    tweet_text = remove_usernames(tweet_text)
    tweet_text = transform_hashtags(tweet_text)
    tweet_text = remove_urls(tweet_text)
    tweet_text = contraction_expansion(tweet_text)
    tweet_text = remove_special_chars(tweet_text)
    tweet_text = remove_stopwords(tweet_text)
    dfs.tweet_text.at[index] = tweet_text

# Store processed data
helpers.dataframe_to_csv(dfs, ds.output_data + 'preprocessed_data.csv')

# print complete message
print('Preprocessing complete')
