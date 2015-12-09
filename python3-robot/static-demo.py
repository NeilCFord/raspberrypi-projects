#! /usr/bin/python

import explorerhat as eh
import time

eh.output.two.off()
time.sleep(0.5)

while True:
    eh.output.two.on()
    time.sleep(0.00001)
    eh.output.two.off()
    print eh.input.two.read()
    print eh.input.two.read()
    print "****"
    time.sleep(1)
