"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
"""


# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         c = 0
#         while True:
#             if 0 in nums:
#                 nums.remove(0)
#                 c +=1
#                 print(nums)
#             else:
#                 break
#         if c:
#             for i in range(0,c):
#                 nums.append(0)
#         return nums

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = nums.count(0)
        if c :
            for i in range(0,c):
                nums.remove(0)
                nums.append(0)
        return nums

C = Solution()
nums = [0,1,0,3,12,0,0,0,0,0,0,0]
print(C.moveZeroes(nums))