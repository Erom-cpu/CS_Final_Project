import requests #pulls data out of websites
import bs4 #this allows to call the data in different ways
import pandas as pd #turns link to html
import matplotlib.pyplot as plt #plots the data
from itertools import cycle, islice
import pandas, numpy as np  # I find np.random.randint to be better


url = 'https://en.wikipedia.org/wiki/List_of_states_with_nuclear_weapons'
# response = requests.get(url)
# soup = bs4.BeautifulSoup(response.text)

# pretty_html_string = soup.prettify()

# with open("nuclear_wiki.htm", "w") as f:
#     f.write(pretty_html_string)

# df = pd.read_csv("nuclear_wiki.htm")
# print(df.columns)

dfs = pd.read_html(
    url,
    match = "Overview of nuclear states and their capacities"
)
df = dfs[0]
df.columns = df.columns.to_flat_index()
df[('Warheads[a]', 'Total')] = df[('Warheads[a]', 'Total')].str.replace(r"\[.*\]","")
df[("Country", "Country")] = df[("Country", "Country")].str.replace(r"\[.*\]","")
df = df[[("Country", "Country"),('Warheads[a]', 'Total')]].astype({('Warheads[a]', 'Total'): 'int32'})
print(df)

#Code for first graph (Line graph (red))
df.plot(x = ('Country', 'Country'), y = ('Warheads[a]', 'Total'), lw =2, 
colormap = 'flag', marker = '.', markersize = 10, title = "Amount of nuclear warheads per state")

#Code for second graph (Bar graph (green))
df.plot(x = ('Country', 'Country'), y = ('Warheads[a]', 'Total'), kind = 'bar', 
colormap = 'Accent', title = "Amount of nuclear warheads per state")

plt.show()
print(df.info())