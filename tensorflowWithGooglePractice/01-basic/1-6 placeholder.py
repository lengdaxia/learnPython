import tensorflow as tf 

w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

# 定义placeholder作为存放数据的地方，这里的维度也不一定要定义
X = tf.placeholder(tf.float32,shape=(3,2),name='input')
a = tf.matmul(X, w1)
y = tf.matmul(a, w2)

# 初始化
sess = tf.Session()
sess.run(tf.global_variables_initializer())


# 计算结果
r = sess.run(y,feed_dict={X:[[0.7,0.9],[0.1,0.4],[0.8,0.5]]})
print(r)




