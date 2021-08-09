#!/usr/bin/env python

import subprocess


def gau_urls(domain):
	with open("gau-data.txt", "w") as gd:
		gau = subprocess.call(["gau", domain], stdout=gd)


def main():

	gau_urls()


if __name__ == "__main__"
	main()
