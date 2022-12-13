"""
Using map() function and len() function create a list that's consisted of lengths of
each element in the first list.
"""

#Type your answer here.

lst1=["Alpine", "Avalanche", "Powder", "Snowflake", "Summit"]

lst2= list(map(lambda  a:len(a),lst1))
""" list(map(len,lst1))"""


print(lst2)

