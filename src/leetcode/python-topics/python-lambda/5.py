"""
Using sorted() function and lambda sort the tuples in the list based on the second items.

"""

lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
#Type your answer here.

lst= sorted(lst, key=lambda a:a[1])


print(lst)
