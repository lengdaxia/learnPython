# encoding:utf-8

from syldb.core import FieldKey,FieldType,TYPE_MAP
from syldb.core import SerializedInterface

# 数据字段对象
class Field(SerializedInterface):

    def __init__(self,data_type,keys=FieldKey.NULL,default=None):

        self.__type = data_type # 数据字段类型
        self.__keys = keys       # 字段的数据约束
        self.__default = default # 默认值
        self.__values = []       # 字段数据
        self.__rows = 0          # 字段数据长度

        # 如果约束只有一个，并且非list类型，则转换成 list
        if not isinstance(self.__keys,list):
            self.__keys = [self.__keys]

        # 如果类型不属于 FieldType ，抛出异常 
        if not isinstance(self.__type,FieldType):
            raise TypeError('Data-Types require type of "FieldType"')

        # 如果类型不属于 FieldKey，抛出异常
        for key in self.__keys:
            if not isinstance(key,FieldKey):
                raise TypeError('Data-keys require type pf "FieldKey"')
        #如果有自增约束，继续判断是否为整型和是否有主键约束
        if FieldKey.INCREMENT in self.__keys:
            # 如果不是整型，抛出类型错误异常
            if self.__type != FieldType.INT:
                raise TypeError('Increment key require Data-Type is integer')
            #如果没有主键约束，抛出无主键约束异常
            if FieldKey.PRIMARY not in self.__keys:
                raise Exception('Increment key require primary key')

        #如果设置了唯一约束，则改值不能为设置空的默认值
        if self.__default is not None and FieldKey.UNIQUE in self.__keys:
            raise Exception('Unique key not allow to set default value')


    # 检查是否符合数据类型
    def __check_type(self,value):
        if value is not None and not isinstance(value,TYPE_MAP[self.__type.value]):
            raise TypeError('data type error ,value must be %s' % self.__type)

    #检查指定位置的数据是否存在
    def __check_index(self,index):
        if not isinstance(index,int) or not -index < self.__rows > index:
            raise Exception('Not this element')
        return True

    # 键值约束
    def __check_keys(self,value):

        #如果字段包含自增键，则选择合适的值自动自增
        if FieldKey.INCREMENT in self.__keys:
            # 如果值为空，则用字段数据长度作为基值自增
            if value is None:
                value = self.__rows + 1

            # 如果值已经存在，则抛出一个值已经存在的异常
            if value in self.__values:
                raise Exception('value %s exists' % value)

        #如果字段包含主键约束或者唯一约束，判断值是否存在
        if FieldKey.PRIMARY in self.__keys or FieldKey.UNIQUE in self.__keys:
            # 如果值已经存在，抛出存在异常
            if value in self.__values:
                raise Exception('Value %s exists' % value)

        # 如果该字段包含主键或者非空键，并且添加的值为空值，则抛出值不能为空异常
        if (FieldKey.PRIMARY in self.__keys or FieldKey.NOT_NULL in self.__keys ) and value is None:
            raise Exception('Field Not Null')

        return value

    # 获取有多少条数据
    def length(self):
        return self.__rows

    #获取数据
    def get_data(self,index=None):
        if index is not None and self.__check_index(index):
            return self.__values[index]
        return self.__values

    # 添加数据
    def add(self,value):
        if value is None:
            value = self.__default
        # 判断数据是否符合约束要求
        value = self.__check_keys(value)
        #检查数据是否符合数据类型
        self.__check_type(value)
        #追加数据
        self.__values.append(value)
        #数据长度 + 1
        self.__rows += 1


    def delete(self,index):
        # 检查删除的index是否越界
        self.__check_index(index)
        # 删除数据
        self.__values.pop(index)
        # 数据长度 -1
        self.__rows -= 1

    # 修改数据
    def modify(self,index,value):
        # 检查是否越界
        self.__check_index(index)
        # 检查键值约束
        value = self.__check_keys(value)
        # 检查数据类型
        self.__check_type(value)
        # 替换原来的数据
        self.__values[index] = value


    def get_keys(self):
        return self.__keys

    def get_type(self):
        return self.__type

    def length(self):
        return self.__rows


# 模型序列化为json
    def serialized(self):
        return SerializedInterface.json.dumps(
            {
                'key':[key.value for key in self.__keys],
                'type':self.__type.value,
                'values':self.__values,
                'default':self.__default
            })

# json反序列化为模型
    @staticmethod
    def deserialized(data):
        json_data = SerializedInterface.json.loads(data)

        keys = [FieldKey(key) for key in json_data['key']]

        obj = Field(FieldType(json_data['type']),keys,default=json_data['default'])

        for value in json_data['values']:
            obj.add(value)

        return obj
