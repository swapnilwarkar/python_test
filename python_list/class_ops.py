#!/usr/bin/env python
# 03-encapsulation-3.py

import struct

class myclass(object):
    def __init__(self, filename):
        self.filename = filename

    def get_filename(self):
        return print(self.filename)

    def set_filename(self, filename):
        self.filename = filename

