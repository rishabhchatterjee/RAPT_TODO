import pandas as pd 

def getDict():

    # for some reason csv not reading but excel file has same col names
    path = '2013_behavior_transcript_full.xls'
    df = pd.read_excel(path)

    names = {}
    count = 0
    for col in df:
        if count < 3:
            count += 1
            continue
        else:
            names[count -2] = col
            count += 1
    return names

