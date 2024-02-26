class Solution:
    @classmethod
    def longestSubstringWithoutRepeatingCharacters(self, s:str)->int:
        charSet = set()
        subWaler = 0
        maxLen = 0
        
        for walker in range(0, len(s)):
            if s[walker] not in charSet:
                charSet.add(s[walker])
                maxLen = len(charSet)
            else:
                while s[walker] in charSet:
                    charSet.remove(s[subWaler])
                    subWaler+=1
                charSet.add(s[walker])
        
        return maxLen

input1 = "abcabcbb"
output1 = Solution.longestSubstringWithoutRepeatingCharacters(input1)
print(output1)
