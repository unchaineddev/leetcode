# https://leetcode.com/problems/find-users-with-valid-e-mails

import pandas as pd
import re

matching = "^[a-zA-Z]+[a-zA-Z-._0-9]*@leetcode.com(.?)"

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    mails = users[users.mail.str.match(matching)]
    return mails
