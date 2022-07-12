import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/shellyschwartz/Downloads/Cardiovascular_exdp.csv")

print(df)

patients = df.groupby("PID")
count = 0
for pat in list(patients):
    dat = pat[1]
    types = list(dat["Type"])
    for type in types:
        if type == "Procedure":
            count = count + 1
            break

print(len(list(patients)), count)
#plot of 20 most frequent events
df['Event'].value_counts()[:20].plot(kind='barh')
plt.show()

#show which events correspond to procedures, diagnosis or both
events = df.groupby("Event")

dict = {}
for event in list(events):
    arr = event[1]["Type"]
    if(len(set(arr))==1):
        dict.update({event[0]: arr[arr.index[0]]})
    else:
        dict.update({event[0]: "both"})
print(dict)

# compare the number of events that are procedures and events that are Diagnosis

arr2 = list(dict.values())
proc = arr2.count("Procedure")
diag = arr2.count("Diagnosis")
print(proc, diag)

#compare counts of diagnosis to procedures




