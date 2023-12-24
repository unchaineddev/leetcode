# https://leetcode.com/problems/get-the-size-of-a-dataframe/

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows, columns = players.shape
    return [rows, columns]

    # alternative solution
    # return list(players.shape)
    
