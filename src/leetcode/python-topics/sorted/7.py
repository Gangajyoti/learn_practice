"""
Using lambda and sorted() function, sort the list based on last characters of the items from z to a.
"""

lakes1=["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]

#Type your answer here.

lakes2= list(sorted(lakes1,key=lambda x:x[-1],reverse=True))


print(lakes2)