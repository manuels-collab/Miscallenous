

class StringMethod:
    def __init__(self):
        self.lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
                    , 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M','N','O','P', 'Q',
                      'R', 'S', 'T', 'U', 'V', 'W',' X', 'Y', 'Z']
        self.letters_index = []
        self.new_word = ''

    def transform(self, word):
        for item in word:
            if item in self.lower_case:
                for letters in self.lower_case:
                    if letters == item:
                        self.letters_index.append(self.lower_case.index(item))
                for indexes in self.letters_index:
                    self.new_word += self.upper_case[indexes]
            elif item in self.upper_case:
                for letters in self.upper_case:
                    if letters == item:
                        self.letters_index.append(self.upper_case.index(item))
                for indexes in self.letters_index:
                    self.new_word += self.lower_case[indexes]
        len_of_word = len(word)
        print(self.new_word[-len_of_word:])







manuels = StringMethod()
manuels.transform('manuels')


word = 'manuels'
