
import pandas as pd
import numpy as np
df = pd.read_csv("/Users/shellyschwartz/Downloads/Cardiovascular_exdp.csv")

patients = df.groupby("PID")


arr = []

for pat in list(patients):
    #skip if time window does not contain diag or procedure
    dat = pat[1]
    dat = dat.sort_values(by=['Date'])
    sub_arr = [dat.iloc[0]["Event"]]

    for i in range(1, len(dat)):
        if(dat.iloc[i]["Date"] <= dat.iloc[i-1]["Date"] + 7):
            if("Procedure" not in list(dat.iloc[i]["Type"])):
                continue
            else:
                sub_arr.append(dat.iloc[i][ "Event"])
        else:
            arr.append(sub_arr)
            sub_arr = [dat.iloc[i][ "Event"]]
    arr.append(sub_arr)


print(len(arr))


#make columns = events that are contained witn the entire dataset
#for each event in trans set the new df[row][trans] = true

uniq_events = df["Event"].unique()
#populate data frame with zeros, set columns to be events
new_df = pd.DataFrame(0, index=np.arange(len(arr)), columns=uniq_events)

count = 0
for trans in arr:
    for event in trans:
        new_df.iloc[count][event] += 1
    count = count + 1



new_df.replace({0: False, 1: True}, inplace=True)

print(new_df)

new_df.to_csv('/Users/shellyschwartz/PycharmProjects/apriori-algo/pros_data2.csv', index = False)