# NLTK library
# for getting all accepted stopwords
from nltk.corpus import stopwords
#adding custom stopwords
my_stopwords = set(stopwords.words('english'))
my_stopwords.add("n't")

# for getting a tokenizer function
from nltk.tokenize import word_tokenize
from re import split, findall

# Pandas - imported to create the appropriate dataframe
import pandas as pd

# Constants
from typing import Final
NUMBER: Final[str] = "#num#"
