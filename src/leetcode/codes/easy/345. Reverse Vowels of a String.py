from operator import itemgetter, attrgetter
class Solution:
    def reverseVowels(self, s: str) -> str:
        mapper = list(filter(lambda x: x != True, (map(lambda x,y: (x,y) if x in'aeiouAEIOU' else True,s,list(range(0,len(s))) ))))
        ind_l = [j for i,j in mapper]

        ss = list(s)
        reversedVowel = list(map(lambda x: x[0] ,sorted(mapper,key=itemgetter(1),reverse=True)))

        for i in range(0,len(ind_l)):
            idx= ind_l[i]
            val = reversedVowel[i]

            ss[idx] = val

        return "".join(ss)


c = Solution()
s = "hello"
print(c.reverseVowels(s))