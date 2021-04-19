Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://www.foxsports.com/soccer/fifa-world-cup/history")

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', {'class':'wisbb_heStandard'})
#print(table)

cols = []
for name in table.select('th'):
    cols.append(name.text.strip())
    
#print(cols)

titles = cols[:3]
#print(titles)

info = []
for match in table.select('td'):
    info.append(match.text.strip())
#print(info)

# Extracting year, host and winner of each match
year = info[::9]
host = info[1::9]
champion = info[2::9]
'''print(year)
print(host)
print(champion)
'''

# Converting list into dictionary
world_cup_dict = {
  'Year' : year,
  'Host' : host,
  'Winner' : champion
}

# Converting dict into dataframe
df= pd.DataFrame.from_dict(world_cup_dict)

#Starting the row count from 1
df.index = df.index+1

print(df )