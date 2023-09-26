#!/usr/bin/env python
# encapsulation-2.py

class MyClass(object):
    def set_val(self, val):
        self.value = val

    def get_val(self):
        print(self.value)
        return self.value



a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(1000)
a.value = 100  # <== Overriding `set_value` directly # <== ie..  Breaking encapsulation

a.get_val()
b.get_val()

print('DONE')