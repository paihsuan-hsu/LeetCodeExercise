import random
class Solution:
    def __init__(self, nums: list[int]):
        self.org = nums
        self.numbers = nums

    def shuffle(self):
        sf = list(self.numbers)
        # m = len(sf)
        # for i in range(m):
        #     tmp = random.randrange(i, m)
        #     sf[i], sf[tmp] =  sf[tmp], sf[i]
        # or just use the shuffle func --- 
        random.shuffle(sf)
        self.numbers = sf

    def reset(self):
        self.numbers = self.org
    
input = [1,2,3]
output = Solution(input)
print(output.numbers)
output.shuffle()
print(output.numbers)
output.reset()
print(output.numbers)
