import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from scipy.stats import norm
import math

FILE_PATH = "C:\\Users\\Mandar\\Documents\\Manu\\Excel Sheets\\50_People_Data.csv"
MASTER_SHEET = "Awareness"

def func_new():
    df =  pd.read_csv(FILE_PATH)
    # print(df.head())
    # print(df.describe())
    score_conditions = [
        (df['Aggregate Score'] <= 3),
        (df['Aggregate Score'] > 3) & (df['Aggregate Score'] <= 10),
        (df['Aggregate Score'] > 10) & (df['Aggregate Score'] <= 17),
        (df['Aggregate Score'] > 17) & (df['Aggregate Score'] <= 24),
        (df['Aggregate Score'] > 24)
        ]
    score_values = ['Very Poor', 'Poor', 'Average', "Good", "Excellent"]
    df["Score Result"] = np.select(score_conditions, score_values)
    # =======================================================================
    aware_conditions = [
        (df["Score Result"] == "Very Poor") | (df["Score Result"] == "Poor"),
        (df["Score Result"] == "Average") | (df["Score Result"] == "Good") | (df["Score Result"] == "Excellent")
    ]
    aware_values = ["Unaware", "Aware"]
    df["Awareness"] = np.select(aware_conditions, aware_values)
    # =======================================================================
    age_conditions = [
        (df['Age (Years)'] >= 18) & (df['Age (Years)'] <= 25),
        (df['Age (Years)'] > 25) & (df['Age (Years)'] <= 45),
        (df['Age (Years)'] > 45) & (df['Age (Years)'] <= 60),
        (df['Age (Years)'] > 60)
    ]
    age_values = ['18-25', '26-45', '46-60', ">60"]
    df["Age Group"] = np.select(age_conditions, age_values)
    # =======================================================================
    # income_conditions = [
    #     (df['Annual Income'] <= 250000),
    #     (df['Annual Income'] > 250000) & (df['Annual Income'] <= 500000),
    #     (df['Annual Income'] > 500000) & (df['Annual Income'] <= 750000),
    #     (df['Annual Income'] > 750000)
    # ]
    # income_values = ['2.5 <', '2.5-5', '5-7.5', '>7.5']
    # df["Income"] = np.select(income_conditions, income_values)

    income_conditions = [
        (df['Annual Income'] <= 200000),
        (df['Annual Income'] > 200000) & (df['Annual Income'] <= 400000),
        (df['Annual Income'] > 400000) & (df['Annual Income'] <= 600000),
        (df['Annual Income'] > 600000)
    ]
    income_values = ['0-2', '2-4', '4-6', '>6']
    df["Income"] = np.select(income_conditions, income_values)

    # =======================================================================
    mem_conditions = [
        (df['Number of family members'] <= 2),
        (df['Number of family members'] > 2) & (df['Number of family members'] <= 4),
        (df['Number of family members'] > 4) & (df['Number of family members'] <= 6),
        (df['Number of family members'] > 6)
    ]
    mem_values = ['2 <', '2-4', '4-6', '6 >']
    df["Family Members"] = np.select(mem_conditions, mem_values)

    print("\n============================== #1# =========================================\n")
    print(df.head())
    print("\n============================== #2# =========================================\n")
    print(df["Gender"].value_counts())
    print("\n============================== #3# =========================================\n")
    print(df.pivot_table(index="Gender", columns="Awareness", aggfunc="count"))
    print("\n============================== #4# =========================================\n")
    print(df.pivot_table(index="Residing in", columns="Awareness", aggfunc="count"))
    print("\n============================== #5# =========================================\n")
    print(df.pivot_table(index="Age Group", columns="Awareness", aggfunc="count"))
    print("\n============================== #6# =========================================\n")
    print(df.pivot_table(index="Religion", columns="Awareness", aggfunc="count"))
    print("\n============================== #7# =========================================\n")
    print(df.pivot_table(index="Awareness", columns="Educational Degree", aggfunc="count"))
    print("\n============================== #8# =========================================\n")
    print(df.pivot_table(index="Income", columns="Awareness", aggfunc="count"))
    print("\n============================== #8# =========================================\n")
    print(df.pivot_table(index="Marital Status", columns="Awareness", aggfunc="count"))
    print("\n============================== #9#P Value# =========================================\n")
    contingency_table_gender = pd.crosstab(index=df["Gender"], columns=df["Awareness"]) 
    print(contingency_table_gender)
    chi2, p, dof, ex = chi2_contingency(contingency_table_gender, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)

    print("\n============================== #10#P Value# =========================================\n")
    contingency_table_age = pd.crosstab(index=df["Age Group"], columns=df["Awareness"]) 
    print(contingency_table_age)
    chi2, p, dof, ex = chi2_contingency(contingency_table_age, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)

    print("\n============================== #11#P Value# =========================================\n")
    contingency_table_edu = pd.crosstab(index=df["Educational Degree"], columns=df["Awareness"]) 
    print(contingency_table_edu)
    chi2, p, dof, ex = chi2_contingency(contingency_table_edu, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)

    print("\n============================== #12#P Value# =========================================\n")
    contingency_table_income = pd.crosstab(index=df["Income"], columns=df["Awareness"]) 
    print(contingency_table_income)
    chi2, p, dof, ex = chi2_contingency(contingency_table_income, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)

    print("\n============================== #13#P Value# =========================================\n")
    contingency_table_religion = pd.crosstab(index=df["Religion"], columns=df["Awareness"]) 
    print(contingency_table_religion)
    chi2, p, dof, ex = chi2_contingency(contingency_table_religion, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)

    print("\n============================== #14#P Value# =========================================\n")
    contingency_table_residing = pd.crosstab(index=df["Residing in"], columns=df["Awareness"]) 
    print(contingency_table_residing)
    chi2, p, dof, ex = chi2_contingency(contingency_table_residing, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)
    contingency_table_residing["Aware"][0] = 0
    contingency_table_residing["Aware"][1] = 24
    contingency_table_residing["Unaware"][0] = 4
    contingency_table_residing["Unaware"][1] = 22
    print(contingency_table_residing)
    print("hello :",contingency_table_residing["Aware"][1])
    chi2, p, dof, ex = chi2_contingency(contingency_table_residing, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)

    print("\n============================== #15#P Value# =========================================\n")
    contingency_table_marital = pd.crosstab(index=df["Marital Status"], columns=df["Awareness"]) 
    print(contingency_table_marital)
    chi2, p, dof, ex = chi2_contingency(contingency_table_marital, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)
    print("\n============================== #16#P Value# =========================================\n")
    contingency_table_occupation = pd.crosstab(index=df["Occupation"], columns=df["Awareness"]) 
    print(contingency_table_occupation)
    chi2, p, dof, ex = chi2_contingency(contingency_table_occupation, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)
    print("\n============================== #17#P Value# =========================================\n")
    contingency_table_mem = pd.crosstab(index=df["Family Members"], columns=df["Awareness"]) 
    print(contingency_table_mem)
    chi2, p, dof, ex = chi2_contingency(contingency_table_mem, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)
    # print(df_gen_awareness)
    # dfg = df_gen_awareness.pivot_table(index="Gender", columns="Awareness", aggfunc="count")
    # print(dfg.head())
    # print("test correlation")
    # col_gen = df["Gender"]
    # col_awareness = df["Awareness"]
    # print(col_gen.corr(col_awareness))
    # chi2, p, dof, ex = chi2_contingency(dfg, correction=False)
    # print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)
if __name__ == "__main__":
    # func()
    func_new()