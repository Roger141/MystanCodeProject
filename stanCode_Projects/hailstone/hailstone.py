"""
File: hailstone.py
Name:Roger141
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

SECRET = 1
def main():
    """
    Computes and prints the hailstone sequence starting from a user-provided
    integer until it reaches 1.
    """
    print('This program computers the hailstone sequences')
    print('')
    n = int(input('Enter a number: '))
    while n != 1:
        if n % 2 == 1:
            print(str(n) + 'is odd,so I do 3n+1:'+str(3*n+1))
            n = 3*n+1
        else:
            n = n//2
            old_n = n*2
            print(str(old_n)+'is even,so I take half:'+str(n))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
