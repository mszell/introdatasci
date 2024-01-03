y = 4

def mystery_function(x):
    mylist = []
    for i in range(x+1):
        mylist.append(i)
    return sum(mylist)

result = mystery_function(y)

print(f"The input is: {y}, the result is: {result}")