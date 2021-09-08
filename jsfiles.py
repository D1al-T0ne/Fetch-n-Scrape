#!/usr/bin/env python

import re
import sys

def jsfiles(fileName):

	with open(fileName) as f:
		urls = f.readlines()
		regex = re.compile('\.js$')
		jsurls = list(filter(regex.search, urls))
		with open("js-links.txt", "w") as js:
			[js.write(jsurl) for jsurl in jsurls]

def main():
	
	jsfiles("gau-data.txt")

if __name__ == "__main__":
	main()
