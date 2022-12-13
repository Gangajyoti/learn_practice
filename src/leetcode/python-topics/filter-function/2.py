"""
Using filter function, filter the even numbers so that only odd numbers are passed to the new list.
"""
lst1=[22, 100, 19, 13, 11, 1, 4, 66]
#Type your answer here.

lst2= list(filter(lambda x: x%2!=0 ,lst1))

print(lst2)

