from dotenv import load_dotenv
import os
import pandas as pd
import gspread

# Load environment variables from .env file
load_dotenv()


def load_beer_data():
    # Generate docstring
    
    print(f"Attempting to access from {os.getenv('KEY_PATH')}")
    gc = gspread.service_account(filename=os.getenv("KEY_PATH"))
    
    gs = gc.open("Beer Database")
    print(gs)
    print(type(gs))
    
if __name__ == "__main__":
    load_beer_data()
