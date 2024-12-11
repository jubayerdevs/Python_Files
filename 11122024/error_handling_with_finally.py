# nums = [1, 2]

# # print(nums[3])
# index = 1

# try:
#     print(nums[index])
# except IndexError:
#     print("Wrong index!")
# finally:
#     print("A value from nums wass accessed!")


# ------------------------------------

try:
    file = open("data.txt", "r")
    #something to do with the file
    print(file)
except:
    print("Error while reading the file")
finally:
    file.close()