def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


results = factorial(int(input("Enter a number")))
print("The factorial of the number is ", results)