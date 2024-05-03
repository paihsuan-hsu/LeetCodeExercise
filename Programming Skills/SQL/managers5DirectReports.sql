-- Input: 
-- Employee table:
-- +-----+-------+------------+-----------+
-- | id  | name  | department | managerId |
-- +-----+-------+------------+-----------+
-- | 101 | John  | A          | null      |
-- | 102 | Dan   | A          | 101       |
-- | 103 | James | A          | 101       |
-- | 104 | Amy   | A          | 101       |
-- | 105 | Anne  | A          | 101       |
-- | 106 | Ron   | B          | 101       |
-- +-----+-------+------------+-----------+
-- Output: 
-- +------+
-- | name |
-- +------+
-- | John |
-- +------+
Select name
From Employee
Where id in (
        Select managerId
        From Employee
        GROUP BY managerId
        HAVING COUNT(*) >= 5
    ) -- 
    -- -- Try Join
    -- Select e1.name
    -- from Employee e1
    --     JOIN Employee e2 ON e1.id = e2.managerId
    -- GROUP BY e1.managerId
    -- Having COUNT(*) >= 5
Select e1.name
from Employee e1
    Inner join Employee e2 ON e1.id = e2.managerId
GROUP BY e2.managerId
Having COUNT(*) >= 5