class Solution:
    @classmethod
    def isPalindromic(self, s: str)-> bool:
        left=0
        right=len(s)-1
        while left<right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True

    @classmethod
    def longestPalindromicSubstring(self, input: str)->str:
        if len(input) <= 1:
            return input
        max_len=1
        max_str=input[0]
        for i in range(len(input)):
            for j in range(i+max_len, len(input)):
                if j-i > max_len and self.isPalindromic(input[i:j]):
                    max_len = j-i
                    max_str = input[i:j]
        return max_str

# Input: s = "babad"
# Output: "bab"
input = "babad"
output = Solution.longestPalindromicSubstring(input)
print(output)