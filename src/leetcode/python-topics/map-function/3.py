"""
Write a map function that adds "Hello, " in front of each item in the list.
"""
#Type your answer here.

lst1=["Jane", "Lee", "Will", "Brie"]

lst2=list(map(lambda a:'Hello, '+a,lst1))

print(lst2)