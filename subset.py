"""
@author: Caroline Jung
Last modified: 5/9/24
"""

import pandas as pd
import matplotlib.pyplot as plt

def get_learner_data(lang, medium, prof):
    """Given the COREFL csv of learner data, output a txt file of just the concordances based on the native language, 
    if written/spoken data, and English proficiency level."""

    data = pd.read_csv(f"corefl-data/{lang}.csv", sep='\t')
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
    """Reassign CEFR proficiency levels into 3 main levels: beginner, intermediate, advanced."""
    if raw_prof == "A1 (lower beginner)" or raw_prof == "A2 (upper beginner)":
        return "beginner"
    elif raw_prof == "B1 (lower intermediate)" or raw_prof == "B2 (upper intermediate)":
        return "intermediate"
    elif raw_prof == "C1 (lower advanced)" or raw_prof == "C2 (upper advanced)":
        return "advanced"
    else:
        return "invalid"

def get_native(medium):
    """Given the COREFL csv for native speakers, output a txt file of just the concordances based on if it was written or spoken data."""
    data = pd.read_csv(f"corefl-data/natives.csv", sep='\t')
    filter_medium = data[data["Medium"] == f"{medium}"]

    final = ""
    filtered = filter_medium["Text"]
    for row in filtered:
        final += row + "\n"

    with open(f"native_{medium.lower()}.txt", "w") as file:
        file.write(final)
    file.close()
    return len(final.split(" "))

# CREATE TXT FILES
# Reference corpus (native)
get_native("Written")
get_native("Spoken")

# Target corpus (German)
get_learner_data("german", "Written", "beginner")
get_learner_data("german", "Written", "intermediate")
get_learner_data("german", "Written", "advanced")

get_learner_data("german", "Spoken", "beginner")
get_learner_data("german", "Spoken", "intermediate")
get_learner_data("german", "Spoken", "advanced")

# Target corpus (Spanish)
get_learner_data("spanish", "Written", "beginner")
get_learner_data("spanish", "Written", "intermediate")
get_learner_data("spanish", "Written", "advanced")

get_learner_data("spanish", "Spoken", "beginner")
get_learner_data("spanish", "Spoken", "intermediate")
get_learner_data("spanish", "Spoken", "advanced")