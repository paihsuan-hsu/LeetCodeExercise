class Solution:
    @classmethod
    def toLowerCase(self, s:str)-> str:
        return s.lower()
    
# Input: s = "Hello"
# Output: "hello"
s = "Hello"    
print(Solution.toLowerCase(s))
# Input: s = "here"
# Output: "here"
s = "here"    
print(Solution.toLowerCase(s))

# Input: s = "LOVELY"
# Output: "lovely"
s = "LOVELY"    
print(Solution.toLowerCase(s))

