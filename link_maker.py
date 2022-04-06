#!/usr/bin/env python

import argparse

def link_maker(filename):

    with open("links.html", "a") as f:
      with open(filename) as d:
        hosts = [line.strip() for line in d.readlines()]
        for host in hosts:
            f.write(f"<a href=https://{host}>{host}</a><br>")


def main():

    parser = argparse.ArgumentParser(description="Takes in a file of hostnames, \
                                     urls, or IPs and create an HTML page with \
                                     clickable links")

    parser.add_argument("-f", "--filename", metavar="", help="Input file be \
                        processed", required =True)

    args = parser.parse_args()

    link_maker(args.filename)

if __name__ == "__main__":
	main()
