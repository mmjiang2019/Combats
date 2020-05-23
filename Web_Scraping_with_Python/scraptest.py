#!/usr/bin/env python3
#coding: utf-8
# urllib.request has been remove in python3
# We use urllib directly

# from urllib import urlopen
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.baidu.com/")
bsObj = BeautifulSoup(html.read(), features="html.parser")

# print(html.read())

# Print the first element which beautiful soup find
print(bsObj.head)
print(bsObj.span)
print(bsObj.script)

# Print the node of specified element
print(bsObj.head.script)
print(bsObj.body.div)

