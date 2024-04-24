import regex as re
import os
import pandas as pd

def count_words(file):
    f = open(file, "r")
    data = f.readlines()
    f.close()

    num_participants = len(data)

    all_participants = ""
    for participant in data:
        all_participants += participant + " "

    count = len(re.findall(r'\w+', all_participants))
    return num_participants, count



files = os.listdir()
corpora = [file for file in files if file.endswith('.txt')]

stats = pd.DataFrame(data=corpora, columns=["filename"])

# def parse_file(filename):
#     return re.findall(r'(\w+)_(\w+)_(\w+).txt', filename)
#     # for date in pattern2.finditer(text2):
#     # print(date.group(1))
# print(parse_file("native_written.txt"))

# #stats["language"] = stats.apply(lambda x: x["filename"], axis=1)

stats["num_participants"] = stats.apply(lambda x: count_words(x["filename"])[0], axis=1)
stats["num_words"] = stats.apply(lambda x: count_words(x["filename"])[1], axis=1)
stats["num_word_per_person"] = stats.apply(lambda x: x["num_words"]/x["num_participants"] 
                                           if x["num_participants"] !=0 else 0, axis=1)

print(stats)