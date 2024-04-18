import pandas as pd
import matplotlib.pyplot as plt

def get_data(file, lang, medium, prof):
    data = pd.read_csv(f"corefl-data/{file}", sep='\t')
    filter_medium = data[data["Medium"] == f"{medium}"]

    # group proficiencies into beginner, intermediate, advanced 
    if medium=="Written":
        filter_medium["proficiency"] = filter_medium["Proficiency (self-assessment) writing"].map(reassign_proficiency)
    elif medium=="Spoken":
        filter_medium["proficiency"] = filter_medium["Proficiency (self-assessment) speaking"].map(reassign_proficiency)
    else:
        print("Not a valid medium.")
    
    final = ""
    filtered = filter_medium[filter_medium["proficiency"] == f"{prof.lower()}"]["Text"]
    for row in filtered:
        final += row + "\n"

    with open(f"{lang}_{medium.lower()}_{prof}.txt", "w") as file:
        file.write(final)
    file.close()

    return len(final.split(" "))

def reassign_proficiency(raw_prof):
    if raw_prof == "A1 (lower beginner)" or raw_prof == "A2 (upper beginner)":
        return "beginner"
    elif raw_prof == "B1 (lower intermediate)" or raw_prof == "B2 (upper intermediate)":
        return "intermediate"
    elif raw_prof == "C1 (lower advanced)" or raw_prof == "C2 (upper advanced)":
        return "advanced"
    else:
        return "invalid"


def get_native(file, medium):
    data = pd.read_csv(f"corefl-data/{file}", sep='\t')
    filter_medium = data[data["Medium"] == f"{medium}"]

    # group proficiencies into beginner, intermediate, advanced 
    final = ""
    filtered = filter_medium["Text"]
    for row in filtered:
        final += row + "\n"

    with open("native_written.txt", "w") as file:
        file.write(final)
    file.close()
    return len(final.split(" "))


#currently, the only data we have is german
#print(get_data("learners_chaplin.csv", "german", "Spoken", "advanced"))
#print(get_native("natives_chaplin.csv", "Spoken")) #native_chap_spoken.txt


print(get_data("learners_chaplin.csv", "german", "Written", "beginner"))
print(get_native("natives_chaplin.csv", "Written")) #native_chap_spoken.txt