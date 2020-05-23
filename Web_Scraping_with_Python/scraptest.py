#!/usr/bin/env python3
#coding: utf-8
# urllib.request has been remove in python3
# We use urllib directly

# from urllib import urlopen
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

def getWebContent(url, tag):
	'''
	handle exception when failing opening url
	'''
	try:
		html = urlopen(url)
	except (HTTPError, URLError) as e:
		print("Http/Url error opending %s" %(url))
		return None
	'''
	handle exception when extracting tag
	'''
	# note that text in html could only be get via read() one time
	html_txt = html.read()
	try: 
		bsObj = BeautifulSoup(html_txt, "html.parser")
		'''
		note:
		1). find("key"): 
			returns the first element which is matched in beautiful soup object
		2). find_all("key"):
			returns all the elements matched in a list
		'''
		content = bsObj.find(tag)
	except AttributeError as e:
		print('%s is not found in %s' %(tag, url))
		return None
	return content


'''
test functions of getting expected tag from url
'''
url = "http://www.baidu.com"
tag = "span"
ctx = getWebContent(url, tag)
if ctx != None:
	print(ctx)
else:
	print("fail to find %s in %s."%(tag, url))


url = "http://12mkasdawsc.com.cn"
tag = "body"
ctx = getWebContent(url, tag)
if ctx != None:
	print(ctx)
else:
	print("fail to find %s in %s."%(tag, url))
