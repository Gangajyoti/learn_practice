"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.



Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1


Constraints:

1 <= n <= 231 - 1
1 <= pick <= n
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
import time


class Solution:
    def __init__(self,pick:int):
        self.pick = pick
    def guess(self,num: int) -> int:
        if num == self.pick : return 0
        if num > self.pick: return -1
        if num < self.pick : return 1



    def guessNumber(self, n: int) -> int:

        if self.guess(n)<=0:
            # if self.guess(n) == 0:
            #     return n
            lo = 1
            hi = n
            mid = ((lo + hi) // 2)
            while True:
                print(lo,mid,hi)
                if self.guess(mid) == 0:
                    return mid
                if self.guess(mid) < 0:
                    hi = mid
                    mid = (hi - lo) //2
                if self.guess(mid) > 0:
                    lo = mid
                    mid = ((hi + lo) // 2) + 1



        else:
            print('im in else')
            lo = n
            hi = 2*n
            mid = ((hi + lo) // 2)+1
            while True:
                print(mid)
                if self.guess(mid) == 0:
                    return mid
                if self.guess(mid) < 0:
                    hi = mid

                if self.guess(mid) > 0:
                    hi = 2*mid

                mid = ((hi + lo) // 2) + 1



c = Solution(2)

strt_time = time.time()
print(c.guessNumber(10000))
print('code took :',time.time() - strt_time)