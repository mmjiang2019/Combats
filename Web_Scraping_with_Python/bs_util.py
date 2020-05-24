#!/usr/bin/env python3
# -*-encoding:utf-8-*-

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup as bsoup

'''
function used to get access to specifid url
'''
def getUrlCtx(url):
	try:
		html = urlopen(url)
	except (HTTPError, URLError) as e:
		print(e)
		print("Url %s couldn't be accessed")
		return None
	return html.read()

'''
function used to get the tag(s) contained in url content
params:
	
'''
def getUrlCtxTag(html_txt, tag, is_all):
	bsObj = bsoup(html_txt, "html.parser")
	try:
		if is_all == False:
			content = bsObj.find(tag)
		else:
			content = bsObj.find_all(tag)
	except AttributeError as e:
		# print(e)
		print ("%s couldn't be find in html_txt" %(tag))
		return None
	return content

def getCtx(url, tag, is_all):
	html_txt = getUrlCtx(url)
	# print(html_txt)
	if html_txt == None:
		return None
	else:
		ctx = getUrlCtxTag(html_txt, tag, is_all)
		if ctx == None:
			print("failed to get url tag(s)")
			return None
	return ctx


url = "http://www.baidu.com"
tag = "a"
print("test of getting the first tag in url content")
result = getCtx(url, tag, False)
print(result)
print("test of getting all the tags in url content")
result = getCtx(url, tag, True)
for item in result:
	print(item)
