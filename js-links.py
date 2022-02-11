#!/usr/bin/env python

import argparse
import re
import sys

def js_links(filename):

	with open(filename) as f:
		urls = f.readlines()
		regex = re.compile('\.js$')
		jsurls = list(filter(regex.search, urls))
		with open("js-links.txt", "w") as js:
			[js.write(jsurl) for jsurl in jsurls]


def main():

    parser = argparse.ArgumentParser(description="Takes in a file of urls, \
                                     usually from the tool gau or wayback and \
                                     parses for JavaScript links placing them in a file.")

    parser.add_argument("-f", "--filename", metavar="", help="Input file to be \
                        processed", required =True)

    args = parser.parse_args()

    js_links(args.filename)

if __name__ == "__main__":
	main()
