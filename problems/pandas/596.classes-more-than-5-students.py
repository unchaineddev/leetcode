# https://leetcode.com/problems/classes-more-than-5-students/

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # class_counts = courses.groupby('class')['student'].nunique()
    # result_classes = class_counts[class_counts >= 5].index
    # result_df = pd.DataFrame(result_classes, columns=['class'])
    # return result_df
    df = courses.groupby('class').count().reset_index()
    return df[df['student'] >=5][['class']]
