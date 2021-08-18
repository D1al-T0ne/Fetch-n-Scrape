#!/usr/bin/env python3

import requests

def statusCode(url):
	
	headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"}

	try:
		r = requests.head(url, headers=headers)
		return(r.status_code, url)
	except requests.ConnectionError:
		pass

def main():

	print(statusCode("https://hackycorp.com"))

if __name__ == "__main__":
	main()

