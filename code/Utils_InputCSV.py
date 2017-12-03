import numpy as np
import pandas as pd

def InputCSV(filename, separator=',', unit='s', columns=['all']):
    #for our case, the unit is 30 sec, since message density and content density features are extracted every 30 seconds.

    input_data = pd.DataFrame()
    
    # run this line for their data
    #input_data = pd.read_csv(filename, sep = separator)

    #changed file to excel to get rid of the utf-8 error
    try:
        input_data = pd.read_excel(filename)
    except:
        print("Unable to read")
        return None
    
    input_data.set_index(input_data.columns[0], inplace = True)
    input_data.index = pd.to_datetime(input_data.index,  unit=unit) # Convert time into DateTime format
    input_data.index.names = ['Time (' + unit +')']

    if columns != ['all'] :
        signal = pd.DataFrame(input_data[columns], input_data.index)
    else :
        signal = input_data

    return signal
