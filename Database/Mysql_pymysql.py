#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#导入mysql驱动：
import pymysql

try:
      #创建数据库连接：
      conn = pymysql.connect(user='root', passwd='', host='localhost', port=3306, db='test', charset='utf8')
      #创建一个Cursor：
      cursor = conn.cursor()

      #创建user表：
      # cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
      #插入记录，这里注意mysql的占位符是%s
      #cursor.execute('insert into user (id, name) values (%s, %s)', ['7', None])
      # cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Aimy'])
      # cursor.execute('insert into user (id, name) values (%s, %s)', ['3', 'Jack'])
      #Cursor对象执行insert，update，delete语句时，rowcount返回单条语句影响的行数
      #print(cursor.rowcount)

      #查询数据：
      cursor.execute('select * from user where id = %s', ['7'])
      # for r in cursor:
      #       print("id:"+str(r[0])+"   name:"+str(r[1]))
      #Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录：
      values = cursor.fetchall()

      print(values)


#要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露:
finally:
      #关闭Cursor：
      cursor.close()
      #提交事务(仅执行查询操作时可省略)：
      conn.commit()
      #关闭Connection：
      conn.close()