# What we need: a place to store 2 inputs, a prompt and manager
# A place to store the original words, set of stemmed words, dataframe
# unique words (useful), unique words (useful+useless)
from nltk.data import find
from head import *

class BOW:
    def __init__(self, texts) -> None:
        """ 
        \nCarries out the Bag of Words Algorithm to large sets of text
        \ntexts: an iterable of strings. Each string carries a set of words/sentences
        """
        # The originally input text file
        self.original = texts
        
        # set of all accepted stopwords + extras
        self.stopwords = my_stopwords
        
        # useless words found throughout the text and their count
        self.useless = dict()

        # list of set of tokenized words filtered from stopwords
        self.__text_list = self.__get_text_sets()
        
        
        # a list of dictionaries. Based on how many times each 
        # word repeated in given text body (based on index)
        self.__repeats_list = self.__get_repeats()

        self.total_repeats = self.__get_total_repeats()

    def __get_text_sets(self) -> list:
        finlist = []
        texts = self.original

        for i in range(len(texts)):
            # make a set for each text and add 
            # their words (if it's not a stopword)
            finlist.append(set())
            for word in word_tokenize(texts[i]):
                word = "".join(split("'\w*", word.casefold()))
                valid_word = not(word in self.stopwords)
                if valid_word:
                    finlist[i].add(word.casefold())
                else:
                    if word in self.useless:
                        self.useless[word] += 1
                    else:
                        self.useless[word] = 1
                
        print(f"finlist is {finlist}")
        return finlist

    def __get_repeats(self) -> list:
        # make a dictionary that counts the words and 
        # adds them if it's in the set
        finlist = []
        tokenized_wordset = self.__text_list
        for i in range(len(self.original)):
            finlist.append(dict())
            print(f"Now working on: {word_tokenize(self.original[i])}\n\n")
            for word in word_tokenize(self.original[i]):
                self.__append_accordingly(finlist, tokenized_wordset, 
                                          i, word.casefold())
        return finlist

    @staticmethod
    def __append_accordingly(finlist, tokenized_wordset, index, word) -> None:
        if word in tokenized_wordset[index]:
            if word in set(finlist[index]):
                finlist[index][word] += 1
            else:
                finlist[index][word] = 1

    def get_repeats(self, index) -> dict:
        return self.__repeats_list[index]

    def __get_total_repeats(self) -> dict:
        fin_dict = dict()
        for wordset in self.__repeats_list:
            for word in set(wordset):
                if word in fin_dict:
                    fin_dict[word] += wordset[word]
                else:
                    fin_dict[word] = wordset[word]
        return fin_dict

def test():
    """Method used for testing implemented class"""
    texts = ["Gaara of the Sand didn't die", "Naruto - Gaara's best friend"]
    # print("Enter text then press ENTER to enter another text")
    # print("Press CTRL+C to exit once you are done pressing ENTER")
    try:
        raise KeyboardInterrupt
        # while True:
        #     texts.append(input())
    except KeyboardInterrupt:
        bow1 = BOW(texts)
        print(f"\nOriginal text:\n{bow1.original}"                + '\n')
        print(f"\nStopwords:\n{bow1.stopwords}"                   + '\n')
        print(f"\nUseless words found:\n{bow1.useless}"           + '\n')
        print(f"\nFirst text  (tokenized): {bow1.get_repeats(0)}" + '\n')
        print(f"\nSecond text (tokenized): {bow1.get_repeats(1)}" + '\n')
        print(f"Total repeats: {bow1.total_repeats}"              + '\n')

if __name__ == "__main__":
    test()
