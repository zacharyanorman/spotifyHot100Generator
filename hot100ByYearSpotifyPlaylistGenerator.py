#Create a playlist from the Billboard Hot 100 of the year for any valid year

#1. User inputs the year

print('Which year (1959-2019) do you want to a playlist from?')
year = int(input())

print('Finding Billboard Year-End Hot 100 singles of ' +str(year))

#2. Scrape wikipedia for the top songs of that year

import urllib
import urllib.request
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_" + str(year)
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, "html.parser")

songTitle = ""
artist = ""
listArtist = []
listTitle = []


table = soup.find("table", { "class" : "wikitable sortable" })

f = open('output.csv', 'w')

for row in table.findAll("tr"):
    cells = row.findAll("td")
    #For each "tr", assign each "td" to a variable.
    #IMPORTANT: Not all wiki tables are the same. Must check for 2 or 3 columns wide 
    if len(cells) == 3:
        #Finds song and artist text
        songTitle = cells[1].findAll(text=True)
        artist = cells[2].findAll(text=True)
        #Appends song and artist to lists
        listTitle.append(songTitle)
        listArtist.append(artist)
    elif len(cells) == 2:
        #Finds song and artist text
        songTitle = cells[0].findAll(text=True)
        artist = cells[1].findAll(text=True)
        #Appends song and artist to lists
        listTitle.append(songTitle)
        listArtist.append(artist)

f.close()

#Attempting to remove all unnecessay entries

searchableArtist = [''] * 100 
searchableTitle = [''] * 100 

for x in range(0, len(listArtist)):
    for y in range(0,len(listArtist[x])):
        if len(listArtist[x][y]) < 3:
            listArtist[x][y] = ''

 
for x in range(0, len(listTitle)):
    for y in range(0,len(listTitle[x])):
        if len(listTitle[x][y]) < 3:
            listTitle[x][y]= ''
            
print(listArtist)
print()
print(listTitle)
print()
print(len(listArtist))
print(len(listTitle))
                   
#Create single searchable lists from sublists. Not the same number of entries

'''
for x in range(0, len(listTitle)):
    listTitle[x] = str(listTitle[x])
    searchableTitle.append(listTitle)
'''


#3. Search for those songs on spotify



#4. Add songs to playlist

