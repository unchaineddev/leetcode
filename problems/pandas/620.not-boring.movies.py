# https://leetcode.com/problems/not-boring-movies/

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema.loc[(cinema['description'] != "boring") & (cinema["id"] % 2 != 0)].sort_values(by=["rating"], ascending=False)
    
