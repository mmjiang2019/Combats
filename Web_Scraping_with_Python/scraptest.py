#!/usr/bin/env python

# urllib.request has been remove in python3
# We use urllib directly
from urllib import urlopen

html = urlopen("http://www.baidu.com/")
print(html.read())

