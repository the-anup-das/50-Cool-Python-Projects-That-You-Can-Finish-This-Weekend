import requests

class LiveCurrencyConverter():
    def __init__(self,url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

#obj = LiveCurrencyConverter('https://api.exchangerate-api.com/v4/latest/USD')

#print(obj.data)

print(requests.get('https://api.exchangerate-api.com/v4/latest/USD').json())
