try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")