#!/usr/bin/env python

import argparse

def link_maker(filename):

    with open("links.html", "a") as f:
      with open(filename) as d:
        subs = [line.strip() for line in d.readlines()]
        for sub in subs:
            f.write(f"<a href=https://{sub}>{sub}</a><br>")


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--filename", help="Input file containing hostnames to process", required =True)

    args = parser.parse_args()

    link_maker(args.filename)

if __name__ == "__main__":
	main()
