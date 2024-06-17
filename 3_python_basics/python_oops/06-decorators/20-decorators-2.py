#!/usr/bin/env python
import datetime


def my_decorator(inner):
    def inner_decorator():
        print(datetime.datetime.utcnow())
        inner()
        print(datetime.datetime.utcnow())

    return inner_decorator


@my_decorator
def decorated():
    print("This happened!")


if __name__ == "__main__":
    decorated()

# This will print: (NOTE: The time will change of course :P)
# # python 20-decorators-2.py
# 2016-05-29 11:46:07.444330
# This happened!
# 2016-05-29 11:46:07.444367
