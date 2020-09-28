'''
mysql.py
pymysql操作数据库基本流程演示
'''
import pymysql

#连接数据库
db = pymysql.connect(host='localhost',
                     port = 3306,
                     user = 'root',
                     password = 'my_root_password',
                     database = 'stu',
                     charset = 'utf8')

#获取游标（操作数据库，执行sql语句）
cur = db.cursor()

#执行sql语句
sql = 'insert into class_1 values (6,"Emma",17,"w",76.5,"15368446844");'

cur.execute(sql) #执行语句

db.commit() #将写操作提交，多次写错做一同提交

#关闭游标、数据库
cur.close()
db.close()

