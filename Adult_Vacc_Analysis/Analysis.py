import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from scipy.stats import norm
import math

FILE_PATH = "C:\\Users\\Mandar\\Documents\\Manu\\Excel Sheets\\FinalClean_1.csv"
Seven_Vaccine_Score = "Seven Vaccine Score"
# Stongly agree perception
sa_perception = [   "To get vaccinated is better than to get diseased",
                    "I need to take vaccine before international travel"
]
# Strongly disagree perception
sda_perception = [  "Vaccines are recommended only or children, adults don't need it",
                    "Only those at high risk should take the vaccines",
                    "There are no side effects of taking vaccine",
                    "There are no contraindications for taking vaccines",
                    "I should take vaccine even if I have contraindication, as I need to travel internationally",
                    "I can take vaccine even if I have fever",
                    "I am absolutely safe after taking vaccine i.e. I will not get disease at all for which I am vaccinated",
                    "I am safe even if I don't take all scheduled doses of recommended vaccines"
] 

P_1_Q = "To get vaccinated is better than to get diseased"
P_1 = "P_1"

P_2_Q = "Vaccines are recommended only or children, adults don't need it"
P_2 = "P_2"

P_3_Q = "Only those at high risk should take the vaccines"
P_3 = "P_3"

P_4_Q = "There are no side effects of taking vaccine"
P_4 = "P_4"

P_5_Q = "I need to take vaccine before international travel"
P_5 = "P_5"

P_6_Q = "There are no contraindications for taking vaccines"
P_6 = "P_6"

P_7_Q = "I should take vaccine even if I have contraindication, as I need to travel internationally"
P_7 = "P_7"

P_8_Q = "I can take vaccine even if I have fever"
P_8 = "P_8"

P_9_Q = "I am absolutely safe after taking vaccine i.e. I will not get disease at all for which I am vaccinated"
P_9 = "P_9"

P_10_Q = "I am safe even if I don't take all scheduled doses of recommended vaccines"
P_10 = "P_10"

SA = "Strongly agree"
A = "Agree"
DK = "Don't know"
D = "Disagree"
SD = "Strongly disagree"


F_1_Q = "My doctor's recommendation"
F_1 = "F_1"

F_2_Q = "Knowing why I should get vaccines"
F_2 = "F_2"

F_3_Q = "Knowing which vaccines I need"
F_3 = "F_3"

F_4_Q = "Cost of vaccines"
F_4 = "F_4"

F_5_Q = "Concern of getting sick if I get vaccinated"
F_5 = "F_5"

F_6_Q = "Trust in Govt. agency's recommendation"
F_6 = "F_6"

F_7_Q = "Worry about other ingredients in vaccines (chemicals or foods, such as pork or eggs)"
F_7 = "F_7"

F_8_Q = "My family or cultural beliefs"
F_8 = "F_8"

F_9_Q = "The time it takes to get vaccinated"
F_9 = "F_9"

F_10_Q = "My access to reliable transportation"
F_10 = "F_10"

F_11_Q = "My religious beliefs"
F_11 = "F_11"

F_12_Q = "My dislike or fear of needles"
F_12 = "F_12"

F_13_Q = "Belief that getting the disease will give me better immunity"
F_13 = "F_13"

F_14_Q = "Belief that I am healthy and won't need vaccine"
F_14 = "F_14"

F_15_Q = "Preference for alternative medicine"
F_15 = "F_15"

F_16_Q = "Social media, TV, newspaper"
F_16 = "F_16"

F_17_Q = "Peer pressure (Friends, Family, Relatives)"
F_17 = "F_17"

F_18_Q = "Lack of co-ordinated immunization programs for adults"
F_18 = "F_18"

# sa_points = {
#     "Strongly agree" : ,
#     "Agree" : ,
#     "Don't know" : ,
#     "Disagree" : ,
#     "Strongly disagree" : 
# } 

