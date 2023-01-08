import pandas as pd
import numpy as np

FILE_PATH = "C:\\Users\\Mandar\\Documents\\Manu\\Excel Sheets\\50 Vaccines.csv"
MASTER_SHEET = "Awareness"

def func_new():
    df =  pd.read_csv(FILE_PATH)
    # print(df.head())
    # print(df.describe())
    score_conditions = [
        (df['Aggregate Score'] <2),
        (df['Aggregate Score'] >= 2)
        ]
    score_values = ["Unaware", "Aware"]
    df["Awareness"] = np.select(score_conditions, score_values)
    print(df["Awareness"].value_counts())
if __name__ == "__main__":
    # func()
    func_new()