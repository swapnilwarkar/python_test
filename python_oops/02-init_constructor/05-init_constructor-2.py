#!/usr/bin/env python
# 05-init_constructor-2.py

class MyNum(object):
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.value = value

    def increment(self):
        self.value = self.value + 1
        print(self.value)


a = MyNum(10)
a.increment()  # This should print 11
a.increment()  # This should print 12
