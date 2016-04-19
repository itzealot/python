#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 需要使用 UTF-8 编码

import sys;

"""
Python中的变量不需要声明，变量的赋值操作既是变量声明和定义的过程。
每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。
"""

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print counter
print miles
print name

# 定义变量并同时赋值
a1 = a2 = a3 = 1;

print (a1);
print a1;
print a2;
print a3;

aa = "aa"
# 字符串与数值不能同时输出
# 单行输出
sys.stdout.write("a1 = " + aa + '\n');

# 定义变量并依次赋值
b1, b2, b3 = 1, 2, "33333john";
print b1;
print b2;
print b3;

