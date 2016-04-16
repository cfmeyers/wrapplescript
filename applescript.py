#!/usr/bin/python

import subprocess

# Note this file created by Dr. Drang, see post:
# http://www.leancrew.com/all-this/2013/03/combining-python-and-applescript/


def asrun(ascript):
    "Run the given AppleScript and return the standard output and error."

    osa = subprocess.Popen(['osascript', '-'],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE)
    return osa.communicate(ascript)[0]


def asquote(astr):
    "Return the AppleScript equivalent of the given string."
    astr = astr.replace('"', '" & quote & "')
    return '"{}"'.format(astr)
