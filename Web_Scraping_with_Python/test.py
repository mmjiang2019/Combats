#!/usr/bin/env python3
#-*-encoding: utf-8-*-
'''
Scripts used to test functions used
'''

import bs_util as util


print("====================test functions in bs_utl.py====================")
url = "http://www.baidu.com"
tag = "a"
print("++++++++++++++++++++test of getting the first tag in url content++++++++++++++++++++")
result = util.getCtx(url, tag, False)
print(result)
print("++++++++++++++++++++test of getting all the tags in url content++++++++++++++++++++")
result = util.getCtx(url, tag, True)
for item in result:
	print(item)
