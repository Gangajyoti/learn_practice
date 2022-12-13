"""
Using map() and filter() functions add 2000 to the values below 8000.
"""
lst1=[1000, 500, 600, 700, 5000, 90000, 17500]
#Type your answer here.

lst2=list(map(lambda x: x+2000 ,filter(lambda x:x<8000 ,lst1) ))

print(lst2)

