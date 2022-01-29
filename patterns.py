#!/usr/bin/env python

import argparse
import re

def pattern(filename):
# Import pattern wordlist
    with open(f"./Patterns/{filename}") as r:
        patterns_list = [pattern.strip() for pattern in r]
        patterns = re.compile(r'\b(?:%s)\b' % '|'.join(patterns_list))
        return patterns

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", help="File of URLs to be parsed.", required =True)
    parser.add_argument("-p", "--pattern", help="Pattern to look for.", required =True)

    args = parser.parse_args()

    with open(args.input) as g:
        results = (line.strip() for line in g.readlines() if re.search(pattern(args.pattern), line))
        for result in results:
            print(result, sep="")

if __name__ == "__main__":
    main()
