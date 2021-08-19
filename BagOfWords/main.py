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

        # a dictionary counting the total 
        # number of repeats of all words inserted
        self.total_repeats = self.__get_total_repeats()

        # a dictionary of all dataframes
        # self.__dataframe["all"] returns the total repeats dataframe
        self.__dataframe = None

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
                    if self.__has_digit(word):
                        finlist[i].add(NUMBER)    
                    else:
                        finlist[i].add(word.casefold())
                else:
                    if word in self.useless:
                        self.useless[word] += 1
                    else:
                        self.useless[word] = 1
                
        print(f"finlist is {finlist}")
        return finlist

    @staticmethod
    def __has_digit(aStr):
        """Checks if the given string has a digit in it"""
        return len(findall("\d+", aStr)) != 0

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
        finset = set(finlist[index])
        if word in tokenized_wordset[index]:
            if word in finset:
                finlist[index][word] += 1
            else:
                finlist[index][word] = 1
        elif BOW.__has_digit(word):
            if NUMBER in finset:
                finlist[index][NUMBER] += 1
            else:   
                finlist[index][NUMBER]  = 1

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

    def __get_dataframe(self): pass


def test():
    """Method used for testing implemented class"""
    texts = ["Talk 31, talk", "Are you the 100th monkey?"]
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
