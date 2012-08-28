#!/usr/bin/env python
#-*- coding:utf-8 -*-

import math
import base64
import sys


def generate(text, length):
    new_text = text
    #times = int(math.ceil(math.log(length/len(text), 1.37)))
    
    while len(new_text) < length:
        new_text = base64.b64encode(new_text)
    
    print new_text
    print "[*] Generating Finished!!"
    print "Original text:", text
    print "Length: %d => %d" % (len(text), len(new_text))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        generate(sys.argv[1], int(sys.argv[2]))
    else:
        print "Usage: %s <ORGTEXT> <REQLENGTH>" % sys.argv[0]
        

