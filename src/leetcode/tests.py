
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        unique_combinations = []
        full_arr = list_1+list_2
        permut = itertools.permutations(full_arr,len(full_arr))
        for comb in permut:

            unique_combinations.append(comb)

        # printing unique_combination list
        for i in range(len(unique_combinations)):
           # print(list(filter(lambda x: x == False,(map(lambda x,y :True if x == y else False,sorted(full_arr)  ,\
           #                                             list(unique_combinations[i]))))))
            if sorted(full_arr) == list(unique_combinations[i]):
                print(i,unique_combinations[i])

        # print(unique_combinations)
        if len(nums2)>0:
            pass
        else:
            nums1

c = Solution()
list_1 = [2,3,4,5]
list_2 = [1, 4, 9]
print(list_1+list_2)
# num1 = []
# num2 = []

