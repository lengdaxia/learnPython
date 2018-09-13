import tensorflow as tf 

y = tf.sigmoid(y)

corss_entropy = -tf.reduce_mean(
                                y_ *tf.log(tf.clip_by_value(y,1e-10,1.0)) + 
                                (1-y)*tf.log(tf.clip_by_value(1-y,1e-10,1.0))
                                )

learning_rate = 0.001
train_step = tf.train.AdamOptimizer(learning_rate).minimize(corss_entropy)