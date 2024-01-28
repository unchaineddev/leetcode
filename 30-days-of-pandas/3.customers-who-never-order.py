import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df1 = pd.merge(customers, orders,  left_on='id', right_on='customerId', how='left')
    df1.rename(columns = {"name": "Customers"}, inplace=True)
    df2 = df1.loc[df1['customerId'].isnull(), ['Customers']]
    return df2
