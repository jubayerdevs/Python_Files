#given a list of numbers, return the squared list of array
#input: [1, 2, 3, 4] -> output: [1, 4, 9, 16]

nums = [1, 2, 3, 4]

temp = list(map(lambda x: x** 2, nums))
print(list(temp))


def squared(nums):
    return list(map(lambda x: x ** 2, nums))
print(squared(nums))


#given a list of numbers, filter the ones divisible by 3
#input: [1, 3, 5, 6, 9, 11, 15] -> output: [3, 6, 9, 15]

def is_divisible_by_three(x):
    return x % 3 == 0

result = list(filter(lambda x: x % 3 == 0, nums))
print(result)


