"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums1_int,nums2_int = 0,0
        c ,d= 0,0
        for item in reversed(num1):
            print(item)
            nums1_int += int(item)* (10 **c)
            c +=1
        for item in reversed(num2):
            print(item)
            nums2_int += int(item)* (10 **d)
            d +=1
        return (nums1_int + nums2_int)


c= Solution()
num1 = "11"
num2 = "123"
print(c.addStrings(num1,num2))