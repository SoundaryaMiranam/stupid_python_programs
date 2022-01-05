#Creating lists
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)    


squares = [x**2 for x in range(10)]  
print(squares)

#List comprehension with nested loops.
first = ['a1', 'a2']; second = ['b1', 'b2']
result = []
for i in first:
    for j in second :
        pair = (i, j)
        result.append(pair)
print(result)


result = [(i,j) for i in first for j in second]
print(result)

#CREATING DICTIONARIES 
result = {}
for x in range(10):
   result[x] = x**2
print(result)


result = {x: x**2 for x in range(10)}
print(result)

#REMOVING DUPLICATES FROM LIST
fruits = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
new = []
for fruit in fruits:
    if fruit not in new:
        new.append(fruit)
print(new)  

# Actually make `new` a list
new = list(set(fruits))
print(new)

#UNPACKING THE ITEMS FROM LIST
x, y = (15, 5)
print(x)
print(y)

fruit, num, date = ['apple', 5,(2021, 11, 7)]

print(date)

#LISTS SLICING
x = [1, 2, 3, 4, 5]
result = x[:3]

print(result)

#sequence[start:stop:step]
x = [10, 5, 13, 4, 12, 43, 7, 8]
result = x[1:6:2]
print(result)
