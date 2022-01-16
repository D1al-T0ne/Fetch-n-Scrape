#!/usr/bin/env python3

import argparse
import httpx
import jsbeautifier
import concurrent.futures
from hashlib import sha256

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"}

def get_js(url):
    with httpx.Client(headers=headers) as client:
        r = client.get(url)
        if r.status_code == 200:
            content = r.text
            js = jsbeautifier.beautify(content)
            hash = sha256(url.encode()).hexdigest()[:16]
            file_name = f"{hash}.js"
            with open(file_name, "w") as f:
                f.write(js)
            print(f"File found and saved at {file_name}")

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", help="File of JS links", required =True)
    parser.add_argument("-t", "--threads", help="Number of threads, default = 5", type=int, default=5)

    args = parser.parse_args()

    with open(args.input) as f:
        urls = [line.strip() for line in f.readlines()]

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(get_js, urls)     

if __name__ == "__main__":
    main()
