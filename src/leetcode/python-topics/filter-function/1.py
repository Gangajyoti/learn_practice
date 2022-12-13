"""
Using filter() function filter the list so that only negative numbers are left.
"""
lst1=[12, -1, 9, 8, -0.5, -0.2, -100]
#Type your answer here.

lst2= list(filter(lambda x:  x <0,lst1))


print(lst2)