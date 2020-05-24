#!/usr/bin/env python3
#-*-encoding: utf-8-*-
'''
Scripts used to test functions used
'''

import bs_util as util
import re

print("====================test functions in bs_utl.py====================")
url = "http://www.baidu.com"
# pair = {"href" : "re.compile(\'^*/(baidu.com)/*$\')"}
pair = {"a" : None}
pair["href"] = re.compile(r'(.*)baidu(.*?) .*')
print("++++++++++++++++++++test of getting the first tag in url content++++++++++++++++++++")
result = util.getUrlLinks(url, False, **pair)
print(result)
print("++++++++++++++++++++test of getting all the tags in url content++++++++++++++++++++")
result = util.getUrlLinks(url, True, **pair)
for item in result:
	print(item)
