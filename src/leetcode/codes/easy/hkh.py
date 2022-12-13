


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        if sum(nums[1:]) ==0: return 0
        for i in range(1,len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):return i
        if sum(nums[:len(nums)-1]) == 0:return len(nums)-1

        return  -1

c = Solution()
nums = [-1,-1,1,1,0,0]
print(c.pivotIndex(nums))


