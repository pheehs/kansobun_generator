#!/usr/bin/env python
#-*- coding:utf-8 -*-

import math
import base64
import sys
import re

HAN_UPPER = re.compile(u"[A-Z]")
HAN_LOWER = re.compile(u"[a-z]")
HAN_NUM = re.compile(u"[0-9]")

def han2zen(word):
    word = HAN_UPPER.sub(lambda m: unichr(ord(u"Ａ") + ord(m.group(0)) - ord("A")), word)
    word = HAN_LOWER.sub(lambda m: unichr(ord(u"ａ") + ord(m.group(0)) - ord("a")), word)
    word = HAN_NUM.sub(lambda m: unichr(ord(u"０") + ord(m.group(0)) - ord("0")), word)
    return word

def generate(text, length, outfile):
    new_text = text
    #times = int(math.ceil(math.log(length/len(text), 1.37)))
    
    while len(new_text) < length:
        new_text = base64.b64encode(new_text)

    new_text = han2zen(unicode(new_text))

    print "[*] Generating Finished!!"    
    if outfile:
        print "[*]Writing to file <%s>" % outfile
        fd = open(outfile, "w")
        fd.write(new_text.encode("utf-8"))
        fd.close()
    else:
        print "Generated text:"
        print new_text

    print "Original text:", text
    print "Length: %d => %d" % (len(text), len(new_text))


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        if len(sys.argv) == 4:
            generate(sys.argv[1], int(sys.argv[2]), sys.argv[3])
        else:
            generate(sys.argv[1], int(sys.argv[2]), None)
    else:
        print "Usage: %s <ORGTEXT> <REQLENGTH> [<OUTPUTFILE>]" % sys.argv[0]
        

