# algo.py

import time

class Algo():
    def __init__(self, number, text, *args, **kwargs):
        self.number = number
        self.text = text

    def timer(func):
        def timing(*args, **kwargs):
            time_before = time.time()
            execution = func(*args, **kwargs)
            time_after = time.time()
            print('Time elapsed:', time_after - time_before)
            return execution

        return timing

    def recur_fac(self):
        if self.number == 1:
            return self.number
        else:
            self.number -= 1
            result = self.number * self.recur_fac()
            return result

    @timer
    def permute_string(self, text='', pocket=''):
        text = self.text
        if len(self.text) == 0:
            print('0 lenght string')
        else:
            for i in range(len(self.text)):
                letter = self.text[i]
                front = self.text[0:i]
                back = self.text[i+1:]
                merge = front + back
                return self.permute_string(merge, letter + '')

if __name__ == '__main__':
    algo = Algo(6, 'Jakub', 4213)
    print(algo.permute_string())



