#!/usr/bin/env python3

import sys
import dns.resolver

def get_cname(hostname):
	found = {}
	result = list()
	result.append(hostname)
	try:
		for rdata in dns.resolver.resolve(hostname, "CNAME"):
			result.append(rdata.target)
	except:
		pass
	if len(result) == 1:
		try:
			A = dns.resolver.resolve(hostname, "A")
			if len(A) > 0:
				result = list()
				result.append(hostname)
				result.append(str(A[0]))
		except:
			pass
	if len(result) > 1:
		if str(result[1]) in found:
			if found[str(result[1])] > 3:
				return
			else:
				found[str(result[1])] = found[str(result[1])] + 1
		else:
			found[str(result[1])] = 1				

		print(result)
		print(str(result[0]) + ":" + str(result[1]) + "\n")

def main():

	get_cname(sys.argv[1])

if __name__ == "__main__":
	main()
