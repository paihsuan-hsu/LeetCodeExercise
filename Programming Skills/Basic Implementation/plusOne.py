class Solution:
    @classmethod
    def plusOne(delf, digits: list[int])->list[int]:
        output = []
        output = digits
        n = len(digits)-1
        if output[n] == 9:
            if n >= 1:
                output[n-1]=output[n-1]+1
                output[n]=0
            else:
                output[n]=1
                output+=[0]
        else:
            output[n]+=1
        
        return output
        
# # Input: digits = [1,2,3]
# # Output: [1,2,4]
input = [1,2,3]
print(Solution.plusOne(input))

# # Input: digits = [4,3,2,1]
# # Output: [4,3,2,2]
input = [4,3,2,1]
print(Solution.plusOne(input))

# # Input: digits = [9]
# # Output: [1,0]
input = [9]
print(Solution.plusOne(input))

# Input: digits = [1,9]
# Output: [2,0]
input = [1,9]
print(Solution.plusOne(input))