# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employee_uni, on='id', how='left')
    df.rename({"id": "unique_id"}, inplace=True)
    return df[["unique_id" ,'name']]
