from pymongo import MongoClient
client = MongoClient('localhost', 27017) #내 컴퓨터에 돌아가는 mongoDB에 접속
db = client.dbsparta #dpsparta 라는 db이름으로 접속할 겁니다

# insert/find/update/delete

# doc = {'name':'jane','age':21} #mongoDB는 딕셔너리가 쌓이는 것!
# db.users.insert_one(doc)

# same_ages = list(db.users.find({},{'_id':False})) #id값 True하면 랜덤id값도 가지고 옴
# for person in same_ages:
#     print(person)

# user = db.users.find_one({'name':'bobby'},{'_id':False})
# print(user)

# db.users.update_one({'name':'bobby'},{'$set':{'age':19}}) #원래 21살이었는데 19살로 바뀜

# db.users.delete_one({'name':'bobby'}) #bobby 사라짐


# 저장 - 예시
doc = {'name':'bobby','age':21}
db.hering.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})