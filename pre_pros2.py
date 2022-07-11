
import pandas as pd
import numpy as np
df = pd.read_csv("/Users/shellyschwartz/Downloads/Cardiovascular_exdp.csv")

patients = df.groupby("PID")


arr = []

time_win = 7
for pat in list(patients):
    dat = pat[1]
    dat = dat.sort_values(by=['Date']) #sort times from least to greatest
    first = dat.iloc[0]
    sub_arr = [first["Event"]] #set first event found in patient group to be first index of a time window

    count = 0
    proc = 0
    diag = 0

    print(dat)

    for i in range(1, len(dat)):

        curr = dat.iloc[i]
        count = count + (curr["Date"] - first['Date']) # find cumulative difference starting from beg of time window
        print(first["Date"], curr["Event"], curr["Date"], count)

        if(count <= time_win and i < len(dat)-1): #check if cumulative difference is within the time window
            sub_arr.append(curr["Event"]) #add the current even to sub array since it is within the time window

            if(curr["Type"]=="Procedure" or "Procedure"==first["Type"]): #update booleans for wether or not time window contains procededure and diagnosis
                proc = 1
            if (curr["Type"] == "Diagnosis" or "Diagnosis"==first["Type"]):
                diag = 1

        elif (count <= time_win and i == len(dat)-1) or (count > time_win): #added edge case for when a valid event is the last row of dat

            if i == len(dat)-1:
                sub_arr.append(curr["Event"])
                if(curr["Type"] == "Diagnosis"):
                    diag = 1
                if (curr["Type"] == "Procedure"):
                    proc = 1

            if (proc == 1 and diag == 1): #check if there are procedures and diagnosis in the window
                print(sub_arr)
                arr.append(sub_arr) #save transaction
            sub_arr = [curr["Event"]] #set sub arr = curr event
            count = 0 #reset time window count
            proc = 0 #reset bools
            diag = 0

        first = curr  # set first event to be curr, so time window events can be updated




#keep a cummaltive count

#for i in range(1, len(dat)):


    # for i in range(1, len(dat)):
    #     if(dat.iloc[i]["Date"] <= dat.iloc[i-1]["Date"] + 7): #make it cummalitive sum
    #
    #         if("Procedure" not in list(dat.iloc[i]["Type"])):  #change this
    #             print(sub_arr)
    #             continue
    #         else:
    #             sub_arr.append(dat.iloc[i][ "Event"])
    #     else:
    #         arr.append(sub_arr)
    #         sub_arr = [dat.iloc[i][ "Event"]]
    # arr.append(sub_arr)


# print(len(arr))
#
#
#make columns = events that are contained witn the entire dataset
#for each event in trans set the new df[row][trans] = true

uniq_events = df["Event"].unique()
#populate data frame with zeros, set columns to be events
new_df = pd.DataFrame(0, index=np.arange(len(arr)), columns=uniq_events)
#
count = 0
for trans in arr:
    for event in trans:
        new_df.iloc[count][event] = 1  #make a boolean
    count = count + 1
#print(new_df)
#
#
#
new_df.replace({0: False, 1: True}, inplace=True)
#
#print(new_df)
#
new_df.to_csv('/Users/shellyschwartz/PycharmProjects/apriori-algo/pros_data2.csv', index = False)