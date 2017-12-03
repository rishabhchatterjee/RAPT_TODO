import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from Utils_InputCSV import InputCSV

from dict_col_names import getDict

import ConditionalGrangerCausality as CGC


filename = '2013_data_GC_v1.xls'
print ("\nLoading behavioral signals from the csv file : ", filename,"\n")

colNames = getDict()
print("colNames dict received.\n")

print(colNames)
print("\n")

x1 = InputCSV(filename, columns = [colNames[16]])   # self disclosure tutor
x2 = InputCSV(filename, columns = [colNames[28]])   # gaze partner tutor
x3 = InputCSV(filename, columns = [colNames[22]])   # smile tutor
# x4 = InputCSV(filename, columns = ['p1_B4'])
# x5 = InputCSV(filename, columns = ['p1_B5'])
# x6 = InputCSV(filename, columns = ['p1_B6'])
# x7 = InputCSV(filename, columns = ['p1_B7'])
# x8 = InputCSV(filename, columns = ['p1_B8'])
# x9 = InputCSV(filename, columns = ['p1_B9'])
# x10 = InputCSV(filename, columns = ['p1_B10'])
# x11 = InputCSV(filename, columns = ['p1_B11'])
# x12 = InputCSV(filename, columns = ['p1_B12'])
# x13 = InputCSV(filename, columns = ['p1_B13'])
# x14 = InputCSV(filename, columns = ['p1_B14'])
# x15 = InputCSV(filename, columns = ['p1_B15'])
# x16 = InputCSV(filename, columns = ['p1_B16'])
# x17 = InputCSV(filename, columns = ['p1_B17'])
# x18 = InputCSV(filename, columns = ['p1_B18'])
# x19 = InputCSV(filename, columns = ['p1_B19'])
# x20 = InputCSV(filename, columns = ['p1_B20'])
# x21 = InputCSV(filename, columns = ['p1_B21'])
# x22 = InputCSV(filename, columns = ['p1_B22'])
# x23 = InputCSV(filename, columns = ['p1_B23'])
# x24 = InputCSV(filename, columns = ['p1_B24'])


x39 = InputCSV(filename, columns = [colNames[4]])   # self disclosure tutee
x40 = InputCSV(filename, columns = [colNames[26]])  # gaze partner tutee
x41 = InputCSV(filename, columns = [colNames[30]])  # smile tutee
# x42 = InputCSV(filename, columns = ['p2_B4'])
# x43 = InputCSV(filename, columns = ['p2_B5'])
# x44 = InputCSV(filename, columns = ['p2_B6'])
# x45 = InputCSV(filename, columns = ['p2_B7'])
# x46 = InputCSV(filename, columns = ['p2_B8'])
# x47 = InputCSV(filename, columns = ['p2_B9'])
# x48 = InputCSV(filename, columns = ['p2_B10'])
# x49 = InputCSV(filename, columns = ['p2_B11'])
# x50 = InputCSV(filename, columns = ['p2_B12'])
# x51 = InputCSV(filename, columns = ['p2_B13'])
# x52 = InputCSV(filename, columns = ['p2_B14'])
# x53 = InputCSV(filename, columns = ['p2_B15'])
# x54 = InputCSV(filename, columns = ['p2_B16'])
# x55 = InputCSV(filename, columns = ['p2_B17'])
# x56 = InputCSV(filename, columns = ['p2_B18'])
# x57 = InputCSV(filename, columns = ['p2_B19'])
# x58 = InputCSV(filename, columns = ['p2_B20'])
# x59 = InputCSV(filename, columns = ['p2_B21'])
# x60 = InputCSV(filename, columns = ['p2_B22'])
# x61 = InputCSV(filename, columns = ['p2_B23'])
# x62 = InputCSV(filename, columns = ['p2_B24'])

