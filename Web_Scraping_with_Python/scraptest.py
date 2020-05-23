#!/usr/bin/env python3
#coding: utf-8
# urllib.request has been remove in python3
# We use urllib directly

# from urllib import urlopen
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

# handle exception when urlopen fails
try:
	html = urlopen("http://www.baidu.com/")
	# html = urlopen("http://mengmajiang.com/")
except URLError as e:
	print(e)
	'''
    you can do something here as below:
	1). break the function
	2). return null
	3). execute some other funcs 
	'''
	# break
	# return
	# ...
except HTTPError as e:
	print(e)
	# same as the last exception
else:
	'''
	continue the function in this section
	'''
	# print(html.read())
	bsObj = BeautifulSoup(html.read(), features="html.parser")


	# Print the first element which beautiful soup find
	print(bsObj.head)
	print(bsObj.span)
	print(bsObj.script)

	# Print the node of specified element
	print(bsObj.head.script)
	print(bsObj.body.div)

