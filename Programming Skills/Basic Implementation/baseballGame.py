class Solution:
    @classmethod
    def calPoints(self, operations: list[str]) -> int:
        op = []
        for i in operations:
            if i == '+':
                op.append(op[-1]+ op[-2])
            if i == 'D':
                op.append(op[-1]*2)
            if i == 'C':
                op.pop()
            if i.isnumeric():
                op.append(int(i))
        return sum(op)

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
# Input: ops = ["5","2","C","D","+"]
# Output: 30
ops = ["5","2","C","D","+"]
output = Solution.calPoints(ops)
print(output)