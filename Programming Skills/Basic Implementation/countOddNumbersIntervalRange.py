class Solution:
    def countOdds(self, low:int, high:int)->int:
        odds=[]
        while low <= high:
            if low%2 !=0:
                odds.append(low)
            low+=1
        return len(odds)

# Input: low = 3, high = 7
# Output: 3
output = Solution()
low = 3
high = 7
print(output.countOdds(low,high))

# Input: low = 8, high = 10
# Output: 1
low = 8
high = 10
print(output.countOdds(low,high))
