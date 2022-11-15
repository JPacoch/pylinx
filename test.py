from random import randint

from class_new import Test
from vars import MY_VARIABLE

x = 1

while x < 5:
    print(randint(1,99))
    x = x + 1

a = Test('TEST')

print(x + MY_VARIABLE)

if __name__ == '__main__':
    print(MY_VARIABLE)
    a.print_text()

