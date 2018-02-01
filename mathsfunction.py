"""
Author: Doddahulugappa B

This python library contains some useful functions to deal with prime numbers and whole numbers.

usage:python mathsfunction.py

isPrime(number)
getPrimesBetween(pNumber1, pNumber2) 
gcd(number1, number2)  // greatest common divisor
getDivisors(number)    // all divisors of 'number' inclusive 1, number
isPerfectNumber(number)
simplifyFraction(numerator, denominator)
factorial (n) // n!
fibonacci(n) // calculate the n-th fibonacci term.
"""
import sys
import math

def fibonacci(n):
    """
        input: positive integer 'n'
        returns the n-th fibonacci term , indexing by 0
    """     
    # precondition
    assert isinstance(n, int) and (n >= 0), "'n' must been an int and >= 0"    
    tmp = 0
    fib1 = 1
    ans = 1 # this will be return    
    for i in range(n-1):        
        tmp = ans
        ans += fib1
        fib1 = tmp        
    return ans
# ------------------------------------------	

def isPrime(number):
    """
        input: positive integer 'number'
        returns true if 'number' is prime otherwise false.
    """
    # precondition
    assert isinstance(number,int) and (number >= 0) , \
    "'number' must been an int and positive"    
    status = True    
    # 0 and 1 are none primes. 
    if number <= 1:
        status = False    
    for divisor in range(2,int(round(math.sqrt(number)))+1):           
        if number % divisor == 0: # if 'number' divisible by 'divisor' then sets 'status' false and breaks up the loop. 
            status = False
            break    
    # precondition
    assert isinstance(status,bool), "'status' must be of type bool"      
    return status
# ------------------------------------------

def gcd(number1,number2):
    """
        Greatest common divisor
        input: two positive integer 'number1' and 'number2'
        returns the greatest common divisor of 'number1' and 'number2'
    """    
    # precondition
    assert isinstance(number1,int) and isinstance(number2,int) \
    and (number1 >= 0) and (number2 >= 0), \
    "'number1' and 'number2' must be positive integers."
    rest = 0    
    while number2 != 0:        
        rest = number1 % number2
        number1 = number2
        number2 = rest
    # precondition
    assert isinstance(number1,int) and (number1 >= 0), \
    "'number' must be of type int and positive"       
    return number1    
# ----------------------------------------------------

def getPrimesBetween(pNumber1, pNumber2):
    """
        input: prime numbers 'pNumber1' and 'pNumber2'and pNumber1 < pNumber2
        returns a list of all prime numbers between 'pNumber1' (exclusive) and 'pNumber2' (exclusive) 
    """    
    # precondition
    assert isPrime(pNumber1) and isPrime(pNumber2) and (pNumber1 < pNumber2), \
    "The arguments must be prime numbers and 'pNumber1' < 'pNumber2'"    
    number = pNumber1 + 1 # jump to the next number    
    ans = [] # this list will be returns.    
    while not isPrime(number): # if number is not prime then fetch the next prime number. 
        number += 1    
    while number < pNumber2:        
        ans.append(number)        
        number += 1        
        while not isPrime(number): # fetch the next prime number. 
            number += 1            
    # precondition
    assert isinstance(ans,list) and ans[0] != pNumber1 \
    and ans[len(ans)-1] != pNumber2, \
    "'ans' must be a list without the arguments"            
    return ans    
# ----------------------------------------------------

def getDivisors(n):
    """
        input: positive integer 'n' >= 1
        returns all divisors of n (inclusive 1 and 'n')
    """    
    # precondition
    assert isinstance(n,int) and (n >= 1), "'n' must be int and >= 1"       
    ans = [] # will be returned.    
    for divisor in range(1,n+1):        
        if n % divisor == 0:
            ans.append(divisor)       
    #precondition
    assert ans[0] == 1 and ans[len(ans)-1] == n, \
    "Error in function getDivisiors(...)"     
    return ans
# ----------------------------------------------------

def isPerfectNumber(number):
    """
        input: positive integer 'number' > 1
        returns true if 'number' is a perfect number otherwise false.
    """    
    # precondition
    assert isinstance(number,int) and (number > 1), \
    "'number' must been an int and >= 1"    
    divisors = getDivisors(number) 
    # precondition
    assert isinstance(divisors,list) and(divisors[0] == 1) and  \
    (divisors[len(divisors)-1] == number), \
    "Error in help-function getDivisiors(...)"     
    return sum(divisors[:-1]) == number # summed all divisors up to 'number' (exclusive), hence [:-1]
