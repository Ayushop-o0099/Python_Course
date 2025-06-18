def factorial(n):
    if n<2:
        return 1
    else:
        return n* (factorial(n-1))
m=int(input("Enter a Number : "))
fac=factorial(m)
print("Factorial of",m,"is :",fac)