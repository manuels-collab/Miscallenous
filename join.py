

class Join:
    def __init__(self):
        self.join_method = ''

    def join_text(self, word, string):
        for item in word:
            if item == ' ':
                print(word.index(item))



text = Join()
text.join_text('manu els', '#')