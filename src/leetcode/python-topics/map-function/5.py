"""
Using map() function and lambda add each elements of two lists together. Use a lambda with two arguments.
"""

lst1=[100, 200, 300, 400, 500]
lst2=[1,10,100,1000,10000]


#Type your answer here.

lst3= list(map( lambda x,y:x+y ,lst1,lst2))


print(lst3)

