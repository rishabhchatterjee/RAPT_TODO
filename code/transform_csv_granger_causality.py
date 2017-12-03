import pandas as pd 

path = "2013_behavior_transcript_full.xls"

def readFile(path):
    try:
        print("\nReading file...\n")
        return pd.read_excel(path)
    except:
        print("\nUnable to read...\n")

df = readFile(path)
print("\nFile read.\n")

print("\nReplacing NaN values with 0\n")

count = 0
for col in df:
    print(col, end = " ")
    if count < 3:
        count += 1
        continue
    else:
        df[col].fillna(0, inplace = True)

print("\nNaN values replaced.\n")

print("\nReplacing x with a 1\n")

for index, row in df.iterrows():
    count = 0
    for col in df:
        if count < 3:
            count += 1
            continue
        else:
            if row[col] == "x":
                row[col] = 1
                print(row[col], end = " ")

print("\nx repalced.\n")

print("\nCreating new csv file")

df.to_csv("2013_data_GC.csv", sep = ",")
# still have to replace xs with 1 for some reason 
# just use replace feature in excel
print("\nFile created.\n")
