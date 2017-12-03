import pandas as pd
import numpy as np

def readFile(path):
    try:
        print("\nReading file...\n")
        return pd.read_excel(path)
    except:
        print("\nUnable to read...\n")

path = "2013_behavior_transcript_full.xls"

df = readFile(path)
print("\nFile read.\n")

# takes time in splitTime format and returns duration in (min, sec)
def durationTime(times):
    if times[0] == times[2]:
        return (0, times[3] - times[1])
    else:
        return (times[2] - times[0], 60 + times[3] - times[1])

# takes start and end times as string and returns min, sec of each time
def splitTime(t1, t2): 
    time1 = t1.split(":")
    time2 = t2.split(":")

    t1_min = int(time1[1])
    t1_sec = int(time1[2][:2])

    t2_min = int(time2[1])
    t2_sec = int(time2[2][:2])

    return (t1_min, t1_sec, t2_min, t2_sec)

def gaze_presence_analysis():
    tutee_partner = {}
    tutee_worksheet = {}
    for index,row in df.iterrows():
        if row["Gaze_Partner_Tutee"] == "x":
            if row["Rapport Rating"] in tutee_partner:
                tutee_partner[row["Rapport Rating"]] += 1
            else:
                tutee_partner[row["Rapport Rating"]] = 1

        if row["Gaze_Worksheet_Tutee"] == "x":
            if row["Rapport Rating"] in tutee_worksheet:
                tutee_worksheet[row["Rapport Rating"]] += 1
            else:
                tutee_worksheet[row["Rapport Rating"]] = 1
            # timeSplit = splitTime(str(row["Time_Start"]), str(row["Time_End"]))
            # duration = durationTime(timeSplit),
            # rapportRating = row["Rapport Rating"]
            # print(index, duration, timeSplit, rapportRating)
    
    print("\nDictionary built.\n")

    print("\nRapport\tBoth\tTutor\tTutee")

    print("\nCount Analysis\n")

    for i in range(1,8):
        key = float("%d.0" % i)
        print(key, tutee_partner[key], tutee_worksheet[key])

#     print("\nPercentage Analysis\n")
    
#     for i in range(1, 8):
#         key = float("%d.0" % i) 
#         total = (both[key] + tutor[key] + tutee[key])/100
#         print(key, "{0:.2f}".format(both[key]/total), 
#                             "{0:.2f}".format(tutor[key]/total), 
#                                         "{0:.2f}".format(tutee[key]/total))

# def mutual_smile_presence_rapport():
#     startTime = 0
#     timeDict = {}

#     for index, row in df.iterrows():
#         currTime = int(str(row["Time_Start"])[3:5]) # mins
#         key = currTime // 5
#         currRapport = row["Rapport Rating"]

#         if row["Smile_Tutor"] == "x" and row["Smile_Tutee"] == "x":
            
#             if key in timeDict:

#                 if "0" not in str(currRapport): # nan
#                     timeDict[key][0] += 1
#                     timeDict[key][2] += 1

#                 else:
#                     timeDict[key][0] += 1  
#                     timeDict[key][1].extend([currRapport])
#             else:
#                 if str(currRapport) != "nan":
#                     timeDict[key] = [1, [currRapport], 0]
#                 else:
#                     timeDict[key] = [1, [], 1]


#     for key in sorted(timeDict.keys()):
#         time_start = 5 * key
#         time_end = 5 * (key + 1) 
#         rapport_avg = sum(timeDict[key][1]) / len(timeDict[key][1])
#         print("Time Period", time_start, " - ",time_end,"\t: ", 
#                     timeDict[key][0], "\tRapportAvg ", 
#                         "{0:.2f}".format(rapport_avg), "\tOmitted ", 
#                             timeDict[key][2], "/", 
#                                 timeDict[key][2] + len(timeDict[key][1]))

# def tutor_only_smile_presence_rapport():
#     startTime = 0
#     timeDict = {}

#     for index, row in df.iterrows():
#         currTime = int(str(row["Time_Start"])[3:5]) # mins
#         key = currTime // 5
#         currRapport = row["Rapport Rating"]

#         if row["Smile_Tutor"] == "x" and row["Smile_Tutee"] != "x":
            
#             if key in timeDict:

#                 if "0" not in str(currRapport): # nan
#                     timeDict[key][0] += 1
#                     timeDict[key][2] += 1

#                 else:
#                     timeDict[key][0] += 1  
#                     timeDict[key][1].extend([currRapport])
#             else:
#                 if str(currRapport) != "nan":
#                     timeDict[key] = [1, [currRapport], 0]
#                 else:
#                     timeDict[key] = [1, [], 1]


#     for key in sorted(timeDict.keys()):
#         time_start = 5 * key
#         time_end = 5 * (key + 1) 
#         rapport_avg = sum(timeDict[key][1]) / len(timeDict[key][1])
#         print("Time Period", time_start, " - ",time_end,"\t: ", 
#                     timeDict[key][0], "\tRapportAvg ", 
#                         "{0:.2f}".format(rapport_avg), "\tOmitted ", 
#                             timeDict[key][2], "/", 
#                                 timeDict[key][2] + len(timeDict[key][1]))

# def tutee_only_smile_presence_rapport():
#     startTime = 0
#     timeDict = {}

#     for index, row in df.iterrows():
#         currTime = int(str(row["Time_Start"])[3:5]) # mins
#         key = currTime // 5
#         currRapport = row["Rapport Rating"]

#         if row["Smile_Tutor"] != "x" and row["Smile_Tutee"] == "x":
            
#             if key in timeDict:

#                 if "0" not in str(currRapport): # nan
#                     timeDict[key][0] += 1
#                     timeDict[key][2] += 1

#                 else:
#                     timeDict[key][0] += 1  
#                     timeDict[key][1].extend([currRapport])
#             else:
#                 if str(currRapport) != "nan":
#                     timeDict[key] = [1, [currRapport], 0]
#                 else:
#                     timeDict[key] = [1, [], 1]


#     for key in sorted(timeDict.keys()):
#         time_start = 5 * key
#         time_end = 5 * (key + 1) 
#         rapport_avg = sum(timeDict[key][1]) / len(timeDict[key][1])
#         print("Time Period", time_start, " - ",time_end,"\t: ", 
#                     timeDict[key][0], "\tRapportAvg ", 
#                         "{0:.2f}".format(rapport_avg), "\tOmitted ", 
#                             timeDict[key][2], "/", 
#                                 timeDict[key][2] + len(timeDict[key][1]))


print("\nDoing Gaze Presence Analysis...\n")
gaze_presence_analysis()
print("\nGaze Presence Analysis done.\n")

# print("\nMutual Smile Presence in intervals of 5 mins along with Rapport Avg\n")
# mutual_smile_presence_rapport()

# print("\nTutor Only Smile Presence in intervals of 5 mins along with Rapport Avg\n")
# tutor_only_smile_presence_rapport()

# print("\nTutee Only Smile Presence in intervals of 5 mins along with Rapport Avg\n")
# tutee_only_smile_presence_rapport()