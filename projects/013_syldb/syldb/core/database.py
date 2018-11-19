from syldb.core import SerializedInterface
from syldb.core.table import Table

class Database(SerializedInterface):

    # 初始化
    def __init__(self,name):
        self.__name = name #数据库名称
        self.__table_names = [] #数据表 list
        self.__table_objs = {} #数据表名和数据表的map

    # 创建 table 
    def create_table(self,table_name,**options):
        if table_name in self.__table_names:
            raise Exception('table exists')
        # 追加数据表名字
        self.__table_names.append(table_name)

        self.__table_objs[table_name] = Table(**options)

    #删除表
    def drop_tables(self,table_name):
        if table_name not in self.__table_names:
            raise Exception('table not exists')

        self.__table_names.remove(table_name)

        self.__table_objs.pop(table_name)

   # 添加表
    def add_table(self,table_name,table):
        if table_name not in self.__table_objs:
            self.__table_names.append(table_name)

            self.__table_objs[table_name] = table

    # 获取表对象
    def get_table_obj(self,name):
        return self.__table_objs.get(name,None)

    # 获取数据库名称
    def get_name(self):
        return self.__name

    # 获取表名称
    def get_table_name(self,index=None):
        length = len(self.__table_names)

        if isinstance(index,int) and -index < length > index:
            return self.__table_names[index]

        return self.__table_names

    # model序列化成json，并存储
    def serialized(self):
        data = {'name':self.__name,'tables':[]}

        for tb_name,tb_data in self.__table_objs.items():
            data['tables'].append(
                [tb_name,tb_data.serialized()]
                )

        return SerializedInterface.json.dumps(data)

    # json反序列化成model
    @staticmethod
    def deserilized(obj):
        data = SerializedInterface.json.loads(obj)

        obj_tmp = DataBase(data['name'])

        for table_name,table_obj in data['tables']:
            obj_tmp.add_table(table_name,Table.deserilized(table_obj))

        return obj_tmp




