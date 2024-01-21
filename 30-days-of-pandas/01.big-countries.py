# https://leetcode.com/problems/big-countries/

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world.loc[(world.area >= 3000000) | (world.population >= 25000000),["name", "population", "area"]]
    return df
