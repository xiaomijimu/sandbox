import random,sys

def collatz(n):
	if (n%2 ==0):
		return n//2
	else:
		return 3*n+1

print("Enter number:")
try:
	n = int(input())
	while (n!=1):
		n = collatz(n)
		print (n)
except ValueError:
	print("please enter number, not string!")


