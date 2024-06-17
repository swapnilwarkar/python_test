#!/usr/bin/env python
# 04-init_constructor.py

class MyNum(object):
    def __init__(self):
        print("\nCalling the __init__() constructor!\n")
        self.val = 0

    def increment(self):
        self.val = self.val + 1
        print(self.val)


dd = MyNum()
dd.increment()  # will print 1
dd.increment()  # will print 2

print('DONE')