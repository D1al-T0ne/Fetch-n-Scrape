#!/usr/bin/env python

import subprocess
import sys

def gau_urls(domain):
	with open("gau-data.txt", "w") as gd:
		gau = subprocess.call(["gau", domain], stdout=gd)
		
def remove_duplicates():
	with open("gau-data.txt") as d:
			dlines = set(d)
			with open("gau-data.txt", "w") as results:
				for line in dlines:
					results.write(line)

def main():

	gau_urls(sys.argv[1])
	
	remove_duplicates()

if __name__ == "__main__":
	main()
