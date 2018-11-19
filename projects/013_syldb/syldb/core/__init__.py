import json

# 数据库核心模块序列化接口
class SerializedInterface:
    # 内部定义一个json对象，方便后续操作不需要import
    json = json

    # 反序列化方法
    @staticmethod
    def deserialized(obj):
        raise NotImplementedError

    # 序列化方法
    def serialized(self):
        raise NotImplementedError


from enum import Enum 

# 字段类型枚举
class FieldType(Enum):
    INT = int = 'int'  #整型
    VARCHAR = varchar = 'str' #字符型
    FLOAT = float = 'float' #浮点型

# 数据类型映射
TYPE_MAP = {
    'int':int,
    'float':float,
    'str':str,
    'INT':int,
    'FLOAT':float,
    'VARCHAR':str
}

# 字段主键枚举
class FieldKey(Enum):

    PRIMARY='PRIMARY KEY'           #主键约束
    INCREMENT = 'AUTO_INCREMENT'    #自增约束
    UNIQUE = 'UNIQUE'               #唯一约束
    NOT_NULL = 'NOT_NULL'           #非空约束
    NULL = 'NULL'                   #可空约束，坐位默认的约束使用


