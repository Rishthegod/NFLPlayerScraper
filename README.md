<h1>NFL Player Data Scraper</h1>
<h3>Feature List:</h3>
<ul><li>Ability to Select NFL to start analyzing from</li>
  <li>Ability to choose how many seasons past to scrape</li>
  <li>Comprehensive Advanced Gamelog Data Scraping</li></ul>
<h4>What's included in the Repo:</h4>
<ul><li><h5>WebScraper.py:</h5> 
Run this script to generate the latest data pull spreadsheet</li>
  <li><h5>QuarterbackCleanupList.csv:</h5>
  List of all NFL Quarterbacks with their respective URL path prefuzzed</li>
  <li><h5>LatestQBdataPull.csv:</h5>
  Latest Quarterback Data pull for the 2020-2023 seasons</li>
  <li><h5>DemoScrapeIDs.py:</h5>
  Run this script to scrape player names and their respective Id's to create CleanupList</li>
  <li><h5>PlayerData.xlsm:</h5>
  Intermediary Spreadsheet with Visual Basic macros to clean player list and generate fuzzed URLs for the QBs</li></ul>

<h5>Reason for development: Sports Betting is a new fad rising quickly among young adults at UC Irvine, this player scraper allows for more informed decisions behind a bet.</h5>
<h5>This is a sample use case for this scraper. By changing the initial URL for the database, the user can easily scrape different positions, or teams as a whole.</h5>
**Next steps:**
Create and algorithm and Train an AI to analyze scraped data and predict whether a given team is going to win or not.   
<h6><small>Command to get html path for player: =MID(AE2,8,LEN(AE2)-11) (deletes file:/// and .htm)</small></h6>
