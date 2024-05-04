# https://leetcode.com/problems/rank-scores/

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values(by='score', ascending=False, inplace=True)
    # scores = scores.groupby(by='score')
    
    scores['rank']=(scores['score'].rank(method='dense',ascending=False))

    return scores[['score', 'rank']]
 
