class Solution:
    @classmethod
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        
        return haystack.find(haystack)

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
haystack = "sadbutsad"
needle = "sad"
print(Solution.strStr(haystack,needle))

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
haystack = "leetcode"
needle = "leeto"
print(Solution.strStr(haystack,needle))