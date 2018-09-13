import tensorflow as tf 

g1 = tf.Graph()
with g1.as_default():
    # 在计算图中个g1中定义变量v。并设置初始值为0
    v = tf.get_variable('v',shape=[1],initializer=tf.zeros_initializer)

g2 = tf.Graph()
with g2.as_default():
    # 在计算图g2中定义变量v，并设置初始值为1
    v = tf.get_variable('v',shape=[1],initializer=tf.ones_initializer)


# 在计算图g1中读取变量‘v’的值
with tf.Session(graph=g1) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("",reuse=True):
        # 在计算图g1中，变量‘v’的取值为 0，所以下面这行会输出【0.】
        print(sess.run(tf.get_variable('v')))


# 在计算图g2中读取变量v的值
with tf.Session(graph=g2) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("",reuse=True):
        print(sess.run(tf.get_variable('v')))


