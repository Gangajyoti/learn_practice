"""
Using sorted() function and lambda sort the words in the list based on their second letter from a to z.
"""

lst=["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]
#Type your answer here.

lst=sorted(lst, key = lambda a:a[1] )

print(lst)
