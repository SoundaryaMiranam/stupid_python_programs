
##Adding an element to set,won't add if element already exists.
x = {'Jack','Csaba','Nat'}
x.add('Annie')
print(x)
# {'Csaba', 'Nat', 'Jack', 'Annie'}

##Removes all elements from set.
x = {'Emma', 'Mike'}
x.clear()
print(x)
# set()

##Returns a copy of set.
x = {'Layla','Ronna'}
y = x.copy()
print(y)
# {'Ronna', 'Layla'}

##Returns different elements from two sets
x = {'Tabs', 'oliver', 'Corner'}
y = {'Sam', 'janine','oliver'}
z = x.difference(y)
print(z)
# {'Corner', 'Tabs'}

##Same as "difference", Removes unwanted elements instead of returing new set.
x = {'Tabs', 'oliver', 'Corner'}
y = {'Sam', 'janine','oliver'}
x.difference_update(y)
print(x)
# {'Corner', 'Tabs'}

##Removes item from a set, won't throw error if item doesn't exist
x = {'John','Aron','Luo'}
x.discard('John')
print(x)
# {'Luo', 'Aron'}

##Returns a set containing only elements that exists in all sets,we can pass multiple parameters
x = {'Rosie','Peter','Sean'}
y = {'Peter', 'Yurl', 'Vector'}
z = x.intersection(y)
print(z)
# {'Peter'}

##Same as "intersection", Removes unwanted elements instead of returing new set.
x = {'Rosie','Peter','Sean'}
y = {'Peter', 'Yurl', 'Vector'}
x.intersection_update(y)
print(x)
# {'Peter'}

##Returns True if none of the elements are in both the sets.
x = {'Rosie','Peter','Sean'}
y = {'Sam', 'Yurl', 'Vector'}
z = x.isdisjoint(y)
print(z)
# True

##Returns True if all elements in original set exists in specified set.
x = {'Rosie','Peter','Sean'}
y = {'Sean', 'Yurl','Rosie', 'Peter'}
z = x.issubset(y)
print(z)
# True

##Returns True if all elements in specified set exists in original set.
x = {'Rosie','Peter','Sean'}
y = {'Sean', 'Peter'}
z = x.issuperset(y)
print(z)
# True

##Removes and returns element from set.
x = {'Rosie','Peter','Sean'}
y = x.pop()
print(x,y)
# {'Peter', 'Sean'} Rosie

##Removes element from a set and raises a error.
x = {'Rosie','Peter','Sean'}
x.remove('Peter')
print(x)
# {'Rosie', 'Sean'}

##Returns set containing all elements from both sets, but not those present in both sets.
x = {'Rosie','Peter','Sean'}
y = {'Peter', 'Yurl', 'Vector'}
z = x.symmetric_difference(y)
print(z)
# {'Vector', 'Sean', 'Rosie', 'Yurl'}

##Same as "symmetric_difference" but updates the original set rather than returning new set.
x = {'Rosie','Peter','Sean'}
y = {'Peter', 'Yurl', 'Vector'}
x.symmetric_difference_update(y)
print(x)
# {'Vector', 'Sean', 'Rosie', 'Yurl'}

##Returns set containing elements from original set and elements from specified set or iterables.
x = {'Tabs', 'oliver', 'Corner'}
y = {'Sam', 'janine','oliver'}
z = x.union(y)
print(z)
# {'Corner', 'Tabs', 'oliver', 'janine', 'Sam'}

##Update original set by adding elements from another set or iterable.
x = {'Tabs', 'oliver', 'Corner'}
y = {'Sam', 'janine','oliver'}
x.update(y)
print(x)
# {'Corner', 'Tabs', 'oliver', 'janine', 'Sam'}





