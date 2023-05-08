import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://en.wikipedia.org/wiki/List_of_states_with_nuclear_weapons'
# response = requests.get(url)
# soup = bs4.BeautifulSoup(response.text)

# pretty_html_string = soup.prettify()

# with open("https://en.wikipedia.org/wiki/List_of_states_with_nuclear_weapons", "w") as f:
#     f.write(pretty_html_string)

# df = pd.("https://en.wikipedia.org/wiki/List_of_states_with_nuclear_weapons")


dfs = pd.read_html(
    url,
    match = "Overview of nuclear states and their capacities"
)
df = dfs[0]

df = df[['Country','Warheads[a], Total']].astype('int')
print(df)
df.plot('Country', y = 'Warheads[a], Total', kind = 'bar')
plt.show()
print(df.info())