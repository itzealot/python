#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 21
b = 10
c = 0

print "a = ", a
print "b = ", b

print "add value is ", a + b

print "sub value is ", a - b

print "mul value is ", a * b

c = a / b
print "div value is ", a / b

c = a % b
print "% value is ", a % b

a = 2
b = 3
print "2^3 value is ", a**b

a = 10.2
b = 5
print "10.2 / 5 = ", a//b

# �Ƚ�����
a = 21
b = 10
c = 0

# �Ƿ����
if ( a == b ):
   print "Line 1 - a is equal to b"
else:
   print "Line 1 - a is not equal to b"

# ������- �Ƚ����������Ƿ����
if ( a != b ):
   print "Line 2 - a is not equal to b"
else:
   print "Line 2 - a is equal to b"

# ������- �Ƚ����������Ƿ����
if ( a <> b ):
   print "Line 3 - a is not equal to b"
else:
   print "Line 3 - a is equal to b"

# С�� 
if ( a < b ):
   print "Line 4 - a is less than b" 
else:
   print "Line 4 - a is not less than b"

# ���� 
if ( a > b ):
   print "Line 5 - a is greater than b"
else:
   print "Line 5 - a is not greater than b"

a = 5;
b = 20;
if ( a <= b ):
   print "Line 6 - a is either less than or equal to  b"
else:
   print "Line 6 - a is neither less than nor equal to  b"

if ( b >= a ):
   print "Line 7 - b is either greater than  or equal to b"
else:
   print "Line 7 - b is neither greater than  nor equal to b"