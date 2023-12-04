# https://leetcode.com/problems/rising-temperature/

# Write your MySQL query statement below

# SELECT w2.id
# FROM WEATHER w1
# INNER JOIN WEATHER w2 ON w1.id + 1 = w2.id
# WHERE w1.temperature < w2.temperature OR w1.recordDate > w2.recordDate
# ORDER BY w2.id

SELECT w1.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature;

