#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys

def fizzbuzz(max_num):
	for i in range(1, max_num + 1):
		if i % 15 == 0:
			print "Fizz Buzz"
		elif i % 3 == 0:
			print "Fizz"
		elif i % 5 == 0:
			print "Buzz"
		else:
			print str(i)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Usage: python fizzbuzz.py [max_num]"
		sys.exit()
	max_num = int(sys.argv[1])
	fizzbuzz(max_num)