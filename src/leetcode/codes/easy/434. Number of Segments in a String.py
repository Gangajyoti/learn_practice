"""
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.



Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1


Constraints:

0 <= s.length <= 300
s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
The only space character in s is ' '.
"""
import re
class Solution:
    def countSegments(self, s: str) -> int:
        s = re.sub(r"[\b]","",s)



        # s= s.rstrip().lstrip()
        # print(s)


        if  (set(s)) !={' '} and len(s) >0 :

            return len(s.split())

c = Solution()
print(c.countSegments(""))