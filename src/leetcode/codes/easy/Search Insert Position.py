"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return list(map(lambda x:'low' if x<target else'high',nums)).count('low')


arr =[1,3,4,6,7,8,9,10]
    # [0,0,1,1,1,2,2,3,3,4]
c = Solution()
print(c.searchInsert(arr,5))
