# NLTK library
# for getting all accepted stopwords
from nltk.corpus import stopwords
#adding custom stopwords
from string import punctuation as __punctuations
my_stopwords = set(stopwords.words('english'))
my_stopwords.add("n't")
for punctuation_mark in __punctuations:
    my_stopwords.add(punctuation_mark)

# for getting a tokenizer function
from nltk.tokenize import word_tokenize
from re import split, findall

# Pandas - imported to create the appropriate dataframe
import pandas as pd

# Constants
from typing import Final
NUMBER: Final[str] = "#num#"