def func_new():
    df =  pd.read_csv(FILE_PATH)
    # print(df.head())
    # print(df.describe())

    #  This is for 18 vaccines
    # score_conditions = [
    #     (df['Aggregate Score'] <= 12),
    #     (df['Aggregate Score'] > 12) & (df['Aggregate Score'] <= 27),
    #     (df['Aggregate Score'] > 27) & (df['Aggregate Score'] <= 42),
    #     (df['Aggregate Score'] > 42) & (df['Aggregate Score'] <= 57),
    #     (df['Aggregate Score'] > 57)
    #     ]

    # This is for 7 vaccines
    score_conditions = [
        (df['Seven Vaccine Score'] <= 3),
        (df['Seven Vaccine Score'] > 3) & (df['Seven Vaccine Score'] <= 10),
        (df['Seven Vaccine Score'] > 10) & (df['Seven Vaccine Score'] <= 17),
        (df['Seven Vaccine Score'] > 17) & (df['Seven Vaccine Score'] <= 24),
        (df['Seven Vaccine Score'] > 24)
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
    income_values = ['2L or less', '2L to 4L', '4L to 6L', '6L or more']
    df["Income"] = np.select(income_conditions, income_values)

    # =======================================================================
    mem_conditions = [
        (df['Number of family members'] <= 2),
        (df['Number of family members'] > 2) & (df['Number of family members'] <= 4),
        (df['Number of family members'] > 4) & (df['Number of family members'] <= 6),
        (df['Number of family members'] > 6)
    ]
    mem_values = ['2 or less', '2 to 4', '4 to 6', '6 or more']
    df["Family Members"] = np.select(mem_conditions, mem_values)

    # =======================================================================

    perception_conditions_1 = [
        (df[P_1_Q] == SA),
        (df[P_1_Q] == A),
        (df[P_1_Q] == DK),
        (df[P_1_Q] == D),
        (df[P_1_Q] == SD),
    ]
    perception_values_1 = [5, 4, 3, 2, 1]
    df[P_1] = np.select(perception_conditions_1, perception_values_1)

    # =======================================================================

    perception_conditions_2 = [
        (df[P_2_Q] == SA),
        (df[P_2_Q] == A),
        (df[P_2_Q] == DK),
        (df[P_2_Q] == D),
        (df[P_2_Q] == SD),
    ]
    perception_values_2 = [1, 2, 3, 4, 5]
    df[P_2] = np.select(perception_conditions_2, perception_values_2)

    # =======================================================================

    perception_conditions_3 = [
        (df[P_3_Q] == SA),
        (df[P_3_Q] == A),
        (df[P_3_Q] == DK),
        (df[P_3_Q] == D),
        (df[P_3_Q] == SD),
    ]
    perception_values_3 = [1, 2, 3, 4, 5]
    df[P_3] = np.select(perception_conditions_3, perception_values_3)

    # =======================================================================
    
    perception_conditions_4 = [
        (df[P_4_Q] == SA),
        (df[P_4_Q] == A),
        (df[P_4_Q] == DK),
        (df[P_4_Q] == D),
        (df[P_4_Q] == SD),
    ]
    perception_values_4 = [1, 2, 3, 4, 5]
    df[P_4] = np.select(perception_conditions_4, perception_values_4)
    
    # =======================================================================
    
    perception_conditions_5 = [
        (df[P_5_Q] == SA),
        (df[P_5_Q] == A),
        (df[P_5_Q] == DK),
        (df[P_5_Q] == D),
        (df[P_5_Q] == SD),
    ]
    perception_values_5 = [5, 4, 3, 2, 1]
    df[P_5] = np.select(perception_conditions_5, perception_values_5)
    
    # =======================================================================
    
    perception_conditions_6 = [
        (df[P_6_Q] == SA),
        (df[P_6_Q] == A),
        (df[P_6_Q] == DK),
        (df[P_6_Q] == D),
        (df[P_6_Q] == SD),
    ]
    perception_values_6 = [1, 2, 3, 4, 5]
    df[P_6] = np.select(perception_conditions_6, perception_values_6)
    
    # =======================================================================
    
    perception_conditions_7 = [
        (df[P_7_Q] == SA),
        (df[P_7_Q] == A),
        (df[P_7_Q] == DK),
        (df[P_7_Q] == D),
        (df[P_7_Q] == SD),
    ]
    perception_values_7 = [1, 2, 3, 4, 5]
    df[P_7] = np.select(perception_conditions_7, perception_values_7)
    
    # =======================================================================

    perception_conditions_8 = [
        (df[P_8_Q] == SA),
        (df[P_8_Q] == A),
        (df[P_8_Q] == DK),
        (df[P_8_Q] == D),
        (df[P_8_Q] == SD),
    ]
    perception_values_8 = [1, 2, 3, 4, 5]
    df[P_8] = np.select(perception_conditions_8, perception_values_8)
    
    # =======================================================================

    perception_conditions_9 = [
        (df[P_9_Q] == SA),
        (df[P_9_Q] == A),
        (df[P_9_Q] == DK),
        (df[P_9_Q] == D),
        (df[P_9_Q] == SD),
    ]
    perception_values_9 = [1, 2, 3, 4, 5]
    df[P_9] = np.select(perception_conditions_9, perception_values_9)
    
    # =======================================================================
    
    perception_conditions_10 = [
        (df[P_10_Q] == SA),
        (df[P_10_Q] == A),
        (df[P_10_Q] == DK),
        (df[P_10_Q] == D),
        (df[P_10_Q] == SD),
    ]
    perception_values_10 = [1, 2, 3, 4, 5]
    df[P_10] = np.select(perception_conditions_10, perception_values_10)
    
    # =======================================================================

    df["Perception Score"] = df[P_1] + df[P_2] + df[P_3] + df[P_4] + df[P_5] + df[P_6] + df[P_7] + df[P_8] + df[P_9] + df[P_10]

    # =======================================================================
    
    perception_conditions_final = [
        (df["Perception Score"] <= 15),
        (df["Perception Score"] > 15) & (df["Perception Score"] <= 25),
        (df["Perception Score"] > 25) & (df["Perception Score"] <= 35),
        (df["Perception Score"] > 35) & (df["Perception Score"] <= 45),
        (df["Perception Score"] > 45)
    ]

    # perception_values_final = ["Very Negative Perception", "Negative Perception", "Neutral", "Positive Perception", "Very Positive Perception"]
    perception_values_final = ["VNP", "NP", "N", "PP", "VPP"]
    df["Perception Result"] = np.select(perception_conditions_final, perception_values_final)

    # =======================================================================
    
    print("\n============================== #1# =========================================\n")
    print(df.head())
    print("\n============================== #2# =========================================\n")
    print(df["Gender"].value_counts())
    print("\n============================== #3# =========================================\n")
    # print(df.pivot_table(index="Gender", columns="Awareness", aggfunc="count"))
    print(df["Residing in"].value_counts())
    print("\n============================== #4# =========================================\n")
    # print(df.pivot_table(index="Residing in", columns="Awareness", aggfunc="count"))
    print(df["Age Group"].value_counts())
    print("\n============================== #5# =========================================\n")
    # print(df.pivot_table(index="Age Group", columns="Awareness", aggfunc="count"))
    print(df["Religion"].value_counts())
    print("\n============================== #6# =========================================\n")
    # print(df.pivot_table(index="Religion", columns="Awareness", aggfunc="count"))
    print(df["Awareness"].value_counts())
    print("\n============================== #7# =========================================\n")
    # print(df.pivot_table(index="Awareness", columns="Educational Degree", aggfunc="count"))
    print(df["Income"].value_counts())
    print("\n============================== #8# =========================================\n")
    # print(df.pivot_table(index="Income", columns="Awareness", aggfunc="count"))
    print(df["Marital Status"].value_counts())
    print("\n============================== #8# =========================================\n")
    # print(df.pivot_table(index="Marital Status", columns="Awareness", aggfunc="count"))
    print(df["Educational Degree"].value_counts())

    print(df["Occupation"].value_counts())

    print(df["Family Members"].value_counts())
    
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
    # contingency_table_residing["Aware"][0] = 0
    # contingency_table_residing["Aware"][1] = 24
    # contingency_table_residing["Unaware"][0] = 4
    # contingency_table_residing["Unaware"][1] = 22
    # print(contingency_table_residing)
    # print("hello :",contingency_table_residing["Aware"][1])
    # chi2, p, dof, ex = chi2_contingency(contingency_table_residing, correction=False)
    # print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)

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

    # ============== PERCEPTION TABLES ===============
    print("\n============================== #18#P Value# #1 Perception =========================================\n")
    contingency_table = pd.crosstab(index=df["Gender"], columns=df["Perception Result"]) 
    print(contingency_table.to_markdown())
    chi2, p, dof, ex = chi2_contingency(contingency_table, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)

    # Writing the dataframe to csv
    df.to_csv("C:\\Users\\Mandar\\Desktop\\PythonPrj\\Adult_Vacc_Analysis\\temp.csv", encoding='utf-8')

    print("\n============================== #19#P Value# #2 Perception =========================================\n")
    contingency_table = pd.crosstab(index=df["Age Group"], columns=df["Perception Result"]) 
    print(contingency_table.to_markdown())
    chi2, p, dof, ex = chi2_contingency(contingency_table, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)

    print("\n============================== #20#P Value# #3 Perception =========================================\n")
    contingency_table = pd.crosstab(index=df["Educational Degree"], columns=df["Perception Result"]) 
    print(contingency_table.to_markdown())
    chi2, p, dof, ex = chi2_contingency(contingency_table, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)

    print("\n============================== #21#P Value# #4 Perception =========================================\n")
    contingency_table = pd.crosstab(index=df["Income"], columns=df["Perception Result"]) 
    print(contingency_table.to_markdown())
    chi2, p, dof, ex = chi2_contingency(contingency_table, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)

    print("\n============================== #22#P Value# #5 Perception =========================================\n")
    contingency_table = pd.crosstab(index=df["Religion"], columns=df["Perception Result"]) 
    print(contingency_table.to_markdown())
    chi2, p, dof, ex = chi2_contingency(contingency_table, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)


    print("\n============================== #23#P Value# #6 Perception =========================================\n")
    contingency_table = pd.crosstab(index=df["Residing in"], columns=df["Perception Result"]) 
    print(contingency_table.to_markdown())
    chi2, p, dof, ex = chi2_contingency(contingency_table, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)


    print("\n============================== #24#P Value# #7 Perception =========================================\n")
    contingency_table = pd.crosstab(index=df["Marital Status"], columns=df["Perception Result"]) 
    print(contingency_table.to_markdown())
    chi2, p, dof, ex = chi2_contingency(contingency_table, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)

    
    print("\n============================== #25#P Value# #8 Perception =========================================\n")
    contingency_table = pd.crosstab(index=df["Occupation"], columns=df["Perception Result"]) 
    print(contingency_table.to_markdown())
    chi2, p, dof, ex = chi2_contingency(contingency_table, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)


    print("\n============================== #26#P Value# #9 Perception =========================================\n")
    contingency_table = pd.crosstab(index=df["Family Members"], columns=df["Perception Result"]) 
    print(contingency_table.to_markdown())
    chi2, p, dof, ex = chi2_contingency(contingency_table, correction=False)
    print("Chi : ",chi2, " , P Value : ",'{:.10f}'.format(p), " , DOF : ", dof, " , EX : ", ex)





    print("\n============================== #29#P Value# #2 Perception =========================================\n")

    print(df['Perception Result'].value_counts())

    print("\n============================== #30#P Value# #3 Perception =========================================\n")

    # print(df[P_1_Q].value_counts())

    p1 = df[P_1_Q].value_counts()
    p2 = df[P_2_Q].value_counts()
    p3 = df[P_3_Q].value_counts()
    p4 = df[P_4_Q].value_counts()
    p5 = df[P_5_Q].value_counts()
    p6 = df[P_6_Q].value_counts()
    p7 = df[P_7_Q].value_counts()
    p8 = df[P_8_Q].value_counts()
    p9 = df[P_9_Q].value_counts()
    p10 = df[P_10_Q].value_counts()
    
    print(pd.concat([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10], axis =1).T.to_markdown())

    print("\n============================== #31#P Value# #Factors =========================================\n")

    f1 = df[F_1_Q].value_counts()
    f2 = df[F_2_Q].value_counts()
    f3 = df[F_3_Q].value_counts()
    f4 = df[F_4_Q].value_counts()
    f5 = df[F_5_Q].value_counts()
    f6 = df[F_6_Q].value_counts()
    f7 = df[F_7_Q].value_counts()
    f8 = df[F_8_Q].value_counts()
    f9 = df[F_9_Q].value_counts()
    f10 = df[F_10_Q].value_counts()
    f11 = df[F_11_Q].value_counts()
    f12 = df[F_12_Q].value_counts()
    f13 = df[F_13_Q].value_counts()
    f14 = df[F_14_Q].value_counts()
    f15 = df[F_15_Q].value_counts()
    f16 = df[F_16_Q].value_counts()
    f17 = df[F_17_Q].value_counts()
    f18 = df[F_18_Q].value_counts()

    print(pd.concat([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18], axis =1).T.to_markdown())

    # print(p1.join(p2))
if __name__ == "__main__":
    # func()
    func_new()