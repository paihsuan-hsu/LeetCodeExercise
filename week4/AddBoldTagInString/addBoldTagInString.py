class Solution:
    @classmethod
    def addBoldTag(self, s: str, words: list[str]) -> str:
        isBold = [False for _ in range(len(s))]

        def findAndMark(word):
            searchPos = 0
            while True:
                found = s.find(word, searchPos)
                if found != -1:
                    for i in range(found, found + len(word)):
                        isBold[i] = True
                    searchPos = found + 1
                else:
                    break
                    
        for word in words:
            findAndMark(word)
 
        res = []
        i, n = 0, len(s)
        
        while i < n:
            if isBold[i]:
                res.append("<b>")
                while i < n and isBold[i]:
                    res.append(s[i])
                    i += 1
                res.append("</b>")
            else:
                while i < n and not isBold[i]:
                    res.append(s[i])
                    i += 1
        
        ouptut =""
        for x in res:
            ouptut+=x

        return ouptut
    
# Input: s = "abcxyz123", words = ["abc","123"]
# Output: "<b>abc</b>xyz<b>123</b>"
    
s = "abcxyz123"
words = ["abc","123"]
output = Solution.addBoldTag(s, words)
print(output)