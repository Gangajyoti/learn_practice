"""
This time using filter() and list() functions filter all the positive integers in the string.
"""
str1="Winter Olympics in 2022 will take place in Beijing China"
#Type your answer here.

lst= list(filter(lambda x: True if x in '0123456789'else False ,str1))

print(lst)

