class Solution:
    @classmethod
    def repeatedSubstringPattern(self, s:str)-> bool:
        n = len(s)
        ss = s+s
        print(ss)
        print(ss[1:-1])
        if s in ss[1:-1]:
            return True

        return False
    
    # or using re.search()


# Input: s = "abab"
# Output: true
s = "abab"
output = Solution.repeatedSubstringPattern(s)
print(output)

# Input: s = "aba"
# Output: false
s = "aba"
output = Solution.repeatedSubstringPattern(s)
print(output)

# Input: s = "abcabcabcabc"
# Output: true
s = "abcabcabcabc"
output = Solution.repeatedSubstringPattern(s)
print(output)