import tensorflow as tf

# 声明两个变量 w1,w2
w1 = tf.Variable(tf.random_normal((2,3),stddev=2,seed=1))
w2 = tf.Variable(tf.random_normal((3,1),stddev=2,seed=1))


x = tf.constant([[0.7,0.9]])
print(x)

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

sess = tf.Session()

# 写法1
sess.run(w1.initializer)#初始化w1
sess.run(w2.initializer)#初始化w2

# 写法2  初始化所有相关变量
# init_op = tf.global_variables_initializer()
# sess.run(init_op)

print(sess.run(y))

sess.close()