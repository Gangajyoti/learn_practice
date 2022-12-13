"""
This time swap the map() and filter() functions so that map() function is inside filter() function.
 Convert a number to positive if it's negative in the list. Only pass those that are converted from
 negative to positive to the new list.
"""
lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
#Type your answer here.

lst2= list(filter(lambda x:  x>0 ,map(lambda x: abs(x) if x<0 else False,lst1)))
"""
lst2 = list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, lst1)))
"""

print(lst2)

