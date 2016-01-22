#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，
也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
'''

# 定义Field类，它负责保存数据库表的字段名和字段类型:
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 创建Model的元类ModelMetaclass：
class ModelMetaclass(type):
    #__new__(当前准备创建的类的对象，类的名字，类继承的父类集合，类的方法集合)
    def __new__(cls, name, bases, attrs):
        #排除掉对Model类的修改：
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)

        print('Found model: %s' % name)

        #在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，
        #同时从类属性中删除该Field属性，否则，容易造成运行时错误(Model继承了dict，属于类字典，同样User也是类字典。
        # 因为初始化User对象时，其实就是初始化一个字典，但存在类属性名与 字典中的键 重名的情况，这样u.id 访问倒是IntegerField('id')，
        # 而不是所期望的u['id'],所以在元类中要删除id,name这些类属性，并通过__getattr__()的定制方法，使其u.id 等价于 u['id'])
        mappings = dict()           #声明dict字典类型
        for k, v in attrs.items():  #dict.items()返回一个由tuple(包含key,value)组成的list
            #判断attrs字典值是否为Field类型(自己定义的)
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                #填充attrs对值到mappings字典中：
                mappings[k] = v
        for k in mappings.keys():   #dict.keys()返回一个由key(字典的目录)值组成的list
            #删除attrs字典中对应的值(其实就是清空attrs字典)：
            attrs.pop(k)

        #重新构造attrs字典：
        attrs['__mappings__'] = mappings    # 保存属性和列的映射关系
        attrs['__table__'] = name   # 把表名保存到__table__中，这里简化为表名默认为类名。(假设表名和类名一致)
        return type.__new__(cls, name, bases, attrs)


# 创建基类 Model：
class Model(dict, metaclass=ModelMetaclass):
    #初始化已实例化后的所有父类对象，方便后续使用或扩展父类中的行为：
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    #属性动态化处理；当使用点号获取类实例属性时，如果属性不存在就自动调用__getattr__方法。
    def __getattr__(self, key):     #此处为自动返回指定字典key的value值，没找到则抛出异常：
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    #属性动态化赋值；当设置类实例属性时自动调用。
    def __setattr__(self, key, value):
        self[key] = value

    #在Model类中，可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等...
    def save(self):
        fields = []
        params = []
        args = []
        #循环出传递进来的字段值和字段名：
        #此处的'self.__mappings__'字典是ModelMetaclass中重构的attrs字典内的'__mappings__'字典：
        for k, v in self.__mappings__.items():    #dict.items()返回一个由tuple(包含key,value)组成的list
            fields.append(v.name)       #重建字段名list； v(自定义的Field类型)中包含两个属性：name(传进来的值)，value(值的类型)。
            params.append('?')          #根据字段数构造一个'？'组成的list用于后面作参数替换符串。
            #getattr(对象(Instance)，属性(name,字符串)，[default])：如果对象中有属性，则返回该属性的值，相当于Instance.name，若没有则返回default值。
            #此处的self为初始化User对象(User继承Model继承dict)时的dict实例，包含了初始化值(id, name, emai, password)：
            args.append(getattr(self, k, None))     #重建字段值list。提取字典内，指定key值的value，没有的返回None。
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('FIELDS: %s' % str(fields))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


#调用接口
#当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，
# 如果没有找到，就继续在父类Model中查找metaclass，找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类:
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 模拟保存到数据库：
u.save()
