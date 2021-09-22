#!/usr/bin/env python

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

os.makedirs("screenshots",exist_ok=True)

chrome_options = Options()
chrome_options.add_argumetn("--headless")
driver = webdriver.Chrome(options=chrome_options)

with open("test.txt") as t:
  urls = t.readlines()
  for url in urls:
    name = url.strip()
    filename = name.replace(".com","")
    driver.get(f"https://{url}")
    driver.get_screenshot_as_file(f"./screenshots/{filename}.png")
    print(f"[+]{name} captured!")
