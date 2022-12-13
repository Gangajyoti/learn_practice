"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.


Constraints:

1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.


"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed: return True
        else:
            # name_set = list(set(name))
            inr_idx = 0
            counter = 0
            for item in name:
                print(counter,name[counter:],typed[counter+inr_idx:])
                if item not in typed or name[counter:].count(item)>typed[counter+inr_idx:].count(item) \
                        or set(name[counter:]) != set(typed[counter+inr_idx:]) : return False
                if name[counter:].count(item)<typed[counter+inr_idx:].count(item) :
                    if  name[counter+1] and item != name[counter+1]:
                        inr_idx += typed[counter+inr_idx:].count(item) - name[counter:].count(item)
                    else   :
                        inr_idx += typed[counter + inr_idx:].count(item) - name[counter:].count(item)
                # print(inr_idx,typed[name.index(item):].count(item) ,name[name.index(item):].count(item),name[name.index(item)+1])
                counter += 1


        return True


c = Solution()
name = "vtkgn"



typed = "vttkgnn"
print(c.isLongPressedName(name,typed))
