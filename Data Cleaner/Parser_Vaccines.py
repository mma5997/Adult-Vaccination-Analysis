import csv
CSV_FILE_REL_PATH = "../Artifacts/CSV_Generated/vaccine.csv"
INPUT = "../Artifacts/TXT_Input/inputVaccine.txt"

COLUMN_HEADERS = list(["Have you heard of this vaccine? (Yes/No)", 
                        "Do you know whether this vaccine is taken in adults or not? (Yes/No)",
                        "Do you know in which condition is this vaccine applicable? (Yes/No)",
                        "Have you taken this vaccine? (Yes/No)",
                        "Reason for not taking the vaccine"])

HAVE_HEARD_OF_VACCINE = "Have you heard of this vaccine"
KNOW_VACCINE_TAKEN_IN_ADULTS = "Do you know whether this vaccine is taken in adults"
KNOW_CONDITION_OF_TAKING_VACCINE = "Do you know in which condition is this vaccine applicable"
HAVE_TAKEN_VACCINE = "Have you taken this vaccine"
REASON_NOT_TAKING_VACCINE = "Reason for not taking the vaccine"

NOT_RECOMMENDED_BY_DOCTOR = "Not recommended by doctor"
COST_OF_VACCINE = "Cost of vaccine"
ANY_OTHER = "Any other"
UNAWARE = "Unaware"
NOT_AVAILABLE = "Not available easily"

def parse():

    # creating a file and writing column header as first row
    with open(CSV_FILE_REL_PATH, 'w',newline='') as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(COLUMN_HEADERS)

    print("Parsing Started")
    
    # Reading file 
    file = open(INPUT, 'r')
    Lines = file.readlines()

    # Strips the newline character
    count=0
    for line in Lines:
        count += 1
        # print("Line{}: {}".format(count, line.strip()))
        with open(CSV_FILE_REL_PATH, 'a', newline='') as fp:
            heardOfVaccine = "No"
            knowVaccineTakenInAdults = "No"
            knowConditionForTakingVaccine = "No"
            takenVaccine = "No"
            reason = None

            writer = csv.writer(fp, delimiter=",")
            splitLine = line.split(';')
            for item in splitLine:
                if HAVE_HEARD_OF_VACCINE in item and "Yes" in item:
                    heardOfVaccine = "Yes"
                elif KNOW_VACCINE_TAKEN_IN_ADULTS in item and "Yes" in item:
                    knowVaccineTakenInAdults = "Yes"
                elif KNOW_CONDITION_OF_TAKING_VACCINE in item and "Yes" in item:
                    knowConditionForTakingVaccine = "Yes"
                elif HAVE_TAKEN_VACCINE in item and "Yes" in item:
                    takenVaccine = "Yes"
                elif REASON_NOT_TAKING_VACCINE in item:
                    if UNAWARE in item:
                        reason = UNAWARE
                    elif NOT_RECOMMENDED_BY_DOCTOR in item:
                        reason = NOT_RECOMMENDED_BY_DOCTOR
                    elif COST_OF_VACCINE in item:
                        reason = COST_OF_VACCINE
                    elif NOT_AVAILABLE in item:
                        reason = NOT_AVAILABLE
                    elif ANY_OTHER in item:
                        reason = ANY_OTHER
            
            if takenVaccine == "Yes":
                reason = "N/A"

            if knowVaccineTakenInAdults == "Yes":
                heardOfVaccine = "Yes"

            if knowConditionForTakingVaccine == "Yes":
                heardOfVaccine = "Yes"

            if heardOfVaccine == "No" and knowVaccineTakenInAdults == "No" and knowConditionForTakingVaccine == "No" and takenVaccine == "No":
                reason = "Unaware"

            if reason is None:
                if heardOfVaccine == "Yes" and knowVaccineTakenInAdults == "Yes" and knowConditionForTakingVaccine == "Yes":
                    reason = ANY_OTHER
                else:
                    reason = UNAWARE
            
            data = list([heardOfVaccine, knowVaccineTakenInAdults, knowConditionForTakingVaccine, takenVaccine, reason])
            writer.writerow(data)

    print("Parsing ended and parsed ", count, " lines in total")

if __name__ == "__main__":
    print("Hello here")
    parse()
