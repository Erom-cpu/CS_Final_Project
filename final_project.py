import pandas as pd #turns link to html
import matplotlib.pyplot as plt #plots the data
from itertools import cycle, islice
import pandas, numpy as np  #p.random.randint sometimes better


url = 'https://en.wikipedia.org/wiki/List_of_states_with_nuclear_weapons' #Website URL

dfs = pd.read_html(
    url,
    match = "Overview of nuclear states and their capacities" #Graph's title in website
)
df = dfs[0]
#following code solves astype() problem 
df.columns = df.columns.to_flat_index()
df[('Warheads[a]', 'Total')] = df[('Warheads[a]', 'Total')].str.replace(r"\[.*\]","")
df[("Country", "Country")] = df[("Country", "Country")].str.replace(r"\[.*\]","")
df = df[[("Country", "Country"),('Warheads[a]', 'Total')]].astype({('Warheads[a]', 'Total'): 'int32'})
print(df)

#Code for bar graph
df.plot(x = ('Country', 'Country'), y = ('Warheads[a]', 'Total'), kind = 'bar', 
colormap = 'Accent', title = "Amount of nuclear warheads per state") #Adds graph color and graph title

plt.show()#Print Graph
print(df.info())#Prints table information