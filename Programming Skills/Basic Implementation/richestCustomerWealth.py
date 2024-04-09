class Sulotion:
    def maximumWealth(self, accounts: list[list[int]])-> int:
        maxWealth=0
        for i in range(len(accounts)):
            maxWealth = max(maxWealth, sum(accounts[i]))

        return maxWealth
    
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
output = Sulotion()
accounts = [[1,2,3],[3,2,1]]
print(output.maximumWealth(accounts))

# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
accounts = [[1,5],[7,3],[3,5]]
print(output.maximumWealth(accounts))

# Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17
accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(output.maximumWealth(accounts))
