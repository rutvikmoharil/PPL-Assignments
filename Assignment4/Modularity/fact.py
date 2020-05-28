#Factorial module

def factorial(n):
	fact = 1
	if n < 0:
		print("factorial of negative number does not exist")

	else:
		for i in range(1,n + 1):
			fact = fact * i
		print(f"Factorial of {n} is {fact}")
	
#n = int(input("Enter number"))

if __name__ == "__main__":
	import sys
	factorial(int(sys.argv[1]))

