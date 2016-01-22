#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
#判断当前目录下是否存在test.db数据库文件，若存在，则删除：
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

#导入SQLite驱动：
import sqlite3

try:
    #连接到SQLite数据库
    #数据库文件是test.db，如果文件不存在，会自动在当前目录创建：
    conn = sqlite3.connect(db_file)
    #创建一个Cursor：
    cursor = conn.cursor()

    #执行SQL语句：
    #cursor.execute('drop table user')
    #创建user表：
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20), score int)')
    #插入记录：
    cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
    cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
    cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
    #Cursor对象执行insert，update，delete语句时，rowcount返回单条语句影响的行数
    #print(cursor.rowcount)

    #执行查询语句：
    #SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数(参数集为list或tuple)
    #cursor.execute('select * from user where id = ?', '1')
    #Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录：
    #values = cursor.fetchall()
    #print(values)

    #返回指定分数区间的名字，按分数从低到高排序
    def get_score_in(low, high):
        cursor.execute('select name from user where score between ? and ?', [low, high])
        values = cursor.fetchall()
        return list(map(lambda x : x[0], values))

    print(get_score_in(60, 100))

#要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露:
finally:
    #关闭Cursor：
    cursor.close()
    #提交事务(仅执行查询操作时可省略)：
    conn.commit()
    #关闭Connection：
    conn.close()



