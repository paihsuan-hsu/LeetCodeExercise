-- Input: 
-- Activity table:
-- +------------+------------+---------------+-----------+
-- | machine_id | process_id | activity_type | timestamp |
-- +------------+------------+---------------+-----------+
-- | 0          | 0          | start         | 0.712     |
-- | 0          | 0          | end           | 1.520     |
-- | 0          | 1          | start         | 3.140     |
-- | 0          | 1          | end           | 4.120     |
-- | 1          | 0          | start         | 0.550     |
-- | 1          | 0          | end           | 1.550     |
-- | 1          | 1          | start         | 0.430     |
-- | 1          | 1          | end           | 1.420     |
-- | 2          | 0          | start         | 4.100     |
-- | 2          | 0          | end           | 4.512     |
-- | 2          | 1          | start         | 2.500     |
-- | 2          | 1          | end           | 5.000     |
-- +------------+------------+---------------+-----------+
-- Output: 
-- +------------+-----------------+
-- | machine_id | processing_time |
-- +------------+-----------------+
-- | 0          | 0.894           |
-- | 1          | 0.995           |
-- | 2          | 1.456           |
-- +------------+-----------------+
SELECT a1.machine_id,
    round(avg(a2.timestamp - a1.timestamp), 3) as processing_time
from Activity a1
    JOIN Activity a2 on a1.machine_id = a2.machine_id
    and a1.process_id = a2.process_id
    and a1.activity_type = 'start'
    and a2.activity_type = 'end'
GROUP BY a1.machine_id -- or
    -- Select a.machine_id,
    --     round(
    --         (
    --             Select avg(a1.timestamp)
    --             from Activity a1
    --             where a1.machine_id = a.machine_id
    --                 and a1.activity_type = 'end'
    --         ) - (
    --             Select avg(a1.timestamp)
    --             from Activity a1
    --             where a1.machine_id = a.machine_id
    --                 and a1.activity_type = 'start'
    --         ),
    --         3
    --     ) as processing_time
    -- from Activity a
    -- group by a.machine_id