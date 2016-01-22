#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#导入SQLAlchemy：
from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#初始化数据库连接：
#SQLAlchemy用一个字符串表示连接信息：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名(?charset=编码)'。
engine = create_engine('mysql+pymysql://root:@localhost:3306/test?charset=utf8')
#第二种方式设置编码，echo参数表示是否打印日志信息
#engine = create_engine('mysql+pymysql://root:@localhost:3306/test', connect_args={'charset':'utf8'}, echo=True)

#创建DBsession类型：
DBSession = sessionmaker(bind=engine)

#创建对象的基类：
Base = declarative_base()

#定义User对象(如果多个表，就继续定义其它class)：
class User(Base):
    #表的名称：
    __tablename__ = 'user'
    #表的结构：
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    #一对多：
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    #"多"的一方的book表是通过外链关联到user表的：
    user_id = Column(String(20), ForeignKey('user.id'))



#创建session对象：
session = DBSession()

# #创建User对象：
# new_user = User(id='5', name='Lucy')
# #添加到session：
# session.add(new_user)

#Query查询可以直接将映射类或类的属性字段作为参数查询：
#创建Query查询，filter是where条件，可以多层嵌套，最后调用one()返回唯一行，如果调用all()则返回所有行：
user = session.query(User).filter(User.id=='1').one()

print('type: ', type(user))
print('name: ', user.name)
print('book info: ', user.books[1].name)


#提交即保存到数据库(仅查询操作时可省略)：
# session.commit()

#关闭session：
session.close()



