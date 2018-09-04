import pymongo
  
client=pymongo.MongoClient("mongodb://192.168.126.129:27019")
# 相当与use test1
db=client.test1
print('db=',db)
# 获取集合
t1 = db.t1
print('stu',t1)
# 新建一个字典（json）
s1 = {"name":'杨康','age':18}
t1.insert_one(s1)
# 获取文档的个数
print(t1.count())