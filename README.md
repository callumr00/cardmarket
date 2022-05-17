# CardMarketScrape

## Description

Python tool to display price of all cards in a Yu-Gi-Oh! set(s).

## Function

![Screenshot of card collection web page](https://github.com/cally2k/CardMarketScrape/blob/master/img/webPage1.png)
The name of the set [1] is inputted into collectionList.txt\
All the cards in the set [2] (inc. all other pages) are then displayed as a list collectively before being outputted 1 by 1 with their respective price.

![Screenshot of card collection web page](https://github.com/cally2k/CardMarketScrape/blob/master/img/webPage2.png)
The price is taken from the first listing available [1] with defined filters applied [2].

## Output

![Screenshot of terminal output](https://github.com/cally2k/CardMarketScrape/blob/master/img/terminalOutput.png)

## Notes

All prices are taken from cardmarket.com\
Functionality requires python with modules: 'requests', 'BeautifulSoup' and 'math'\
For multiple sets, place the nth set name on a new line below the previous
