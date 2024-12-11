
## Dealing with the error

# try:
#     age = int(input("How old are you?"))
# except:
#     print("Wrong input dude!")


# x = 3/0
# print(x)


try:
    apples = int(input("How many apples?"))
    persons = int(input("How many persons?"))

    dist = apples / persons
    print(f"Apple per persons, {dist}")
# except:
#     print("Error!")

except ValueError:
    print("Please enter only numeric values")
except ZeroDivisionError:
    print("Number of persons can not be zero!")
except:
    print("Some unknown error happened!")

    