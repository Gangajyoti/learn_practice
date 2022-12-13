from itertools import combinations
from math import factorial
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        nums = list(range(1,k+1))
        print(sum(nums))
        comb = combinations(nums,n)
        ways = 0
        # li = list(filter(lambda x : sum(x)>0,map(lambda x: x if sum(x)==target else (0,0) ,comb)))


        # return len(li) * factorial(n)


ob = Solution()
print(ob.numRollsToTarget(30,30,500))


# Print the obtained combinations

