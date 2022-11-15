# algo.py

from time import time

class Algo():
    def __init__(self, number, *args, **kwargs):
        self.number = number

    @timer
    def recur_fac(self):
        if self.number == 1:
            return self.number
        else:
            self.number -= 1
            result = self.number * self.recur_fac()
            return result

    def timer(func):
        def timing(*args, **kwargs):
            time_before = time.time()
            execution = func(*args, **kwargs)
            time_after = time.time()
            print('Time elapsed:', time_after - time_before)
            return execution

        return timing


if __name__ == '__main__':
    algo = Algo(6)
    print(algo.recur_fac())
