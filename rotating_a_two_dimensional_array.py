# -*- coding: utf-8 -*-
"""rotating-a-two-dimensional-array.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cUIKB8BCXvGDAbXFqZ9IfGk7Si4ZPK4D

###matrix clockwise rotation:
"""

mat = [[1,2,3],[4,5,6],[7,8,9]]
clock_rotated_mat = list(zip(*mat[::-1]))
clock_rotated_mat

"""[::-1] - reverse the matrix

zip(*_) - unpacks the nested list values of each list according to its index.

list() - cast back to list object.

###matrix anti-clockwise rotation:
"""

mat = [[1,2,3],[4,5,6],[7,8,9]]
anti_clock_rotated_mat = (list(zip(*mat))[::-1])
anti_clock_rotated_mat