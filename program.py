# Program to find factorial of a number

def Factorial(num):
    factorial = 1
    if num < 0:
        print("Factorial doesn't exists")
    elif num == 0:
        print(1)
    else:
        for i in range(1, num + 1):
            factorial *= i
        print("Factorial of number", num,"is", factorial)

num = int(input())
result = Factorial(num)