##matrix clockwise rotation:
mat = [[1,2,3],[4,5,6],[7,8,9]]
clock_rotated_mat = list(zip(*mat[::-1]))
print(clock_rotated_mat)

##matrix anti-clockwise rotation:

mat = [[1,2,3],[4,5,6],[7,8,9]]
anti_clock_rotated_mat = (list(zip(*mat))[::-1])
print(anti_clock_rotated_mat)

#Explaination:
#1. [::-1] - reverse the matrix
#2. zip(*_) - unpacks the nested list values of each list according to its index.
#3. list() - cast back to list object.
