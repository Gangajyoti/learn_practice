"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"


Constraints:

1 <= columnNumber <= 231 - 1
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        LETTERS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while columnNumber:
            columnNumber, rem = divmod(columnNumber - 1, 26)
            print(columnNumber,rem)
            result = LETTERS[rem]+ result
        return result

"""
The divmod() method in python takes two numbers and returns a pair of numbers consisting of their quotient and remainder. 

Syntax : 

divmod(x, y)
x and y : x is numerator and y is denominator
x and y must be non complex
"""

c= Solution()
print(c.convertToTitle(27))