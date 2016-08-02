#!/usr/bin/python
#__*__ coding:utf-8 _*_
from __future__ import division

#计算器 只能输入+、-、*、/

first =  int(input('请输入第一个数字'))
second = int(input('请输入第二个数字'))
mark = input('输入运算符')


def comp(a,b,c):
    m = ['+','-','*','/']
    while 1:
        result = 0.0
        if c in m:
            if c=='+':
                result = a + b
            elif c=='-':
                result = a - b
            elif c=='*':
                result = a * b
            elif c=='/':
                result = a // b
            print(result)
            break
        else:
            c = input('重新输入符号')
        
        
comp(first,second,mark)

    