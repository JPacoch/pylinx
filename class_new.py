class Test():
    def __init__(self, text):
        self.text = text

    def print_text(self):
        print(self.text)

if __name__ == "__main__":
    test = Test('test')
    test.print_text()
