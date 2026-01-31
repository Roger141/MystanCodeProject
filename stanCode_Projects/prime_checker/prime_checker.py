"""
File: prime_checker.py
Name:Roger141
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100	 # Exit value.
def main():
	"""
	Continuously prompts the user for integers and reports whether each number is prime until EXIT is entered.
	"""
	print('Welcome to the prime checker')
	n = int(input('n: '))
	while n != EXIT:
		if is_prime(n):
			print(str(n) + ' is a prime number.')
		else:
			print(str(n) + ' is not a prime number.')
		n = int(input('n: '))
	print('Have a good one!')

def is_prime(n):
	"""
	1 is not a prime number.
	"""
	if n <=1:
		return False
	i = 2
	while i*i <= n:
		if n % i ==0:
			return False
		i +=1
	return True



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
