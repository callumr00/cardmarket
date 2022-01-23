# Import modules
import requests
from bs4 import BeautifulSoup
import math

# Convert CollectionList.txt to a list of collections
file = open('collectionList.txt', 'r')
collectionList = [(line.strip()).split() for line in file]
file.close()

# Converts items in collectionList to URLs and append to list
collectionListURL = []

for item in collectionList:
    collectionURL = 'https://www.cardmarket.com/en/YuGiOh/Products/Singles/' + str(item)
    collectionListURL.append(collectionURL.replace('[\'','').replace('\']',''))

# Set index to 0
i = 0

# Web scrapes for each item in list
for item in collectionListURL:
    print('Name: ' + str(collectionList[i]))
    print()

    results = BeautifulSoup(requests.get(item).content, 'html.parser').find('main', class_='container')

    # Find amount of pages
    pageAmount = (math.ceil(int(results.find('div', class_='col-auto d-none d-md-block').text.strip().replace(' Hits',''))/20))

    # Create empty lists & set variables
    pageList    = []
    cardList    = []
    cardURLList = []

    value       = 0
    pageNumber  = 1

    # Get URL for each page
    while pageNumber <= pageAmount:
        urlNew = item + f'?site={pageNumber}'
        pageNumber = pageNumber + 1
        pageList.append(urlNew)

    # Get card list from each page
    for item in pageList:
        resultsNew = BeautifulSoup(requests.get(item).content, 'html.parser').find('main', class_='container')

        cards = resultsNew.find_all('div', class_='col-10 col-md-8 px-2 flex-column align-items-start justify-content-center')[1:]

        # Fill lists with card name and URL
        for item in cards:
            cardName = item.find('a')
            cardList.append(cardName.text.strip())
            cardURLList.append('https://www.cardmarket.com/' + cardName['href'].replace('en/YuGiOh/Products/Structure-Decks/',''.replace('?sellerCountry=13&language=1','')) + '?sellerCountry=13&language=1')

    print(cardList)
    print()

    # Get card info
    for item in cardURLList:
        cardInfoResults = BeautifulSoup(requests.get(item).content, 'html.parser').find('main', class_='container')

        # Get card name
        name = cardInfoResults.find('h1')
        name.find('span').extract()
        print(name.text.strip())

        # Get card price

        # Note: Price shown is inaccurate and can be in either EUR or GBP
        price  = cardInfoResults.find_all('dd', class_='col-6 col-xl-7')[1:]
        print(price[3].text.strip())
        # value = value + round(float(price[3].text.replace(',','.').replace('£','').replace('€','').strip()),2)
        print()

    # Print info
    print('Value: ' + str(value))
    print('Cards: ' + str(len(cardList)))
    print('Pages: ' + str(len(pageList)))
    print()

    # Set name to next in list
    i = i + 1