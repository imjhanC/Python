import requests 

url='https://newsapi.org/v2/top-headlines'
params= {'q' : 'ev car','category':'business','language':'en','apiKey':'5c67d5cecbe34a12bb094d0f4c5bc775' }
## q : title of the article you wanted to search
## category: what kind of news do you want (Business, Entertainment, Health, Science and etc )

response = requests.get(url,params=params)

data = response.json()

for article in data['articles']:
    print(article['title'])
    print(article['article'])