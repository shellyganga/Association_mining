from matplotlib import pyplot as plt
import networkx as nx
import pandas as pd
import gravis as gv
import networkx as nx

data = pd.read_csv("/Users/shellyschwartz/PycharmProjects/apriori-algo/rules.csv")

print(data)

arr = []
for i in range(len(data)):
    tuple = (data.loc[i, 'antecedents'][12:-3], data.loc[i, 'consequents'][12:-3])
    arr.append(tuple)





g1 = nx.DiGraph()
g1.add_edges_from(arr)
fig = gv.d3(g1)
fig.display()
# g1.add_edges_from(arr)
# plt.tight_layout()
# nx.draw_networkx(g1, arrows=True)
#plt.savefig("g1.png", format="PNG")
#
# # tell matplotlib you're done with the plot: https://stackoverflow.com/questions/741877/how-do-i-tell-matplotlib-that-i-am-done-with-a-plot
#plt.clf()
