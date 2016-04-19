#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

# 使用缩进来代替换行，严格使用相同的缩进，不然报错
if True:
    print "Answer"
    print "True"
else:
    print "Answer" # 注释可在语句或表达式行末
	# 没有严格缩进，在执行时保持
print "False"

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''
"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
print "多行注释"

# 用户按下换行就会退出
raw_input("\n\nPress the enter key to exit.");