# ------------------------------------------------------------

def simplifyFraction(numerator, denominator):
    """
        input: two integer 'numerator' and 'denominator'
        assumes: 'denominator' != 0
        returns: a tuple with simplify numerator and denominator.
    """    
    # precondition
    assert isinstance(numerator, int) and isinstance(denominator,int) \
    and (denominator != 0), \
    "The arguments must be of type int and 'denominator' != 0"    
    gcdOfFraction = gcd(abs(numerator), abs(denominator)) # build the greatest common divisor of numerator and denominator.
    # precondition
    assert isinstance(gcdOfFraction, int) and (numerator % gcdOfFraction == 0) \
    and (denominator % gcdOfFraction == 0), \
    "Error in function gcd(...,...)"    
    return (numerator // gcdOfFraction, denominator // gcdOfFraction)    
# -----------------------------------------------------------------
    
def factorial(n):
    """
        input: positive integer 'n'
        returns the factorial of 'n' (n!)
    """    
    # precondition
    assert isinstance(n,int) and (n >= 0), "'n' must be a int and >= 0"    
    ans = 1 # this will be return.    
    for factor in range(1,n+1):
        ans *= factor    
    return ans    
# -------------------------------------------------------------------

def read_choice(choice):
	"""Read Choice and perform accordingly"""	
	if choice==9:
		print("***********Thank You*************")
		sys.exit(0)
		return False
	elif choice==1:
		try:
			number=int(raw_input("Enter Positive Integer Number: "))
			print("%d Th Fibonacci Number is: %d" % (number,fibonacci(number)))
		except Exception as e:
			print(e)
		return True
	elif choice==2:
		try:
			number=int(raw_input("Enter the Number: "))
			print("Factorial of %d is: %d" %(number,factorial(number)))
		except Exception as e:
			print(e)
		return True
	elif choice==3:
		try:
			number=raw_input("Enter two numbers with / symbol in bewteen(Eg.100/80): ")
			number=number.split("/")
			result=simplifyFraction(int(number[0]),int(number[1]))
			print("Simplified Fraction is: %d/%d" %(result[0],result[1]))
		except Exception as e:
			print(e)
		return True
	elif choice==4:
		try:
			number=int(raw_input("Enter Positive Number: "))
			print("%d is Perfect number? %s" % (number,isPerfectNumber(number)))
		except Exception as e:
			print(e)
		return True
	elif choice==5:
		try:
			number=int(raw_input("Enter Positive Number: "))
			print("%d is prime? %s" % (number,isPrime(number)))
		except Exception as e:
			print(e)
		return True
	elif choice==6:
		try:
			number=int(raw_input("Enter Positive Number: "))
			print("Divisors of %d are: %s" %(number,getDivisors(number)))
		except Exception as e:
			print(e)
		return True
	elif choice==7:
		try:
			number=raw_input("Enter 2 Prime  Numbers with 1 space between them: ")
			number=number.split(" ")
			print("Prime Numbers between %d and %d are: %s"%(int(number[0]),int(number[1]),getPrimesBetween(int(number[0]),int(number[1]))))
		except:
			print("Value error\n Please Enter 2 Prime  Numbers with 1 space between them: ")
		return True
	elif choice==8:
		try:
			number=raw_input("Enter 2 Positive Numbers with 1 space between them: ")
			number=number.split(" ")
			print("GCD of %d and %d is: %d " % (int(number[0]),int(number[1]),gcd(int(number[0]),int(number[1]))))
		except Exception as e:
			print(e)
		return True 
	else:		
		print("Invalid Choice,Please enter choice 1-9")
		return True    

if __name__=="__main__":	
	run=True
	while run:
		print("""
		-------------------------Welcome to Maths Calculation-------------------------
		1. Get Nth Fibonacci Number
		2. Factorial of a Given Number
		3. Simplify given Fraction
		4. Given number is Perfect Number or not
		5. Given number is Prime or not
		6. Get divisors of given number
		7. Get Prime numbers between given 2 Prime Numbers
		8. Get GCD of 2 given positive numbers
		9. Exit		
		--------------------------*****************************-------------------------
		""")
		try:
			choice = int(raw_input("Enter Your Choice: "))
		except:
			print("Value Error please enter only 1-9")
		run=read_choice(choice)
		
		
