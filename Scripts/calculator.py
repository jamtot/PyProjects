def add(num1, num2):
    print("The sum of "+str(num1)+" and "+ str(num2) + " is " + str(num1+num2))

def multiply(num1, num2):
    print("The product of "+str(num1)+" and "+ str(num2) + " is " + str(num1*num2))

def divide(num1, num2):
    print("The quotient of "+str(num1)+" and "+ str(num2) + " is " + str(num1/num2))

def subtract(num1,num2):
    print("The difference between "+str(num1)+" and "+ str(num2) + " is " + str(num1-num2))

def welcome():
    print("""Welcome to calculator.py.
There are 4 functions to avail from:
add(#,#) - add two #'s e.g. add(4,6)
subtract(#,#) - subract one # from another e.g. subtract(10,5)
multiply(#,#) - multiply one # by another e.g. multiply(4,3)
divide(#,#) - divide one # by another e.g. divide(12,3)""")


if __name__ == "__main__":
    welcome()