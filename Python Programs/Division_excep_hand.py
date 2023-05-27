#exception handling for division
try:
    x=int(input("Enter First Number:"))
    y=int(input("Enter Second Number:"))
    print(x/y)

except ZeroDivisionError:
    print("can't divide with zero")
except ValueError:
    print("please provide int value only")