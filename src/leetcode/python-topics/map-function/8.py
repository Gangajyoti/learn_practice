"""
Using map() function, first return a new list with absolute values of existing list.
Then for ans_1, find the total sum of the new list's elements.
"""

lst=[99.3890,-3.5, 5, -0.7123, -9, -0.003]
new_lst= list(map(abs,lst))

ans_1= sum(new_lst)

print(ans_1)

