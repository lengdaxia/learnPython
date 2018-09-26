import tensorflow as tf

# 1 交叉熵 ，计算预测的概率分布和真实答案的概率分布之间的距离
# y_ ,y = 0,0
# corss_entropy = tf.reduce_mean(y_ *tf.log(tf.clip_by_value(y,1e-10,1.0)))

# 2 softmax
# cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y_,logits=y)

# 3 MSE mean sqaured error 回归问题的损失函数计算
# mse = tf.reduce_mean(tf.square(y_ - y))


from numpy.random import RandomState
batch_size = 8

# 两个输入节点
x = tf.placeholder(tf.float32,shape=(None,2),name='x-input')
# 回归问题一般只有一个输出节点
y_ = tf.placeholder(tf.float32,shape=(None,1),name='y-input')


# 定义一个单层的神经网络前向传播算法，这里是简单加权
w1 = tf.Variable(tf.random_normal([2,1],stddev=1,seed=1))
y = tf.matmul(x,w1)

# 定义预测多了和预测少了的成本
loss_more = 10
loss_less = 1
loss = tf.reduce_mean(tf.where(tf.greater(y,y_),(y-y_) * loss_more,(y_-y)*loss_less))

train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

# 通过随机数生成一个模拟数据集
ram = RandomState(1)
dataset_size = 128
X = ram.rand(dataset_size,2)

#  设置回归的正确值为两个输入的和加上一个噪音，噪音的取值范围在 -0.5~0.5之间
Y = [[x1+x2 + ram.rand()/10.0 -0.05] for (x1,x2) in X]

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    STEPS = 5000
    for i in range(STEPS):
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size,dataset_size)
        sess.run(train_step,
                 feed_dict={x:X[start:end],y_:Y[start:end]})
        print(sess.run(w1))
