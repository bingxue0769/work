#!/usr/bin/python
#__*__ coding:utf-8 _*_


import configparser

conf = configparser.ConfigParser()
conf.read("f:\\conf.conf")
conf.read(filenames, encoding)

# 获取指定的section， 指定的option的值
name = conf.get("section1", "name")
print(name)
age = conf.get("section1", "age")
print (age)

#获取所有的section
sections = conf.sections()
print (sections)

#写配置文件

# 更新指定section, option的值
conf.set("section2", "port", "8081")

# 写入指定section, 增加新option的值
conf.set("section2", "IEPort", "80")

# 添加新的 section
conf.add_section("new_section")
conf.set("new_section", "new_option", "http://www.cnblogs.com/tankxisao")
conf.set("new_section    ", "iii", "33333")

# 写回配置文件
# conf.write(open("f:\\conf.conf","w"))
    