class Solution:
    @classmethod
    def letterCombinationsOfPhoneNumber(self, numbers:str)->list[str]:
        phone_map={
            '1':'',
            '2':'abc',
            '3':'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(letters, numbers):
            if len(numbers) == 0:
                output.append(letters)
            else:
                for char in phone_map[numbers[0]]:
                    backtrack(letters+char, numbers[1:])

        output=[]
        backtrack("",numbers)
        return output

input = "23"
output = Solution.letterCombinationsOfPhoneNumber(input)
print(output)
