#!/usr/bin/env python3

import argparse
import httpx
import concurrent.futures

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"}

def get_status(url):
    with httpx.Client(headers=headers,verify=False) as client:
    	try:
            r = client.get(f"https://{url}")
            print(f"[{r.status_code}] - {url}")
        except httpx.ConnectTimeout:
            print(f"[*] Hit timeout limit when connecting to {url}")
        except httpx.NetworkError:
            print(f"[*] A netword error occured when conntecting to {url}")
        except KeyboardInterrupt:
            print("[*] Stopping ...") 

    
def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", help="File of urls to check", required =True)
    parser.add_argument("-t", "--threads", help="Number of threads, default = 5",type=int, default=5)

    args = parser.parse_args()

    with open(args.input) as f:
        urls = [line.strip() for line in f.readlines()]

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(get_status, urls)     

if __name__ == "__main__":
	main()
