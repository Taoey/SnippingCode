#coding=utf-8
'''
test_succeed
'''
from pymongo import MongoClient

#连接数据库
client=MongoClient()
db=client.Taoey

#查找信息,获得cursor对象,可以利用for循环获取对象的信息
p=db.QQ_group.find({},{"_name":1,"_num":1,"_id":0})
# print(type(p))
# print(p)

# 数据的输出
for i in p:
    print(i["_name"]+":"+i["_num"])