# https://leetcode.com/problems/calculate-special-bonus/

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees.apply(lambda employees: employees["salary"]  if employees["employee_id"] % 2 != 0 and not employees['name'].startswith("M") else 0, axis=1)

    return employees[["employee_id", "bonus"]].sort_values(by=["employee_id"])
