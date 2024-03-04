class Solution:
    @classmethod
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c, r, o, a, k, found, same_forg=0,0,0,0,0,0,0
        for walker in croakOfFrogs:
            if walker not in "croak":
                return -1
            else:
                if walker == 'c':
                    if c == k and c !=0:
                        same_forg += 1
                    c +=1
                elif walker == 'r':
                    r +=1
                elif walker == 'o':
                    o +=1
                elif walker == 'a':
                    a +=1
                elif walker == 'k':
                    k+=1
            if not c >= r >= o >= a >= k:
                return -1
        if not c == r == o == a == k:
            return -1
        return c - same_forg

input = "croakcroak"
output = Solution.minNumberOfFrogs(input)
print(output)
input = "crcoakroak"
output = Solution.minNumberOfFrogs(input)
print(output)
input = "croakcrook"
output = Solution.minNumberOfFrogs(input)
print(output)
