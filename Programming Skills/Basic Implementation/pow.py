class Solution:
    def pow(slef, x: float, n: int)->float:
        return pow(x,n)
    
output = Solution()
# Input: x = 2.00000, n = 10
# Output: 1024.00000
x = 2.00000
n = 10
print(output.pow(x,n))
# Input: x = 2.10000, n = 3
# Output: 9.26100
x = 2.10000 
n = 3
print(output.pow(x,n))
# Input: x = 2.00000, n = -2
# Output: 0.25000
x = 2.00000
n = -2
print(output.pow(x,n))
