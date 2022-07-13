# importing the required module
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


#get prosesed data
data = pd.read_csv("/Users/shellyschwartz/PycharmProjects/apriori-algo/pros_data2.csv")
#apriori stuff

# Extracting the most frequest itemsets via Mlxtend.
frequent_itemsets = apriori(data, min_support=0.04, use_colnames=True,  max_len = 2)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))

# printing the frequent itemset
print(frequent_itemsets)

#restrict length = 1

#  We set our metric as "confidence to define whether antecedents & consequents are dependent our not
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=.4)
rules["antecedents_length"] = rules["antecedents"].apply(lambda x: len(x))
rules["consequents_length"] = rules["consequents"].apply(lambda x: len(x))
rules = rules.sort_values("lift")

#write sorting funct

print(rules)

#generated from explore.py
dict = {'00160J6': 'Procedure', '009600Z': 'Procedure', '009U3ZX': 'Procedure', '00P600Z': 'Procedure', '027034Z': 'Procedure', '02H43KZ': 'Procedure', '02H63JZ': 'Procedure', '02H63KZ': 'Procedure', '02HK3JZ': 'Procedure', '02HK3KZ': 'Procedure', '02HV33Z': 'Procedure', '02PA3MZ': 'Procedure', '02RG0JZ': 'Procedure', '03C63ZZ': 'Procedure', '03HY32Z': 'Procedure', '047H3ZZ': 'Procedure', '047J3ZZ': 'Procedure', '04V03D6': 'Procedure', '05HB33Z': 'Procedure', '05HM33Z': 'Procedure', '05PYX3Z': 'Procedure', '06H033Z': 'Procedure', '099670Z': 'Procedure', '099F30Z': 'Procedure', '099G30Z': 'Procedure', '0B113F4': 'Procedure', '0B978ZZ': 'Procedure', '0B9F8ZX': 'Procedure', '0BH17EZ': 'Procedure', '0BH18EZ': 'Procedure', '0BP1XFZ': 'Procedure', '0BQT4ZZ': 'Procedure', '0CDWXZ1': 'Procedure', '0CDXXZ1': 'Procedure', '0D164ZA': 'Procedure', '0D1B0Z4': 'Procedure', '0D1K0Z4': 'Procedure', '0D1L0Z4': 'Procedure', '0D2DXUZ': 'Procedure', '0D758ZZ': 'Procedure', '0DB18ZX': 'Procedure', '0DB58ZX': 'Procedure', '0DB68ZX': 'Procedure', '0DB78ZX': 'Procedure', '0DB80ZZ': 'Procedure', '0DB98ZX': 'Procedure', '0DBE8ZX': 'Procedure', '0DBL0ZZ': 'Procedure', '0DBN8ZX': 'Procedure', '0DBN8ZZ': 'Procedure', '0DH60UZ': 'Procedure', '0DH63UZ': 'Procedure', '0DH67UZ': 'Procedure', '0DJ08ZZ': 'Procedure', '0DN80ZZ': 'Procedure', '0DNL0ZZ': 'Procedure', '0DNM0ZZ': 'Procedure', '0DNU0ZZ': 'Procedure', '0DNW0ZZ': 'Procedure', '0DQU0ZZ': 'Procedure', '0DSL0ZZ': 'Procedure', '0DTF0ZZ': 'Procedure', '0DTF4ZZ': 'Procedure', '0DTG0ZZ': 'Procedure', '0DTJ4ZZ': 'Procedure', '0F798ZZ': 'Procedure', '0HBNXZZ': 'Procedure', '0HBRXZZ': 'Procedure', '0J2TXYZ': 'Procedure', '0JB70ZZ': 'Procedure', '0JBN0ZZ': 'Procedure', '0JH606Z': 'Procedure', '0JH609Z': 'Procedure', '0JH63XZ': 'Procedure', '0JN80ZZ': 'Procedure', '0JPT0PZ': 'Procedure', '0JX80ZB': 'Procedure', '0KXN0Z0': 'Procedure', '0QB20ZZ': 'Procedure', '0RB30ZZ': 'Procedure', '0RG10A0': 'Procedure', '0T760DZ': 'Procedure', '0TY00Z0': 'Procedure', '0VTTXZZ': 'Procedure', '0W3P8ZZ': 'Procedure', '0W9B30Z': 'Procedure', '0W9B3ZX': 'Procedure', '0WPF0JZ': 'Procedure', '0WPG03Z': 'Procedure', '0WQF0ZZ': 'Procedure', '0YUH0KZ': 'Procedure', '10D00Z1': 'Procedure', '10E0XZZ': 'Procedure', '10H07YZ': 'Procedure', '30233N1': 'Procedure', '30243N1': 'Procedure', '3E0134Z': 'Procedure', '3E0436Z': 'Procedure', '3E043XZ': 'Procedure', '3E06317': 'Procedure', '3E0G76Z': 'Procedure', '3E0L3GC': 'Procedure', '4A00X4Z': 'Procedure', '4A023N7': 'Procedure', '4A10X4Z': 'Procedure', '4A133B1': 'Procedure', '4A133J1': 'Procedure', '5A09357': 'Procedure', '5A1221Z': 'Procedure', '5A1935Z': 'Procedure', '5A1945Z': 'Procedure', '5A1955Z': 'Procedure', '5A1D00Z': 'Procedure', '5A1D70Z': 'Procedure', '5A2204Z': 'Procedure', '6A801ZZ': 'Procedure', '8C01X6J': 'Procedure', 'B2111ZZ': 'Procedure', 'B211YZZ': 'Procedure', 'B2151ZZ': 'Procedure', 'B215YZZ': 'Procedure', 'B246ZZ4': 'Procedure', 'B24BZZZ': 'Procedure', 'B24CZZZ': 'Procedure', 'B311YZZ': 'Procedure', 'B3121ZZ': 'Procedure', 'B312YZZ': 'Procedure', 'B3151ZZ': 'Procedure', 'B315YZZ': 'Procedure', 'B316YZZ': 'Procedure', 'B31F1ZZ': 'Procedure', 'B410YZZ': 'Procedure', 'B5131ZA': 'Procedure', 'B543ZZA': 'Procedure', 'B548ZZA': 'Procedure', 'I110': 'Diagnosis', 'I119': 'Diagnosis', 'I130': 'Diagnosis', 'I1311': 'Diagnosis', 'I132': 'Diagnosis', 'I200': 'Diagnosis', 'I208': 'Diagnosis', 'I2119': 'Diagnosis', 'I214': 'Diagnosis', 'I219': 'Diagnosis', 'I21A1': 'Diagnosis', 'I238': 'Diagnosis', 'I248': 'Diagnosis', 'I249': 'Diagnosis', 'I2510': 'Diagnosis', 'I25110': 'Diagnosis', 'I25118': 'Diagnosis', 'I25119': 'Diagnosis', 'I252': 'Diagnosis', 'I255': 'Diagnosis', 'I25810': 'Diagnosis', 'I259': 'Diagnosis', 'I2781': 'Diagnosis', 'I313': 'Diagnosis', 'I330': 'Diagnosis', 'I339': 'Diagnosis', 'I38': 'Diagnosis', 'I420': 'Diagnosis', 'I428': 'Diagnosis', 'I429': 'Diagnosis', 'I468': 'Diagnosis', 'I469': 'Diagnosis', 'I471': 'Diagnosis', 'I472': 'Diagnosis', 'I498': 'Diagnosis', 'I499': 'Diagnosis', 'I501': 'Diagnosis', 'I5020': 'Diagnosis', 'I5021': 'Diagnosis', 'I5022': 'Diagnosis', 'I5023': 'Diagnosis', 'I5030': 'Diagnosis', 'I5031': 'Diagnosis', 'I5032': 'Diagnosis', 'I5033': 'Diagnosis', 'I5042': 'Diagnosis', 'I5043': 'Diagnosis', 'I50810': 'Diagnosis', 'I50813': 'Diagnosis', 'I5082': 'Diagnosis', 'I509': 'Diagnosis', 'I513': 'Diagnosis', 'I517': 'Diagnosis', 'P2912': 'Diagnosis', 'R000': 'Diagnosis', 'R001': 'Diagnosis', 'R011': 'Diagnosis', 'R570': 'Diagnosis', 'R9431': 'Diagnosis', 'R9439': 'Diagnosis', 'T82198A': 'Diagnosis', 'T827XXA': 'Diagnosis', 'T82857A': 'Diagnosis', 'T829XXA': 'Diagnosis', 'Z01810': 'Diagnosis', 'Z4502': 'Diagnosis', 'Z8249': 'Diagnosis', 'Z8674': 'Diagnosis', 'Z950': 'Diagnosis', 'Z95810': 'Diagnosis'}
df = pd.DataFrame(columns = rules.columns)
for row in rules.iterrows():

    if((dict[list(row[1]['antecedents'])[0]] == "Procedure" and dict[list(row[1]['consequents'])[0]] == "Diagnosis") or (dict[list(row[1]['antecedents'])[0]] == "Diagnosis" and dict[list(row[1]['consequents'])[0]] == "Procedure")):
        df = df.append(row[1])
    else:
        continue



df.to_csv('/Users/shellyschwartz/PycharmProjects/apriori-algo/rules.csv', index = False)

#find negative relationships?
