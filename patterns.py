#!/usr/bin/env python

import re

# Import pattern wordlist
with open("rce.txt") as r:
	patterns_list = [pattern.strip() for pattern in r]
	patterns = re.compile(r'\b(?:%s)\b' % '|'.join(patterns_list))


with open("raw-gau-data.txt") as g:
	lines = g.readlines()
	for line in lines:
		if re.search(patterns, line):
			print(line, end="")

#https://stackoverflow.com/questions/6750240/how-to-do-re-compile-with-a-list-in-python
#https://stackoverflow.com/questions/4785244/search-a-text-file-and-print-related-lines-in-python
