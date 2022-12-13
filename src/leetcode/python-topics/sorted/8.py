"""
Using lambda and sorted() function, sort the list based on the remainder from dividing each element to 5
(From greater to smaller).
"""

lst1=[1000, 50, 66, 101, 333, 9999, 19, 300, 200, 250]

#Type your answer here.

lst2=list(sorted(lst1,key=lambda x:x%5,reverse=True))


print(lst2)