"""
Using map() function and lambda and count() function create a list which consists of
the number of occurence of letter: a.
"""

lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
#Type your answer here.

lst2= list(map(lambda x:x.count('a'),lst1))


print(lst2)

