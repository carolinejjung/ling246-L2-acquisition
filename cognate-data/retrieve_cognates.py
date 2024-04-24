import pandas as pd

data = pd.read_csv("spanish_cognates_hout.csv")
data_to_write = ""
for word in list(data[1:]["English Cognate"]):
    data_to_write += word + ", "

f = open("spanish_english_cognates.txt", "w")
f.write(data_to_write)
f.close()