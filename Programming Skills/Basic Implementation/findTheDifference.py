class Solution:
    @classmethod
    def findTheDifference(self, s: str, t:str)-> str:

        n1 = len(s)
        n2 = len(t)    
        i=0  
        # since n2 == n1+1, we don't need to worry out of rnage
        while i < n1:
            if s[i] not in t:
                return s[i]
            i+=1
        return t[i]
            
# Input: s = "abcd", t = "abcde"
# Output: "e"
s = "abcd"
t = "abcde"
output = Solution.findTheDifference(s,t)
print(output)
# Input: s = "", t = "y"
# Output: "y"
s = ""
t = "y"
output = Solution.findTheDifference(s,t)
print(output)