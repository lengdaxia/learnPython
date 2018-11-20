# _*_ coding:utf-8 _*_
from syldb import Engine
from syldb.case import *
from syldb.core.field import Field,FieldType,FieldKey


e = Engine()                    # 实例化数据库引擎对象
e.create_database('test_db')
e.select_db('test_db')          # 选择数据库 test_db
e.create_table(name='t_test',f_id=Field(data_type=FieldType.INT,keys=[FieldKey.PRIMARY,FieldKey.INCREMENT]),
                f_name=Field(data_type=FieldType.VARCHAR,keys=[FieldKey.NOT_NULL]),
                f_age=Field(data_type=FieldType.INT,keys=[FieldKey.NOT_NULL])
    )
# 向表 `t_test` 中添加一些数据
e.insert(table_name='t_test', f_name='shiyanlou_003', f_age=30)
e.insert(table_name='t_test', f_name='shiyanlou_004', f_age=40)
e.insert(table_name='t_test', f_name='xiaoming', f_age=50)
e.insert(table_name='t_test', f_name='echo', f_age=50)


print("-"*5, "this is table t_test data", "-"*5)
all_data = e.search("t_test")
for i in all_data:
    print(i)
print("-" * 30)


print("-"*5, "search people age >= 30", "-"*5)
test1_data = e.search(table_name="t_test", f_age=GreaterCase(30))
for i in test1_data:
    print(i)
print("-" * 30)

# 保存更改到数据库中
e.commit()

e.run()
