"""
Using filter() and list() functions and .lower() method filter all the vowels in a given string.
"""
str1="Winter Olympics in 2022 will take place in Beijing China"
#Type your answer here.

lst= list(filter(lambda x:x.lower()in ['a','e','i','o','u'],str1))
""" lst = list(filter(lambda x: True if x.lower() in "aeiou" else False, str1)) """

print(lst)

