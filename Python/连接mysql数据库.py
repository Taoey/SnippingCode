#coding=utf-8
'''
blog : http://www.cnblogs.com/lhuan/p/6160023.html
'''

import pymysql

# main
db=pymysql.connect('localhost','root','password','YourdbName')
cursor=db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print ("Database version : %s " % data)