"""
Polars (9): Banking Churn


1. Label Age based on: -

-------------------------------------------
| Age Range (Years) | Age Group           |
|-------------------|---------------------|
| ≤ 17             | Children/Teenagers   |
| 18 - 24          | Young Adults         |
| 25 - 34          | Adults               |
| 35 - 44          | Middle-Aged Adults   |
| 45 - 54          | Older Adults         |
| 55 - 64          | Pre-Retirement       |
| ≥ 65             | Seniors              |
-------------------------------------------

2. Label Credit Score based on: -

HINT: Find mean using .describe() method

-------------------------------------------
| Credit Score Range | Credit Score Label |
|--------------------|--------------------|
| < Credit Score Mean| Low                |
| ≥ Credit Score Mean| High               |
-------------------------------------------

3. Label Salary based on: -

HINT: Find Quartile using .describe() method

------------------------==---------------------
| Salary Range           | Salary Label       |
|------------------------|--------------------|
| < Salary 25% Quartile  | Low                |
| <= Salary 50% Quartile | Medium             |
| > Salary 50% Quartile  | High               |
-----------------------------------------------

4. Use Aggregation to provide data as below: -

Churn Rate = Exited / Total Customers

Expected Output: -

Data:
-----------------------------------------------------
| Credit Score Label | Exited | Total  | Churn Rate |
|--------------------|--------|--------|------------|
| Low                | 18335  | 81023  | 0.226294   |
| High               | 16586  | 84011  | 0.197427   |
-----------------------------------------------------


Data:
--------------------------------------------------------------------
| Salary Label | Credit Score Label | Exited | Total  | Churn Rate |
|--------------|--------------------|--------|--------|------------|
| High         | Low                | 9566   | 40693  | 0.235077   |
| Medium       | High               | 3982   | 21167  | 0.188123   |
| Low          | High               | 4118   | 21018  | 0.195927   |
| High         | High               | 8486   | 41826  | 0.202888   |
| Medium       | Low                | 4310   | 20096  | 0.214471   |
| Low          | Low                | 4459   | 20234  | 0.220372   |
--------------------------------------------------------------------


Data:
--------------------------------------------------------
| Age Group           | Exited | Total  | Churn Rate   |
|---------------------|--------|--------|--------------|
| Seniors             | 412    | 1971   | 0.209031     |
| Young Adults        | 504    | 4986   | 0.101083     |
| Pre-Retirement      | 3964   | 7506   | 0.528111     |
| Older Adults        | 12189  | 22199  | 0.549079     |
| Adults              | 4494   | 55681  | 0.080710     |
| Middle-Aged Adults  | 13358  | 72691  | 0.183764     |
--------------------------------------------------------

"""