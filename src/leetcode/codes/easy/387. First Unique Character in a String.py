"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        old_s = s
        while len(s)>=1:

            if s[0] and old_s.count(s[0])<=1:
                return old_s.index(s[0])
            else:
                s = s.removeprefix(s[0])

        return -1

c = Solution()
s = "lovely"
print(c.firstUniqChar(s = "aabb"))