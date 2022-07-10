#reshape the pandas dataframe such that we can see which procedure(s) and diagnosis(s) occur together
#event codes will represent different diagnosies and procedures
#columns = name of event, rows = events that occured with a particular column label event
#for now, one transaction will represent one claim

import pandas as pd
import numpy as np
df = pd.read_csv("/Users/shellyschwartz/Downloads/Cardiovascular_ex - Cardiovascular_ex.csv")

claims = df.groupby("CID")

uniq_events = df["Event"].unique()



#populate data frame with zeros, set columns to be events
new_df = pd.DataFrame(0, index=np.arange(len(df['CID'])), columns=uniq_events)

count= 0

#for each row: if it exists in the claim, assign 1 to a event (rows represent claims/transactions)
for claim in list(claims):
    arr = list(claim[1]["Event"])

    for event in arr:
        new_df.iloc[count][event] += 1
    count = count + 1


#transform 0/1 into true false
new_df.replace({0: False, 1: True}, inplace=True)

print(new_df)

new_df.to_csv('/Users/shellyschwartz/PycharmProjects/apriori-algo/pros_data.csv', index = False)

#apply apriori algo with grouping of claims by patient-time window
#make graphs for antecedents and conesequences
#finetune apriori/assocation rule mining, costumize metric, sort according to diff metrics






















