

class Split:
    def __init__(self):
        self.split = ' '


    def split_text(self, word, index, spaces):
        data = ''
        for item in word:
            if index == word.index(item):
                while spaces != 0:
                    new_item = item + self.split
                    spaces -= 1
                    self.split += ' '
                    data = new_item
        print(word[:index]+data+word[index+1:])



splited_text = Split()
splited_text.split_text("Manuels", 3, 4)