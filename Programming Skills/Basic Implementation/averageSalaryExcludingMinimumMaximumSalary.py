class Solution:
    def average(self, salary: list[int])->float:
        maxSalary = salary[0]
        minSalary = salary[0]
        i = 1
        while i < len(salary):
            maxSalary=max(maxSalary, salary[i])
            minSalary=min(minSalary, salary[i])
            i+=1
        AveSalary=0
        for s in salary:
            if s != maxSalary and s != minSalary:
                AveSalary+=s
        return AveSalary/(len(salary)-2)

# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
output = Solution()
salary = [4000,3000,1000,2000]
print(output.average(salary))

# Input: salary = [1000,2000,3000]
# Output: 2000.00000
salary = [1000,2000,3000]
print(output.average(salary))
