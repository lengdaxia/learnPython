from syldb import Engine
from syldb.core.field import Field,FieldType,FieldKey

e = Engine()
e.create_database('test_db')
e.select_db('test_db')

e.create_table(name='t_test',fid=Field(data_type=FieldType.INT,keys=[FieldKey.PRIMARY,FieldKey.INCREMENT]),
                fname=Field(data_type=FieldType.VARCHAR,keys=[FieldKey.NOT_NULL]),
                fage=Field(data_type=FieldType.INT,keys=[FieldKey.NOT_NULL])
    )

e.insert(table_name='t_test',fname='shiyanlou_001',fage=20)
e.insert(table_name='t_test',fname='shiyanlou_002',fage=10)

ret = e.search('t_test')
for row in ret:
    print(row)


e.commit()