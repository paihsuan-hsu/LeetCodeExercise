class Solution:
    @classmethod
    def mergeAlternately(self, word1: str, word2:str )->str:
        output=""
        n1 = len(word1)
        n2 = len(word2)
        walker=0

        while walker < max(n1,n2):
            if walker<n1:
                output+=word1[walker]
            if walker<n2:
                output+=word2[walker]
            walker+=1
        
        return output
    
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
word1 = "abc"
word2 = "pqr"
output = Solution.mergeAlternately(word1,word2)
print(output)

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
word1 = "abcd"
word2 = "pq"
output = Solution.mergeAlternately(word1,word2)
print(output)
