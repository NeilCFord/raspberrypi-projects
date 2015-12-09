#! /usr/bin/python

import explorerhat as eh
import time

eh.output.one.off()
time.sleep(0.5)

while True:
    eh.output.one.on()
    time.sleep(0.00001)
    eh.output.one.off()
    print eh.input.one.read()
    print eh.input.one.read()
    print "****"
    time.sleep(1)
