 <h1>Nuclear Deal Tweet Preprocessing</h1>
<!-- <hr style="margin:10px 0;padding:0;"/> -->

This code is part of the research project titled "Iranian State-Sponsored Propaganda on Twitter: Exploring Methods for Automatic Classification and Analysis".

The results are published in a paper titled "Sentiment and Objectivity in Iranian State-Sponsored Propaganda on Twitter" in IEEE Transactions on Computational Social Systems at [doi.org/10.1109/TCSS.2023.3273729](https://doi.org/10.1109/TCSS.2023.3273729)

<h3>Project</h3>
<hr style="margin:10px 0;padding:0;"/>

This project aims to label Iranian state-sponsored propaganda for sentiment and emotion using automated methods. Additionally, this project will evaluate various machine learning algorithms performance for correctly classifying sentiment and emotion contained in the text based on the automated labelling.


<h3>About</h3>
<hr style="margin:10px 0;padding:0;"/>

This code is used to preprocess twitter data. This code will:
* Convert text to lowercase
* Remove accents from letters
* Remove usernames
* Remove the `#` symbol from hashtags
* Remove URL's
* Expand contractions and convert slang
* Remove special characters, punctuation, reserved words and HTML markup
* Remove stopwords

<h3>Prerequisites</h3>
<hr style="margin:10px 0;padding:0;"/>

**Note:** it is recommended that you create a virtual environment (this code was created for Python 3.6):

    mkvirtualenv --python=/usr/bin/python3.6 preprocessing
    workon preprocessing


To install the required dependencies:

    pip install -r requirements.txt

To install NLTK stopwords:

    python nltk_downloader.py
When the dialog box appears, click `all packages` and scroll down to `stopwords`. Then click `download` and once complete, close the dialog.

Copy `dataset.py.example` to `dataset.py`

    cp dataset.py.example dataset.py

in `dataset.py`:
- Add the absolute path to the `dataset` variable (folder containing the extracted nuclear deal dataset files)
  - e.g. `/home/USER/nuclear_deal_tweet_extraction/data/`
- Add an absolute path to the `output_data` variable for storing output data
  - e.g. `/home/USER/nuclear_deal_tweet_extraction/output_data/`

<h3>Requirements</h3>
<hr style="margin:10px 0;padding:0;"/>

The requirements for this code to run are detailed in `requirements.txt`.

<h3>Execution</h3>
<hr style="margin:10px 0;padding:0;"/>

- Within the Python virtual environment, run:
`python preprocessing.py`
