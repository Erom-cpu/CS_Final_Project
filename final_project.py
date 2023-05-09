import requests #pulls data out of websites
import bs4 #this allows to call the data in different ways
import pandas as pd #turns link to html
import matplotlib.pyplot as plt #plots the data



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
df = df[[("Country", "Country"),('Warheads[a]', 'Total')]].astype('int')
print(df)
df.plot(('Country', 'Country'), y = ('Warheads[a]', 'Total'), kind = 'bar')
plt.show()
print(df.info())