#!/usr/bin/python
# -*- coding: UTF-8 -*-

print "�ַ���Demo: "

# �ַ���ʹ�� "" ��ʶ
str = 'Hello World!'

print str # ��������ַ���
print str[0] # ����ַ����еĵ�һ���ַ�
print str[2:5] # ����ַ����е������������֮����ַ���
print str[2:] # ����ӵ������ַ���ʼ���ַ���
print str * 2 # ����ַ�������
print str + "TEST" # ������ӵ��ַ���

print ""
print "����Demo: "

# ����ʹ�� [] ����ʶ
# ����ֵ���Ը����±�������
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list # ��������б�
print list[0] # ����б�ĵ�һ��Ԫ��
print list[1:3] # ����ڶ�������������Ԫ�� 
print list[2:] # ����ӵ�������ʼ���б�ĩβ������Ԫ��
print tinylist * 2 # ����б�����
print list + tinylist # ��ӡ��ϵ��б�

print ""
print "Ԫ��Demo: "

# Ԫ��ʹ��()����ʶ����ֵֻ�ܿɶ�
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print tuple # �������Ԫ��
print tuple[0] # ���Ԫ��ĵ�һ��Ԫ��
print tuple[1:3] # ����ڶ�������������Ԫ�� 
print tuple[2:] # ����ӵ�������ʼ���б�ĩβ������Ԫ��
print tinytuple * 2 # ���Ԫ������
print tuple + tinytuple # ��ӡ��ϵ�Ԫ��

print ""
print "�ֵ�Demo: "
"""
�ֵ�(dictionary)�ǳ��б�����python֮���������������ݽṹ���͡��б�������Ķ����ϣ��ֵ�������Ķ��󼯺ϡ�
����֮����������ڣ��ֵ䵱�е�Ԫ����ͨ��������ȡ�ģ�������ͨ��ƫ�ƴ�ȡ��
"""

# ʹ�� {} ��ʶ�ֵ�
# ʹ�÷�ʽ���� C++ �� map
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one'] # �����Ϊ'one' ��ֵ
print dict[2] # �����Ϊ 2 ��ֵ
print tinydict # ����������ֵ�
print tinydict.keys() # ������м�
print tinydict.values() # �������ֵ