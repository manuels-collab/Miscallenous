



class Title:
    def __init__(self):
        self.lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
                    , 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M','N','O','P', 'Q',
                      'R', 'S', 'T', 'U', 'V', 'W',' X', 'Y', 'Z']

    def create_title(self, word):
        first_letter = word[0]
        letter_index = 0
        for item in self.lower_case_letters:
            if item == first_letter:
                letter_index += self.lower_case_letters.index(item)
                for item in self.upper_case_letters:
                    if self.upper_case_letters.index(item) == letter_index:
                        data = item
                        print(data+word[1:])


tile= Title()
tile.create_title("peach")