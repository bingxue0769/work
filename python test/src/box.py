#!/usr/bin/python
#__*__ coding:utf-8 _*_


strdd = input("输入str")
screenlen =60
strlen = len(strdd)
boxlen = strlen+10
left_boxmergin = (screenlen-boxlen)//2

print()
print(' ' * left_boxmergin + '+' + '-' * (boxlen-2) + '+' )
print(' ' * left_boxmergin + '|' + ' ' * strlen + '|')
print(' ' * left_boxmergin + '|' +       strdd + '|')
print(' ' * left_boxmergin + '|' + ' ' * strlen + '|')
print(' ' * left_boxmergin + '+' + '-' * (boxlen-2) + '+' )
print()
