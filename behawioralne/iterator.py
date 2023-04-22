"""Iterator dla funkcji"""

import time


def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


g = fib()

# try:
#    for e in g:
#       print(e)
#       time.sleep(1)
#
# except KeyboardInterrupt:
#    print("Calculation stopped")


"""Iterator dla klasy"""


class NumberWheel:  # pylint: disable=too-few-public-methods
    "The concrete iterator (iterable)"

    def __init__(self):
        self.index = 0

    def __next__(self):
        """Return a new number next in the wheel"""

        self.index = self.index + 1
        if self.index > 50:
            raise StopIteration
        return self.index * 2

    def __iter__(self):
        return self


# The Client
NUMBERWHEEL = NumberWheel()

for i in NUMBERWHEEL:
    print(i, end=", ")
