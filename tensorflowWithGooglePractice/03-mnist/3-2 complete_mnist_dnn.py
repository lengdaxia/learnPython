import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


#mnist 相关常数
INPUT_NODE = 28*28
OUTPUT_NODE = 10

#配置神经网络参数
LAYER1_NODE = 500 # 隐藏层节点数
BATCH_SIZE = 100  # 每批训练样本数量
LEARNING_RATE_BASE = 0.8  #基础数学率
LEARNING_RATE_DECAY = 0.99  #衰减学习率

REGULARZATION_RATE = 0.0001 #描述模型复杂度的正则化项在损失函数中的系数
TRAIN_STEPS = 30000
MOVING_AVERAGE_DECAY = 0.99 #滑动平均衰减率


# 一个辅助函数，给定神经网络的输入和所有参数，计算神经网络的前向传播结果
def inference(input_tensor,avl_class,weights1,biases1,weight2,biases2):
    if avl_class == None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor,weights1) + biases1)
        return  tf.matmul(layer1,weight2) + biases2
    else:
        layer1 = tf.nn.relu(tf.matmul(input_tensor,avl_class.average(weights1) )+ avl_class.average(biases1))
        return tf.matmul(layer1,avl_class.average(weight2)) + avl_class.average(biases2)

# 训练模型的过程
def train(mnist):
    x  = tf.placeholder(tf.float32,[None,INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32,[None,OUTPUT_NODE],name='y-input')

    # 生产隐藏层参数
    weights1 = tf.Variable(tf.truncated_normal([INPUT_NODE,LAYER1_NODE],stddev=0.1))
    biase1 = tf.Variable(tf.constant(0.1,shape=[LAYER1_NODE]))

    # 生产输出层参数
    weights2 = tf.Variable(tf.truncated_normal([LAYER1_NODE,OUTPUT_NODE],stddev=0.1))
    biases2 = tf.Variable(tf.constant(0.1,shape=[OUTPUT_NODE]))

    y = inference(x,None,weights1,weights2,biase1,biases2)