#Comment input x77 from 100, in case of groups of 3 members such as formal study 1 and 2 where members are named p1,p2,p4
#In case of groups with 4 members such as formal study 3-6 where members are named p1,p2,p3,p4, keep all inputs uncommented
"""
x77 = InputCSV(filename, columns = ['p3_B1'])
x78 = InputCSV(filename, columns = ['p3_B2'])
x79 = InputCSV(filename, columns = ['p3_B3'])
x80 = InputCSV(filename, columns = ['p3_B4'])
x81 = InputCSV(filename, columns = ['p3_B5'])
x82 = InputCSV(filename, columns = ['p3_B6'])
x83 = InputCSV(filename, columns = ['p3_B7'])
x84 = InputCSV(filename, columns = ['p3_B8'])
x85 = InputCSV(filename, columns = ['p3_B9'])
x86 = InputCSV(filename, columns = ['p3_B10'])
x87 = InputCSV(filename, columns = ['p3_B11'])
x88 = InputCSV(filename, columns = ['p3_B12'])
x89 = InputCSV(filename, columns = ['p3_B13'])
x90 = InputCSV(filename, columns = ['p3_B14'])
x91 = InputCSV(filename, columns = ['p3_B15'])
x92 = InputCSV(filename, columns = ['p3_B16'])
x93 = InputCSV(filename, columns = ['p3_B17'])
x94 = InputCSV(filename, columns = ['p3_B18'])
x95 = InputCSV(filename, columns = ['p3_B19'])
x96 = InputCSV(filename, columns = ['p3_B20'])
x97 = InputCSV(filename, columns = ['p3_B21'])
x98 = InputCSV(filename, columns = ['p3_B22'])
x99 = InputCSV(filename, columns = ['p3_B23'])
x100 = InputCSV(filename, columns = ['p3_B24'])
"""
# x115 = InputCSV(filename, columns = ['p4_B1'])
# x116 = InputCSV(filename, columns = ['p4_B2'])
# x117 = InputCSV(filename, columns = ['p4_B3'])
# x118 = InputCSV(filename, columns = ['p4_B4'])
# x119 = InputCSV(filename, columns = ['p4_B5'])
# x120 = InputCSV(filename, columns = ['p4_B6'])
# x121 = InputCSV(filename, columns = ['p4_B7'])
# x122 = InputCSV(filename, columns = ['p4_B8'])
# x123 = InputCSV(filename, columns = ['p4_B9'])
# x124 = InputCSV(filename, columns = ['p4_B10'])
# x125 = InputCSV(filename, columns = ['p4_B11'])
# x126 = InputCSV(filename, columns = ['p4_B12'])
# x127 = InputCSV(filename, columns = ['p4_B13'])
# x128 = InputCSV(filename, columns = ['p4_B14'])
# x129 = InputCSV(filename, columns = ['p4_B15'])
# x130 = InputCSV(filename, columns = ['p4_B16'])
# x131 = InputCSV(filename, columns = ['p4_B17'])
# x132 = InputCSV(filename, columns = ['p4_B18'])
# x133 = InputCSV(filename, columns = ['p4_B19'])
# x134 = InputCSV(filename, columns = ['p4_B20'])
# x135 = InputCSV(filename, columns = ['p4_B21'])
# x136 = InputCSV(filename, columns = ['p4_B22'])
# x137 = InputCSV(filename, columns = ['p4_B23'])
# x138 = InputCSV(filename, columns = ['p4_B24'])

#Comment input x141, in case of groups of 3 members such as formal study 1 and 2 where members are named p1,p2,p4
#In case of groups with 4 members such as formal study 3-6 where members are named p1,p2,p3,p4, keep all inputs x139,x140,x141,x142 uncommented
#CI refers to curiosity increase. It is computed from original/raw thin-slice curiosity series as follows:
    #CI=1, if there is increase/maintenance of curiosity level compared to previous thin-slice [for curiosity levels 1 and 2];
    #CI=0, if there is decrease of curiosity level compared to previous thin-slice [for curiosity levels 1 and 2], as well as maintenance of curiosity level compared to previous thin-slice [for curiosity level 0]
x139 = InputCSV(filename, columns = [colNames[49]]) # rapport delta pre
x140 = InputCSV(filename, columns = [colNames[49]])
#x141 = InputCSV(filename, columns = ['CI_p3'])
#x142 = InputCSV(filename, columns = ['CI_p4'])

max_lag = 6     # 1) maximum lag acceptable to estimate autoregressive models (In our case, we choose 3, which means 3X30 secs=90 secs)
criterion = 'bic'   # 2) criterion to estimate the optimal number of lags to estimate autoregressive models
plot = True         # 3) authorize for plot of the results

print("\n")
cgc = CGC.ConditionalGrangerCausality(max_lag = max_lag, criterion = criterion, plot = plot)

#For groups of 4 members
#results = cgc.compute(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x39,x40,x41,x42,x43,x44,x45,x46,x47,x48,x49,x50,x51,x52,x53,x54,x55,x56,x57,x58,x59,x60,x61,x62,x77,x78,x79,x80,x81,x82,x83,x84,x85,x86,x87,x88,x89,x90,x91,x92,x93,x94,x95,x96,x97,x98,x99,x100,x115,x116,x117,x118,x119,x120,x121,x122,x123,x124,x125,x126,x127,x128,x129,x130,x131,x132,x133,x134,x135,x136,x137,x138,x139,x140,x141,x142)


#For groups of 3 members (inputs x77 to x100 and x141 are removed before the computation)
#results = cgc.compute(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x39,x40,x41,x42,x43,x44,x45,x46,x47,x48,x49,x50,x51,x52,x53,x54,x55,x56,x57,x58,x59,x60,x61,x62,x115,x116,x117,x118,x119,x120,x121,x122,x123,x124,x125,x126,x127,x128,x129,x130,x131,x132,x133,x134,x135,x136,x137,x138,x139,x140,x142)


results = cgc.compute(x1,x2,x3,x39,x40,x41,x139,x140)



input("Press any key to exit")
