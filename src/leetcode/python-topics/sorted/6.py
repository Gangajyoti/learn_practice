"""
Using len function and sorted() function, sort the list based on the length of the strings this time
in descending order.
"""

lakes1=["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]

#Type your answer here.

lakes2= sorted(lakes1,key=len,reverse=True)


print(lakes2)

