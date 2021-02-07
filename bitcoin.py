#2021 GMIT
#Bitcoing Price Checker 
#Author Michal Sudol = GMIT G00398852@gmit.ie

import requests 

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
returnedData = requests.get(url)
bitCoinDict = returnedData.json()

print(bitCoinDict)