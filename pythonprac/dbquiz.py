from pymongo import MongoClient
client = MongoClient('localhost', 27017) #내 컴퓨터에 돌아가는 mongoDB에 접속
db = client.dbsparta #dpsparta 라는 db이름으로 접속할 겁니다

# 한 개 찾기 - 예시
target_movie = db.movies.find_one({'title':'매트릭스'}) #딕셔너리값 나옴
# print(target_movie['star'])

target_star=target_movie['star']
movies = list(db.movies.find({'star':target_star}))
# for movie in movies:
#     print(movie['title'])

db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': '0'}})