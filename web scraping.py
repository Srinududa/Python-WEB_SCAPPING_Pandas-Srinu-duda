

import requests
import pandas as pd
from bs4 import BeautifulSoup
response=requests.get('https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree')

# print(response)

soup=BeautifulSoup(response.content, 'html.parser')
# print(soup)

names=soup.find_all('div', class_='_4rR01T')

name=[]
for i in names:
    d=i.get_text()
    name.append(d)
# print(len(name))


prices=soup.find_all('div', class_='_30jeq3 _1_WHN1')
price=[]
for i in prices:
   
    d=i.get_text()
    price.append(d)
# print(len(price))

ratings=soup.find_all('div', class_='_3LWZlK')
rating=[]
for i in ratings:
   d=i.get_text()
   rating.append(d)

rat=ratings[0:24]

# print(len(rating))

links=soup.find_all('a', class_='_1fQZEK')

link=[]
for i in links:
   
    d='https://www.flipkart.com'+i['href']
    link.append(d)
# print(len(link))


images=soup.find_all('img', class_='_396cs4')
image=[]
for i in images:
    d=i['src']
    image.append(d)
img=images[0:24]
# print(image)

df=pd.DataFrame()

df['name']=name
df['prices']=price
df['ratings']=rat
df['images']=img
df['links']=link

df.to_csv('mobile_data.csv')





