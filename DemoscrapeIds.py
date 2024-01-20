from bs4 import BeautifulSoup #beautiful soup is a library that provides the backbone for webscraping 
import requests

url = 'https://www.pro-football-reference.com/years/2023/passing.htm'
r = requests.get(url) #use the requests method to acess the url 

soup = BeautifulSoup(r.content, 'html.parser') #beautiful soup uses thee fetched url and parses the html content 

players = soup.find('table' , id = 'passing') #go to inspect element on your browser and find the ID for the table you are going to use 

print(players)
