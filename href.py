#!/usr/bin/env python

with open("test.html", "w") as f:
  f.write("<title>Generated test html</title>")
  f.write("<h2>Report for Test</h2>")
  with open("test.txt") as t:
    urls = t.readlines()
    for url in urls:
      name = url.strip()
      filename = name.replace(".com","")
      f.write(f"<a href=https://{url}>{url}</a><br>")
