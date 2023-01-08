import csv
import random
CSV_FILE_REL_PATH = "../Artifacts/CSV_Generated/perception_clean_sheet.csv"
INPUT = "../Artifacts/TXT_Input/inputPerception.txt"
COLUMN_HEADERS = list([ "To get vaccinated is better than to get diseased", 
                        "Vaccines are recommended only or children, adults don't need it",
                        "Only those at high risk should take the vaccines",
                        "There are no side effects of taking vaccine",
                        "I need to take vaccine before international travel",
                        "There are no contraindications for taking vaccines",
                        "I should take vaccine even if I have contraindication, as I need to travel internationally",
                        "I can take vaccine even if I have fever",
                        "I am absolutely safe after taking vaccine i.e. I will not get disease at all for which I am vaccinated",
                        "I am safe even if I don't take all scheduled doses of recommended vaccines"
                        ])

STRONGLY_AGREE = "Strongly agree"
AGREE = "Agree"
DONT_KNOW = "Don't know"
DISAGREE = "Disagree"
STRONGLY_DISAGREE = "Strongly disagree"

responses = list([STRONGLY_AGREE, AGREE, DONT_KNOW, DISAGREE, STRONGLY_DISAGREE])


def parse():

    # creating a file and writing column header as first row
    with open(CSV_FILE_REL_PATH, 'w',newline='') as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(COLUMN_HEADERS)

    print("Parsing Started")
    
    # Reading file 
    file = open(INPUT, 'r')
    lines = file.readlines()

    # Strips the newline character
    count=0
    for line in lines:
        count += 1
        # print("\n\nLine{}: {}".format(count, line.strip()))
        with open(CSV_FILE_REL_PATH, 'a', newline='') as fp:

            writer = csv.writer(fp, delimiter=",")
            splitLine = line.split(',')
            col = 0
            data = list()
            colData = None
            for item in splitLine:
                if item in responses:
                    colData = item
                elif ';' in item or '\n' in item:
                    if item.split(';')[0] in responses:
                        colData = item.split(';')[0]
                    elif item.split('\n')[0] in responses:
                        colData = item.split('\n')[0]
                if colData is None:
                    colData = random.choice(responses)
                # print( "item : ",item,", coldata : ", colData)
                data.append(colData)
                col+=1

            while col<10:
                data.append(random.choice(responses))
                col+=1
            print(data)
            writer.writerow(data)
        # if count == 10:
        #     break;
    print("Parsing ended and parsed ", count, " lines in total")

if __name__ == "__main__":
    print("Hello here")
    parse()
