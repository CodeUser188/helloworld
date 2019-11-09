#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle as p
import time

url = "F:\0000练习--c,keil,py,wut,ect\py_练习\AdressBook"      #$URL, the path of the file will be generated

class person:
    notes={}   #创建字典
    def add(self):
        name = input('请输入要添加的联系人姓名')
        time.sleep(0.2)
        if name in person.notes:
            print('该联系人已经存在')
        else:
          telephone =  (input('请输入联系人电话号码'))
          addr =  (input('请输入联系人地址'))
          label = {'电话':telephone,'地址':addr}
          person.notes[name]=label

    def dele(self):
      name = (input('请输入要删除的联系人姓名'))
      time.sleep(0.2)
      if name in person.notes:
        del person.notes[name]
        print ("%s" %  person.notes.items())
      else:
        print('联系人 %s 不存在'%name)

    def search(self):
      name = (input('请输入要搜索的联系人姓名'))
      time.sleep(0.2)
      if name in person.notes:
         print('联系人 %s 的\n电话号码是 %s ,\n地址是 %s'%(name,person.notes[name]['电话'],person.notes[name]['地址']))
      else:
         print('联系人 %s 不存在'%name)

    def modify(self):
      name = (input('请输入要编辑的联系人姓名'))
      time.sleep(0.2)
      if name in person.notes:
        telephone =  (input('请输入联系人电话号码'))
        addr =  (input('请输入联系人地址'))
        person.notes[name]['电话']=telephone
        person.notes[name]['地址']=addr
      else:
        print('联系人 %s 不存在\n若要编辑请选择添加选项'%name)
    
    def write(self):
      time.sleep(0.2)
      f = open('联系人.txt','wb+')
      p.dump(person.notes,f)
      f.close()
    
    def read(self):
      time.sleep(0.2)
      file = url + '联系人.txt'        #FILE= URL + NAME
      try:
        f = open(file ,'rb+')
        person.notes = p.load(f)
        f.close()
      except:
        f = open(file ,'w')
        f.close()
    
    def show(self):
      print(person.notes)

def menu():  #定义函数menu()显示功能菜单  
    print('''系统提供以下功能
    1：添加
    2：删除
    3：修改
    4：搜索
    5：退出
    6: 显示全部联系人信息''')

people = person()
people.read()
while True:
  try:
    menu()
    choice = int(input('请输入相应数字操作'))   
    if choice == 1:
        people.add()
    elif choice == 2:
        people.dele()
    elif choice == 3:
        people.modify()
    elif choice == 4:
        people.search()
    elif choice == 5:
        people.write()
        break
    elif choice == 6:
        people.show()
    else:
        print('输入不合法，请输入合法数字')
        time.sleep(1)
  except ValueError:
      print('请输入数字选项')
      time.sleep(1)
