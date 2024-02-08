def fact(a):
    if a == 1:
        return 1
    else:
        return a * fact(a - 1)


num = int(input("Enter a number to get factorial: "))


result = fact(num)
print(f"The factorial of {num} is: {result}")