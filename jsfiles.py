#!/usr/bin/env python

import re


def jsfiles():

	with open("raw-gau-data.txt") as f:
		urls = f.readlines()
		regex = re.compile('\.js$')
		jsurls = list(filter(regex.search, urls))
		return(jsurls)

def main():
	
	with open ("python-js-links.txt", "w") as w:
		links = w.writelines(jsfiles())

if __name__ == "__main__":
	main()
