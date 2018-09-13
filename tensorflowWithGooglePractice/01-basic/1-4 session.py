import tensorflow as tf

# 方法 1
# 1 创建一个会话
sess = tf.Session()

# 2 使用会话来运行计算
# sess.run()

# 3 计算完成之后记得关闭session
sess.close()


print('-*-'*10)
# 方法2
# 1 上下文管理器来创建会话
with tf.Session() as sess:

    # 2 使用
    sess.run()
# 3 不需要关闭，自动管理资源释放


print('-*-'*10)
# tf.Tensor.eval
sess = tf.Session()
with sess.as_default():
    print(result.eval())