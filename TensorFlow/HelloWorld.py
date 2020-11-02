#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   HelloWorld.py
@Time    :   2020/05/01 16:49:32
@Author  :   Pengguo GU 
@Contact :   15292093662@163.com
@License :   (C)Copyright 2020-2021 GPG-A
@Desc    :   Tensorflow basic operation
'''

# import packages
import tensorflow as tf
import numpy as np

# 数值精度
npi = np.pi
print(npi)
x = tf.constant(npi,dtype=tf.float32)
y = tf.constant(npi,dtype=tf.float64)
print(x)
print(y)

# 数据类型转化
a = tf.constant(np.pi,dtype=tf.float16)
b = tf.cast(a,tf.double)
print(a,b)
