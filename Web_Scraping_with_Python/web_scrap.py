#!/usr/bin/env python3

import datetime
import random
import re
import bs_util as utl

random.seed(datetime.datetime.now())

def getLinks(url):
	tag = "a"
	attr = {"id"} 
	links = bs_utl.getUrlCtx(url, )
