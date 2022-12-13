"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []
        count = 0
        for symbol in strs:

            if symbol in ")}]" and len(stack) == 0:
                return False
            elif symbol in "({[":
                stack.append(symbol)
            elif symbol == brackets[stack[-1]]:
                stack.pop()
                count += 1
            else:
                return False
        if count != 0 and len(stack) ==0:
            return True
        else:
            return False






strs = "([]){"

c = Solution()
print(c.isValid(strs))



"""
optimized code from google 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mapping = {
            '(':')',
            '[':']',
            '{':'}'            
        }
        
        for char in s:
            if char in mapping.keys():
                stack.append(mapping[char])
            elif not stack or stack[-1]!=char:
                return False
            else:
                stack.pop()
        
        return len(stack)==0
"""






