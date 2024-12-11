def add_one(x):
    return x+1

y = 5 + 5
#anonumous function
add_one_lambda = lambda x: x + 1

a = add_one_lambda(5)
b =  add_one(5)

print(a, b)


demo = lambda x, y: x + y
demo(2, 4) #6