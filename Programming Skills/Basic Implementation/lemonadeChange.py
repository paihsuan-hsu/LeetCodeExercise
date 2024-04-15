class Solution:
    def lemonadeChange(self, bills: list[int])->bool:
        change = {
            5:0,
            10:0,
            20:0
        }
        i = 0
        print("bills are: ", bills)
        while i < len(bills):
            if bills[i] in change:
                change[bills[i]]+=1
            elif bills[i] % 5 !=0:
                return False
            
            exchange = bills[i] - 5
            if exchange / 20 >= 1:
                twentyBills = exchange // 20
                if change[20] >= twentyBills:
                    change[20] -= twentyBills
                    exchange -= (20*twentyBills)
            if exchange / 10 >= 1:
                tenBills = exchange//10
                if change[10] >= tenBills:
                    change[10] -= tenBills
                    exchange -= (10*tenBills)
            if exchange / 5 >= 1:
                fiveBills = exchange//5
                if change[5] >= fiveBills:
                    change[5] -= fiveBills
                    exchange -= (5*fiveBills)    
            print("change is: ", change, "exchange is: ", exchange)
            if exchange != 0:
                return False
            i+=1

        return True
                
# Input: bills = [5,5,5,10,20]
# Output: true
output = Solution()
bills = [5,5,5,10,20]
print(output.lemonadeChange(bills))

# Input: bills = [5,5,10,10,20]
# Output: false
bills = [5,5,10,10,20]
print(output.lemonadeChange(bills))



