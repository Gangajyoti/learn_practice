"""
Using len function and sorted() function, sort the list based on the length of the strings
(In ascending order).
"""


lakes1=["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]

#Type your answer here.

lakes2=list(sorted(lakes1,key=lambda x:len(x)))
"""
lakes2 = sorted(lakes1, key = len)
"""

print(lakes2)

