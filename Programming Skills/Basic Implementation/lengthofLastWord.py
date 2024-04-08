class Solution:
    @classmethod
    def lengthOfLastWord(self, s: str)-> int:
        words = s.split()

        return len(words[-1])

# Input: s = "Hello World"
# Output: 5
s = "Hello World"        
print(Solution.lengthOfLastWord(s))

# Input: s = "   fly me   to   the moon  "
# Output: 4
s = "   fly me   to   the moon  " 
print(Solution.lengthOfLastWord(s))


# Input: s = "luffy is still joyboy"
# Output: 6
s = "luffy is still joyboy"
print(Solution.lengthOfLastWord(s))
