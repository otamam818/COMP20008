# What we need: a place to store 2 inputs, a prompt and manager
# A place to store the original words, set of stemmed words, dataframe
# unique words (useful), unique words (useful+useless)
from head import *

class BOW:
    def __init__(self, texts) -> None:
        """ 
        \nCarries out the Bag of Words Algorithm to large sets of text
        \ntexts: an iterable of strings. Each string carries a set of words/sentences"""
        # The originally input text file
        self.original = texts
        self.__text_list = []
        for i in texts:
            self.__text_list.append(set(word_tokenize(i)))
        # set of all accepted stopwords
        self.stopwords = set(stopwords.words('english'))



def main():
    """Creates a Bag of Words for two inputs"""
    pass  

if __name__ == "__main__":
    main()
