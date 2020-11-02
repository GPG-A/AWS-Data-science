#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   HelloWorld.py
@Time    :   2020/05/01 14:02:12
@Author  :   Pengguo GU 
@Contact :   15292093662@163.com
@License :   (C)Copyright 2020-2021 GPG-A
@Desc    :   Learn baout Tensor
'''

# import packages

import torch
# 构造一个5×3矩阵，不初始化
x = torch.empty(5,3)
# print(x)

# 构造一个随机初始化的矩阵
y = torch.rand(5,3)
# print(y)

# 构造一个零矩阵
z = torch.zeros(5,3,dtype=torch.long)
# print(z)

# 构造一个Tensor,Tensor就是一个多维数组multidimensional array
a1 = torch.tensor([5.5,3])
print(a1,a1.dtype)

# 构造一个与size大小相同的用1填充的张量。new_ones(size, dtype=None, device=None, requires_grad=False) → Tensor
a2 = a1.new_ones(5,3,dtype=torch.double)
print(a2,a2.size())

# 创建一个 tensor 基于已经存在的 tensor
a3 = torch.randn_like(a2,dtype=torch.float)
print(a3,a3.dtype,a3.size())

# 加法
print(a2+a3)