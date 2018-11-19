from syldb.core import SerializedInterface
from syldb.core.database import Database

import base64

def _decode_db(content):
    content = base64.decodebytes(content)
    return content.decode()[::-1]

def _encode_db(content):
    content = content[::-1].encode()
    return base64.encodebytes(content)


class Engine:

    def __init__(self,db_name=None,format_type='dict',path='db.data'):

        self.path = path #数据库存放路径名

        self.__current_db = None

        self.__format_type = format_type

        if db_name is not None:
            self.select_db(db_name)

        self.__database_objs = {} #数据库映射表
        self.__database_names = [] #数据库名字集合


    def create_database(self,database_name):
        if database_name in self.__database_names:
            raise Exception('Database exists')

        self.__database_names.append(database_name)
        self.__database_objs[database_name] = Database(database_name)

    def drop_database(self,database_name):

        if database_name not in self.__database_names:
            raise Exception('Database not exists')

        self.__database_names.remove(database_name)

        self.__database_objs.pop(database_name)


    def select_db(self,db_name):
        if db_name not in self.__database_names:
            raise Exception('has not this database')

        self.__current_db = self.__database_objs[db_name]


    def search(self,table_name,fields='*',sort='ASC',**conditions):
        return self.__get_table(table_name).search(fields=fields,sort=sort,format_type = self.__format_type,**conditions)

    def __get_table(self,table_name):

        self.__check_is_choose()

        table = self.__current_db.get_table_obj(table_name)

        if table is None:
            raise Exception('Not table %s'% table_name)

        return table

    def __check_is_choose(self):
        if not self.__current_db or not isinstance(self.__current_db,Database):
            raise Exception('No database choose')


    def insert(self,table_name,**data):
        return self.__get_table(table_name).insert(**data)

    def update(self,table_name,data,**conditions):
        self.__get_table(table_name).update(data,**conditions)

    def delete(self,table_name,**conditions):
        return self.__get_table(table_name).delete(**conditions)



    def create_table(self,name,**options):
        self.__check_is_choose()
        self.__current_db.create_table(name,**options)

    def get_database(self,format_type='list'):
        databases = self.__database_names

        if format_type == 'dict':
            tmp = []
            for database in databases:
                tmp.append({'name':database})
            databases = tmp
        return databases
    
    def get_table(self,format_type='list'):
        self.__check_is_choose()
        tables = self.__current_db.get_table()

        if format_type == 'dict':
            tmp = []
            for table in tables:
                tmp.append({'name':table})
        return tables


    def commit(self):
        self.__dump_databases()

    def rollback(self):
        self.__load_databases()


    def serilized(self):
        return SerializedInterface.json.dumps([

                database.serialized() for database in self.__database_objs.values()
            ])

    @staticmethod
    def deserialized(self,content):
        data = SerializedInterface.json.loads(content)

        for obj in data:
            database = Database.deserialized(obj)

            db_name = database.get_name()

            self.__database_names.append(db_name)
            self.__database_objs[database_name] = database



    def __dump_databases(self):
        with open(self.path ,'wb') as f:
            content = _encode_db(self.serilized())

            f.write(content)

    def __load_databases(self):
        if not os.path.exists(self.path):
            return

        with open(self.path,'rb') as f:
            content = f.read()

        if content:
            self.deserialized(_decode_db(content))


