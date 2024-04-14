import requests
from bs4 import BeautifulSoup
url=input("Enter the url:")
#url = 'https://www.reddit.com/'
#url = 'https://en.wikipedia.org/wiki/Human_evolution'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print("1.contents in quotes")
print("2.links")
print("3.headings")
n=int(input("enter the choice:"))
if(n==1):
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').text.strip()
        print(text)
if(n==2):
    links = soup.find_all('a')
    for link in links:
        print('URL:', link.get('href'))
if(n==3):
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for heading in headings:
        print(heading.text.strip())



