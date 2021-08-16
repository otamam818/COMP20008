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
        
        # set of all accepted stopwords
        self.stopwords = set(stopwords.words('english'))
        
        # list of set of tokenized words filtered from stopwords
        self.__text_list = self.__get_text_sets()
        
        # useless words found throughout the text and their count
        self.useless = dict()
        
        # a list of dictionaries. Based on how many times each 
        # word repeated in given text body (based on index)
        self.__repeats_list = [] 

    def __get_text_sets(self):
        finlist = []
        texts = self.original
        for i in range(len(texts)):
            # make a set for each text and add 
            # their words (if it's not a stopword)
            finlist.append(set())
            for word in texts[i]:
                if not(word in self.stopwords):
                    finlist[i].add(word)
                
        return [set(word_tokenize(i)) for i in texts if not(i in self.stopwords)]

    def __get_repeats(self):
        # make a dictionary that counts the 
        finlist = []
        for i in self.original:
            finlist.append(dict())




def main():
    """Creates a Bag of Words for two inputs"""
    pass  

if __name__ == "__main__":
    main()
