import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017) #내 컴퓨터에 돌아가는 mongoDB에 접속
db = client.dbsparta #dpsparta 라는 db이름으로 접속할 겁니다

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작


title=soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
print(title.text)
print(title['href'])

trs=soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a_tag=tr.select_one('td.title>div>a')
    if a_tag is not None:
        rank=tr.select_one('td:nth-child(1)>img')['alt']
        title=a_tag.text
        star=tr.select_one('td.point').text
        doc={
            'title':title,
            'rank':rank,
            'star':star
        }
        db.hering.insert_one(doc)