"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.



Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Can you find an O(n) solution?
"""


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums_set = (set(nums))
        counter ,max_num= 0,0
        if len(nums_set) >= 3:
            while nums_set and counter < 3:

                max_num = max(nums_set)
                nums_set.remove(max_num)
                counter += 1
            print(nums_set, max_num)
            return max_num

        return max(nums_set)

c = Solution()
nums = [1,2,2,5,3,5]
print(c.thirdMax(nums))