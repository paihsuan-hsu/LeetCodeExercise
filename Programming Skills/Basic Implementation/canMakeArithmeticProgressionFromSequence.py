class Solution:
    @classmethod
    def canMakeArithmeticProgression(self, arr: list[int])-> bool:
        arr.sort()
        n = len(arr)
        if n == 1 or n == 0:
            return True
        
        diff = arr[1]-arr[0]
        for i in range(n-1):
            if arr[i+1] - arr[i] != diff:
                return False

        return True


# Input: arr = [3,5,1]
# Output: true
input = [3,5,1]
print(Solution.canMakeArithmeticProgression(input))

# Input: arr = [1,2,4]
# Output: false
input = [1,2,4]
print(Solution.canMakeArithmeticProgression(input))