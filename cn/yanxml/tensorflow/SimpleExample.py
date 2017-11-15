#!/usr/bin/python
#coding=gbk
import tensorflow as tf

# a = tf.constant([1.0,2.0],name="a")
# b = tf.constant([2.0,3.0],name="b")
# result = a+b
# sess = tf.Session()
# print sess.run(result)
# sess.close()

def TensorflowExample():
    a = tf.constant([1.0,2.0],name="a")
    b = tf.constant([2.0,3.0],name="b")
    result = a+b
    sess = tf.Session()
    sess.run(result)
    sess.close()
    return result
    # 将计算结果简单的输出

print TensorflowExample()