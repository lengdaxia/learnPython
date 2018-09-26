import tensorflow as tf

# 获取一层神经网络的权重，并将这个权重的L2正则化损失加入到losses的集合中
def get_weights(shape, lambdas):

    var = tf.Variable(tf.random_normal(shape=shape),dtype=tf.float32)
    tf.add_to_collection(
        'losses',tf.contrib.layers.l2_regularizer(lambdas)(var)
    )
    return var

x = tf.placeholder(tf.float32,shape=[None,2])
y_ = tf.placeholder(tf.flags,shape=[None,1])

# 定义每一层网络的节点数量
layer_dimensions = [2,10,10,10,1]
# 神经网络的层数
n_layers = len(layer_dimensions)

# 这个变量维护前向传播时候最深层的节点，开始时就是说输入层
cur_layer = x
# 定义当前层的节点个数
in_dimension = layer_dimensions[0]

for i in range(1,n_layers):
    # 输出层的节点个数，也是下一层的输入节点数量
    # 更新输出层
    out_dimension = layer_dimensions[i]
    # 更新权重，加入了l2正则化
    weight = get_weights([in_dimension,out_dimension],0.001)
    bias = tf.Variable(tf.constant(0.1,shape=[out_dimension]))

#     使用relu
    cur_layer = tf.nn.relu(tf.matmul(cur_layer,weight) + bias)
    # 更新输入层
    in_dimension = layer_dimensions[i]

mse_loss = tf.reduce_mean(tf.square(y_,cur_layer))

# 将均方误差损失函数加入到损失集合中
tf.add_to_collection('losses',mse_loss)

# 将 losses列表中的所有损失项 加起来，就是最终的损失函数
loss = tf.add_n(tf.get_collection('losses'))

