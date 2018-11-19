from syldb.core import SerializedInterface
from syldb.core.field import Field,FieldType,FieldKey

# 创建表
# table = Table(f_id = Field(data_type = FieldType.INT,keys= [FieldKey.PRIMARY,FieldKey.INCREMENT],f_name=Field(data_type=FieldType.VARCHAR,keys=FieldKey.UNIQUE))

# 数据表对象
class Table(SerializedInterface):

    def __init__(self,**options):
        self.__field_names = [] #数据表的所有字段名
        self.__field_objs = {}  #数据表字段名和字段对象的映射
        self.__rows = 0         #数据条目数量

        # 获取所有字段名和字段对象为数据表初始化字段
        for filed_name ,field_obj in options.items():
            # 进行字段添加
            self.add_field(filed_name,field_obj)

    # 添加新字段
    def add_field(self,filed_name,field_obj,value=None):

        # 如果新添加的字段名已经存在，抛出字段已存在的异常
        if filed_name in self.__field_names:
            raise Exception('Field Exists')
        # 如果field_obj 不为 Field对象，抛出类型错误异常
        if not isinstance(field_obj,Field):
            raise TypeError('type error,value must be %s' % Field)
        #添加字段名
        self.__field_names.append(filed_name)

        # 绑定字段名和字段
        self.__field_objs[filed_name] = field_obj

        # 如果已存在其他字段
        if len(self.__field_names) > 1:

            length = self.__rows

            field_obj_length = field_obj.length()

            if field_obj_length != 0:
                if field_obj_length == length:
                    return

                raise Exception('Fiedl data length inconformity')

            for index in range(0,length):
                if value:
                    self.__get_field(filed_name).add(value)
                else:
                    self.__get_field(filed_name).add(None)
        else:
            self.__rows = field_obj.length()

# 查询数据，
    def search(self,fields,sort,format_type,**conditions):

        # 如果要查询的字段是* ，则返回所有字段对应的数据
        if fields == '*':
            fields = self.__field_names
        else:
            # 判断查询的字段是否存在，不存在则抛出异常
            for filed in fields:
                if field not in self.__field_names:
                    raise Exception('%s field not Exists' % field)

        # 初始化查询结果变量为一个空的list
        rows = []
        # 解析条件，并返回符合条件的数据索引
        match_index = self.__parse_conditions(**conditions)

        # 遍历符合条件的数据索引，根据指定的返回格式返回数据
        for index in match_index:
            # 返回list类型的数据，也就是没有字段名
            if format_type == 'list':
                row = [self.__get_field_data(filed_name,index) for filed_name in fields]
            elif format_type == 'dict': #返回dict类型的数据，也就是字段和值成键值对
                row = {}
                for filed_name in fields:
                    row[filed_name] = self.__get_field_data(filed_name,index)
            else:
                # 如果找不到类型，抛出格式错误异常
                raise Exception('format type invalid')
            rows.append(row)
        # 默认为升序，如果选择了倒序，则倒序后返回
        if sort == 'DESC':
            rows = rows[::-1]
        return rows

    # 获取 Field对象
    def __get_field(self,field_name):
        if field_name not in self.__field_names:
            raise Exception('%s field not exist' % field_name)
        return self.__field_objs[field_name]

    # 获取字段中的数据
    def __get_field_data(self,filed_name,index = None):
        # 获取Field对象
        field = self.__get_field(field_name)

        return field.get_data(index)

    def __parse_conditions(self,**conditions):

        # 如果条件为空，数据索引为所有，反之为匹配条件的索引
        match_index = range(0,self.__rows)
        return match_index


    def delete(self,**conditions):
        # 获取符合条件的数据索引
        match_index = self.__parse_conditions(**conditions)
        # 遍历所有的Field对象
        for field_name in self.__field_names:
            count = 0
            match_index.sort()

            tmp_index = match_index[0] #当前Field对象所删除的第一个索引值
            # 遍历所有匹配的索引
            for index in match_index:
                # 如果当前索引大于第一个删除的索引值，则index减去count
                if index > tmp_index:
                    index = index - count
                # 删除对应位置的数据
                self.__get_field(field_name).delete(index)
                # 每删除一次，次数加1
                count += 1
        # 重新获取数据长度
        self.__rows = self.__get_field_length(self.__field_names[0])

    # 获取 Field对象长度
    def __get_field_length(self,field_name):

        field = self.__get_field(field_name)
        return field.length()

    # 更新参数
    def update(self,data,**conditions):
        # 获取符合条件搜索之后的缩印值
        match_index = self.__parse_conditions(**conditions)
        #
        name_tmp = self.__get_name_tmp(**data)

        for field_name in name_tmp:
            for index in match_index:
                self.__get_field(field_name).modify(index,data[field_name])

    # 解析参数中包含的字段名
    def __get_name_tmp(self,**options):
        name_tmp = []

        params = options

        for field_name in params.keys():
            if field_name not in self.__field_names:
                raise Exception('%s Field not exist' % field_name)

            name_tmp.append(field_name)
        return name_tmp


    def insert(self,**data):
        if 'data' in data:
            data = data['data']

        name_tmp = self.__get_name_tmp(**data)

        for field_name in self.__field_names:
            value = None

            if field_name in name_tmp:
                value = data[field_name]

            try:
                self.__get_field(field_name).add(value)
            except Exception as e:
                raise Exception(field_name,str(e))

        self.__rows += 1


    def serialized(self):
        data = {}

        for field in self.__field_names:
            data[field] = self.__field_objs[field].serialized()

        return SerializedInterface.json.dumps(data)


    @staticmethod
    def deserialized(data):
        json_data = SerializedInterface.json.loads(data)

        table_obj = Table()

        field_names = [field_name for field_name in json_data.keys()]

        for field_name in field_names:

            field_obj = Field.deserialized(json_data[field_name])

            table_obj.add_field(field_name,field_obj)

        return table_obj

