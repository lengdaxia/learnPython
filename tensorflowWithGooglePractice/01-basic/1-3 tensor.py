import tensorflow as tf 

# 张量可以被简单理解成多维数组
# 零阶张量表示标量 scalar
# 第一阶张量为向量（vector）
# 第n阶张量，理解成n维数组


# 1 使用张量记录中间结果
a = tf.constant([1.0,2.0],name='a')
b = tf.constant([2.0,3.0],name='b')

result = tf.add(a, b,name='add')
print (result)
# output: Tensor("add:0", shape=(2,), dtype=float32)
# 'add:0' 表示add输出的第一个结果
# shape=(2,),表示结果是一个一维数组
# dtype=float32 ,表示张量的类型，类型不匹配会报错

# 下面的报错，类型不匹配
# a = tf.constant([1,2],name='a')
# result = tf.add(a, b,name='add')
# print(result)


# tf支持14中张量类型 
# tf.int8,16,32,64
# tf.uint8,16,32,64
# tf.float32,64
# tf.bool
# tf.complex64,128


print('-*-'*10)
#  直接计算向量和
result = tf.constant([1.0,2.0],name='a') + tf.constant([2.0,3.0],name='b')
with tf.Session() as sess:
    print(sess.run(result))






