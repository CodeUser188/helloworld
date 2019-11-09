#!/usr/bin/env python -*- coding:utf-8 -*-
import pickle as p
import time

PATH = r"F:\0000练习--c,keil,py,wut,ect\py_练习\AdressBook\\"       #$URL, the path of the file will be generated
FILE = PATH + '联系人.txt'
Pre = print("waiting...\n")

class person:
    notes={}    #创建字典
    def add(self):
        name = input('请输入要添加的联系人姓名')
        if name=='q0':                                  #禁止使用q0作为联系人姓名
            print("you can't use the name('q0')！")
            time.sleep(1)
            name = (input('请输入要添加的联系人姓名'))
        while(name!='q0'):
            time.sleep(0.2)
            if name in person.notes:
                print('！该联系人已经存在')
                time.sleep(1)
                name = (input('请输入要添加的联系人姓名'))
            else:
                telephone =  (input('请输入联系人电话号码'))
                addr =  (input('请输入联系人地址(备注)'))
                label = {'电话':telephone,'地址(备注)':addr}
                person.notes[name]=label
                break

    def dele(self):        #删除联系人
        name = (input('请输入要删除的联系人姓名'))
        while( name!='q0' ):
            Pre
            time.sleep(0.2)
            if name in person.notes:
                del person.notes[name]
                print ("""\'%s\'成功删除
                       现在联系人有%s """ %  (name,person.notes.items()) )
                break
            else:         #此人不存在时
                print('！联系人 %s 不存在，请重新输入，或按q0退出删除'%name)
                time.sleep(1)
                name = (input('请再次输入要删除的联系人姓名'))
                
    def search(self):       #查找联系人
        name = (input('请输入要搜索的联系人姓名'))
        while(name!='q0'):
            Pre
            time.sleep(0.2)
            if name in person.notes:
                print('联系人 %s 的\n电话号码是 %s ,\n地址(备注)是 %s'%(name,person.notes[name]["电话"],person.notes[name]["地址(备注)"]))
                break
            else:           #查无此人时
                print('联系人 %s 不存在'%name)
                name = (input('请再次输入要查找的联系人姓名'))

    def modify(self):       #编辑联系人信息
        name = (input('请输入要编辑的联系人姓名'))
        while(name!='q0'):
            Pre
            time.sleep(0.2)
            if name in person.notes:
                telephone =  (input('请输入联系人电话号码'))
                addr =  (input('请输入联系人地址(备注)'))
                person.notes[name]["电话"]=telephone
                person.notes[name]["地址(备注)"]=addr
                break
            else:
                print('联系人 %s 不存在\n若要编辑请选择添加选项'%name)
                name = (input('请再次输入要编辑的联系人姓名'))
    
    def write(self):        #写入联系人信息  文件处理
        time.sleep(0.2)
        f = open( FILE ,'wb+')
        p.dump(person.notes,f)
        f.close()
        print("saved\n\ntips:press'exit()' to close project ")
              
    def read(self):     #读取联系人文件
        time.sleep(0.5)
            #FILE= PATH + NAME
                    #PATH = "F:\0000练习--c,keil,py,wut,ect\py_练习\AdressBook\" 
        try:
            f = open( FILE ,'rb+')
            person.notes = p.load(f)
            f.close()
        except:
            f = open( FILE ,'w')
            f.close()
    
    def show(self):     #显示所有联系人信息
        print(person.notes)
        time.sleep(0.5)

def menu():     #定义函数menu()显示功能菜单
    Pre
    time.sleep(1)
    print('''\n>>>系统提供以下功能
！！！ Warning：直接退出会造成数据丢失，退出时请按q0
    0：显示全部联系人信息
    1：添加
    2：删除
    3：修改
    4：搜索
    q0：保存并退出
！！！ Warning：直接退出会造成数据丢失，退出时请按q0''')
people = person()
people.read()
print( "联系人存储文件路径" + PATH )        #show the path of th file
while True:
    menu()
    try:
        choice = input('请输入相应选项完成操作')
        if choice == '0':
            people.show()
        elif choice == '1':
            people.add()
        elif choice == '2':
            people.dele()
        elif choice == '3':
            people.modify()
        elif choice == '4':
            people.search()
        elif choice == 'q0':
            people.write()
            break
            exit()
        else:
            print('！输入不合法，请输入合法数字')
            time.sleep(1)
    except ValueError:
        print('请输入选项')
        time.sleep(1)
