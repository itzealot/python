#!/usr/bin/python
# -*- coding: UTF-8 -*-

# the circle while
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"

# continue �� break �÷�
i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # ��˫��ʱ�������
        continue
    print i         # ���˫��2��4��6��8��10
	
# break �÷�	
i = 1
while 1:            # ѭ������Ϊ1�ض�����
    print i         # ���1~10
    i += 1
    if i > 10:     # ��i����10ʱ����ѭ��
        break

# ѭ��ʹ�� else ���
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
# else
else:
   print count, " is not less than 5"

