class Solution:
    @classmethod
    def judgeCircle(self, moves: str)->bool:
        m = [0,0]
        # Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
        for i in moves:
            if i == 'R':
                m[0] += 1
            if i == 'L':
                m[0] -= 1
            if i == 'U':
                m[1] += 1
            if i == 'D':
                m[1] -= 1
        return m == [0,0]

# Input: moves = "UD"
# Output: true
print(Solution.judgeCircle("UD"))

# Input: moves = "LL"
# Output: false
print(Solution.judgeCircle("LL"))