import collections
class Solution:
    @classmethod
    def isAnagram(self, s:str,t:str)->bool:
        if len(s) != len(t):
            False
        
        ht = collections.defaultdict(int)

        for v in s:
            ht[v] += 1
        
        for x in t:
            ht[x] -= 1
        
        for val in ht.values():
            if val != 0:
                return False
            
        return True

        # or we can sort both str and check if they are the same str
    

# Input: s = "anagram", t = "nagaram"
# Output: true
s = "anagram"
t = "nagaram"
print(Solution.isAnagram(s,t))

# Input: s = "rat", t = "car"
# Output: false
s = "rat"
t = "car"
print(Solution.isAnagram(s,t))