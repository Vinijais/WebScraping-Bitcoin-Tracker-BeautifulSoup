import requests
from bs4 import BeautifulSoup
url ="https://www.binance.com/en/price/bitcoin"
res = requests.get(url)
print(res)
# soup = BeautifulSoup(res.text, 'lxml')
soup = BeautifulSoup(res.text, 'html.parser')  # Use 'html.parser' instead of 'lxml'

uneditedPrice = soup.find(class_='css-1267ixm').text
print(uneditedPrice)
formattedPrice = uneditedPrice[2:]  # Removing dollar sign
formattedPrice = formattedPrice.replace(",", "")  # Removing comma

# Splitting the string at '+' and taking the first part
formattedPrice = formattedPrice.split('+')[0]

print(formattedPrice)
myIdealPrice = 68000
# formattedPrice = int(formattedPrice)
formattedPrice = int(''.join(filter(str.isdigit, formattedPrice)))  # Extract digits and convert to integer

if (formattedPrice < myIdealPrice):
    print("Bitcoin value is favourable")
else:
    print("Bitcoin value is not favourable")