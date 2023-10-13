#!/usr/bin/python3.6
import sys
import logging
import os

import parse_wav
import class_ops
import timer_decorator
import class_plus_decorators

#log = logging.getLogger()
#log.setLevel(logging.DEBUG)

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('')

input_file1 = 'sample1.wav'
input_file2 = 'sample2.wav'
output_directory = 'output'

#time python3 argv1 argv2 argv3
if __name__ == '__main__':
    #input_file1 = sys.argv[1]
    #input_file2 = sys.argv[2]
    #output_file = sys.argv[3]

    if not os.path.isfile(input_file1):
        log.error('arg input file does not exist...')
        exit(-1)
    elif not os.path.isfile(input_file2):
        log.error('arg config file does not exist...')
        exit(-1)
    elif not os.path.isdir(output_directory):
        log.error('arg output dir does not exist...')
        exit(-1)

    log.info(
        '\nInput file1: {}\nInput file2: {}\nOutput_directory: {}\n'
          .format(input_file1, input_file2, output_directory))

    #Default/Normal method calling from another .py file
    #parse_wav.parse_wav_file(input_file1)

    # Decorator method calling from another .py file
    #timer_decorator.parse_wav_file(input_file1)

    # Use of class and object for calling the Default/Normal method calling from another .py file
    #myclass_object = class_ops.myclass(input_file1)
    #myclass_object.set_filename(input_file1)
    #myclass_object.get_filename()
    #myclass_object.parse_wav_method()

    # Use of class and object for calling the decorator method calling from another .py file
    myclass_object = class_plus_decorators.myclass(input_file1)
    myclass_object.set_filename(input_file1)
    myclass_object.get_filename()
    myclass_object.parse_wav_method()
