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
def getUrlCtxTag(html_txt, is_all, **pairs):
	bsObj = bsoup(html_txt, "html.parser")
	try:
		if is_all == False:
			for tag, attr in pairs.items():
				content = bsObj.find(tag, attr)
		else:
			for tag, attr in pairs.items():
				content = bsObj.find_all(tag, attr)
	except AttributeError as e:
		# print(e)
		print ("%s with atrribute %s couldn't be find in html_txt" %(tag, attr))
		return None
	return content

def getCtx(url, is_all, **pairs):
	html_txt = getUrlCtx(url)
	# print(html_txt)
	if html_txt == None:
		return None
	ctx = getUrlCtxTag(html_txt, is_all, **pairs)
	if ctx == None:
		print("failed to get url tag(s)")
		return None
	return ctx

def getUrlLinks(url, is_all, **pairs):
	ctx = getCtx(url, is_all, **pairs)
	if ctx == None:
		return None
	return ctx

