import tensorflow as tf


# 可以使用固定的学习率
fixed_learn_rate = 0.001

# 也可以使用衰减的学习率，根据训练轮数衰减
# 定义一个衰减率
decay_rate = 0.99 # 衰减率
global_steps = 5000 #总训练步数
decay_step = 50 #衰减速度

decay_learn_rate = fixed_learn_rate * decay_rate ^ (global_steps/decay_step)


# tf decay_learn_rate
global_step = tf.Variable(0)

# 通过exponential_decay 函数生成学习率
learn_rate = tf.train.exponential_decay(learn_rate=0.1,global_step=global_step,decay_steps=100,decay_rate=0.96,staircase=True)

# 使用衰减的学习率，在minimize函数中传入global_step
learning_step = tf.train.GradientDescentOptimizer(learn_rate).minimize(loss=None,global_step=global_step)




