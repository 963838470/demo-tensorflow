import tensorflow as tf
# 创建一个变量, 初始化为标量 0.
state = tf.Variable(0)

# 创建一个 op, 其作用是使 state 增加 1

one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# 启动图, 运行 op
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())  # 初始化所哟变量
    print(sess.run(state))  # 打印 'state' 的初始值
    for _ in range(3):
        sess.run(update)
        # 运行 op, 更新 'state', 并打印 'state'
        print(sess.run(state), sess.run(new_value))

