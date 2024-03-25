import collections
class Solution:
    @classmethod
    def bullsAndCows(self, secret: str, guess: str)->str:
        bulls=0
        cows=0
        checkSecret = collections.Counter(secret)    
        # chekcing cows in secret
        for i in guess:
            if i in checkSecret:
                if checkSecret[i] == 1:
                    cows+=1
                    checkSecret[i]+=1
                if checkSecret[i] > 1:
                    checkSecret[i]-=1

        # checking bulls in secret
        for x ,y in zip( secret, guess):
            if x==y:
                bulls+=1
                cows-=1
        return str(bulls)+"A"+str(cows)+"B"
    
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"

secret = "1807"
guess = "7810"
output = Solution.bullsAndCows(secret, guess)
print(output)

secret2 = "1123"
guess2 =  "0111"
output2 = Solution.bullsAndCows(secret2, guess2)
print(output2)
