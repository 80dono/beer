import os
import pandas as pd
import gspread
import re
import numpy as np


def load_beer_data() -> pd.DataFrame:
    """Fetches beer data from the Google Sheet.

    Raises:
        EnvironmentError: Errors if the global variable BEER_KEY_PATH has not been set in the local environment (see `devcontainer.json`).

    Returns:
        A dataframe of beer data.
    """
    
    key_path = os.getenv('SERVICE_ACCT_CREDS')
    if key_path is None:
        raise EnvironmentError("SERVICE_ACCT_CREDS is not set in the local environment.")
    gc = gspread.service_account(filename=key_path)
    
    ws = gc.open("Beer Database").get_worksheet(0)
    data = pd.DataFrame(ws.get_all_records())
    
    # Data cleaning
    df = data.copy()
    df["ABV"] = df["ABV"].apply(lambda x: float(x.strip('%'))/100)
    # Might want to make sub_style be "{sub_style} {style}" instead of just "{sub_style}"
    df["sub_style"] = (df["Style"]
                       .apply(lambda x: re.findall(r"(?<=\()[\D\s]+(?=\)$)", x))
                       .apply(lambda x: x[0] if x else pd.NA))
     
    return df

   
if __name__ == "__main__":
    load_beer_data()
