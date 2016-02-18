import csv
import numpy as np
import pandas as pd
data = pd.read_csv("problem.csv")
#data= []

#for row in csvFile:
#	data.append(row)

data = np.array(data)
print data.shape
for i in xrange (0,50):
   print (data[0,0]+data[0,0])
#data[i,0::]
np.array(data).tolist()
