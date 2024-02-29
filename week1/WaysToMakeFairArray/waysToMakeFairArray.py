class Solution:
    @classmethod
    def waysToMakeFairArray(self, numbers: list)-> int:
        remover=0
        index =0
        n = len(numbers)
        found =0

        while remover<n :
            oddSum = 0
            evenSum = 0
            i = 0
            while i < n:
                if i == remover:
                    i+=1
                    continue
                elif i < remover:
                    index = i
                else:
                    index = i-1
                if index%2==0:
                    evenSum+=numbers[i]
                else:
                    oddSum+=numbers[i]
                i+=1
            print(str(evenSum)+ "  " +str(oddSum) +"\n")
            if evenSum == oddSum:
                found += 1
            
            remover+=1
        return found

input = [2,1,6,4]
output = Solution.waysToMakeFairArray(input)
print(output)