from random import randint
from class.py import Test()
x = 1

while x < 5:
    print(randint(1,99))
    x = x + 1

a = Test('TEST')

if __name__ == '__main__':
    a.print_text() 
