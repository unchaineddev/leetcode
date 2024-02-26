import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[(views.author_id == views.viewer_id)]
    df = df[['author_id']] 
    df = df.sort_values(by=['author_id'], ascending=True).drop_duplicates()
    df = df.rename(columns={'author_id': 'id'})
    return df
