#!/usr/bin/env python

import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

os.makedirs("screenshots",exist_ok=True)

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def screenshot(domain):
    filename = os.path.splitext(domain)[0]+".png" 
    driver.get(f"https://{domain}")
    driver.get_screenshot_as_file(f"./screenshots/{filename}")

def main():
	
	screenshot(sys.argv[1])
#with open("test.txt") as t:
#  urls = t.readlines()
#  for url in urls:
#    name = url.strip()
#    print(f"[+]{name} captured!")
if __name__ == "__main__":
	main()
