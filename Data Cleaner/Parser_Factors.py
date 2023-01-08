import csv
import random
CSV_FILE_REL_PATH = "../Artifacts/CSV_Generated/factors_clean_sheet.csv"
INPUT = "../Artifacts/TXT_Input/inputFactors.txt"
COLUMN_HEADERS = list([ "My doctor's recommendation", 
                        "Knowing why I should get vaccines",
                        "Knowing which vaccines I need",
                        "Cost of vaccines",
                        "Concern of getting sick if I get vaccinated",
                        "Trust in Govt. agency's recommendation",
                        "Worry about other ingredients in vaccines (chemicals or foods, such as pork or eggs)",
                        "My family or cultural beliefs",
                        "The time it takes to get vaccinated",
                        "My access to reliable transportation",
                        "My religious beliefs",
                        "My dislike or fear of needles",
                        "Belief that getting the disease will give me better immunity",
                        "Belief that I am healthy and won't need vaccine",
                        "Preference for alternative medicine",
                        "Social media, TV, newspaper",
                        "Peer pressure (Friends, Family, Relatives)",
                        "Lack of co-ordinated immunization programs for adults"
                        ])

VERY_LIKELY = "Very Likely"
SOMEWHAT_LIKELY = "Somewhat Likely"
NEUTRAL = "Neutral"
NOT_VERY_LIKELY = "Not Very Likely"
NOT_AT_ALL_LIKELY = "Not At All Likely"

responses = list([VERY_LIKELY, SOMEWHAT_LIKELY, NEUTRAL, NOT_VERY_LIKELY, NOT_AT_ALL_LIKELY])


def parse():

    # creating a file and writing column header as first row
    with open(CSV_FILE_REL_PATH, 'w',newline='') as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(COLUMN_HEADERS)

    print("Parsing Started")
    
    # Reading file 
    file = open(INPUT, 'r')
    lines = file.readlines()

    print(lines[0])
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
