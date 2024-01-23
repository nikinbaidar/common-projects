"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
'name' is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the
continent to which it belongs, its area, the population, and its GDP value.

A country is big if:
    * it has an area of at least three million (i.e. $3000000 km^2$), or
    * it has a population of at leat twenty-five million (i.e., 25000000)

Write a solution to find the name, population, and are of the *big countries*

Return the result in *any order*

Example

Input: 
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
Output: 
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
"""

import pandas as pd

def big_contries(world: pd.DataFrame) -> pd.DataFrame:
    x = world[(world['area'] >= 25000000) | (world['population'] >= 3000000)]
    desired_columns = ['name', 'area', 'population']
    return x.loc[:, desired_columns]


