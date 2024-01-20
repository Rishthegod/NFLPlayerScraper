import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time 

playerList = pd.read_csv("/Users/rishsharma/Documents/QuarterBackCleanupList.csv") #access the scrubbed Quarterback list that we created
NFLurl = 'https://www.pro-football-reference.com' #set the base url from which we are going to fuzz or append paths to all the players

seasonYears = []

def createNFLSeasonURL(Year : int) -> str:
    '''create the fuzzed url for any year input given, specifically for NFL players'''
    createdUrl = "/gamelog/" + str(Year) + "/advanced/"
    return createdUrl


def askUser() -> tuple:
    """This function asks the user to input the season, and number of past years to analyze from"""
    selectedYear = int(input("Please input the current season: "))
    seasonCount = int(input("Please enter how many seasons past you want to analyze from: "))
    return selectedYear, seasonCount



def createSeasonArray() -> None:
    selectedYear,seasonCount = askUser()
    for i in range(seasonCount):
        seasonYears.append(createNFLSeasonURL(selectedYear - i))

createSeasonArray()

print(seasonYears)

f = open("latestDataPullQB.csv", 'w', newline='') #open a csv file to write the data to 
scrapedGames = csv.writer(f)

statList = []
headerCount = 0


for x in range(0,len(playerList)): #create a loop that iterates through every line in the cleanuplist csv
    url_extension = playerList['ID'].iloc[x] #get the Id for row x 
    playerName = playerList['Name'].iloc[x] #get the name for row x 
    for y in seasonYears:
        time.sleep(6) #sleep for six seconds to not get IP banned from the website for too many request
        
        r =requests.get(NFLurl + url_extension + y) #create the url to retrieve information for that player

        soup = BeautifulSoup(r.text, 'html.parser')

        season_table = soup.find('table', id = "advanced_passing") #, based on the html table id on the website, we pull the stat table

        

        statList = []
        headerCount = 0

        print(NFLurl + url_extension + y)

        try: 
            for headers in season_table.find_all('th'): #th means table header in html
                valueHeader = headers.text
                if valueHeader == 'Rk': 
                    '''check if we are starting from the correct column that we want (that we have the right table)
                      Rk is the table header for the column Rank on the website. If we are scraping form another source then we need to change this'''
                    headerCount = 1
                if headerCount == 1: 
                    statList.append(valueHeader)
            print("This is the first thing printed")
            scrapedGames.writerow(statList) #create the headerList

            gameArray = []
            breakValue = 0 
            for game in season_table.find_all('tr'): #tr is table row
                cols = game.find_all('td') #td is table data
                statList = [playerName]
                for col in cols:
                    if 'Upcoming' in col.text: #a value of Upcoming is invalid and thus we need to move onto the next column
                        breakValue = 1 
                        break
                    else:
                        stat_col = col.text #otherwise the value is valid and we can append it to statList
                        statList.append(stat_col)
                    if breakValue == 1:
                        break
                print(statList)
                scrapedGames.writerow(statList)
                gameArray.append(statList)

        except Exception as error:
            print("sum went wrong", error) 
            continue #continue on all exceptions, for example rows may be empty when players miss games or switch teams etc.
f.close()