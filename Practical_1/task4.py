import requests
import csv
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)


soup= BeautifulSoup(response.content, 'html.parser')
quotes = soup.findAll("span",attrs={"class":"text"})
authors= soup.findAll("small",attrs={"class":"author"})

##if you want to save to csv file
file =open("scraped_quotes.csv","w")
writer =csv.writer(file)

writer.writerow(["QUOTES","AUTHORS"])

for quote, author in zip(quotes, authors):
    print(quote.text + "-" + author.text)
    writer.writerow([quote.text,author.text])
file.close()