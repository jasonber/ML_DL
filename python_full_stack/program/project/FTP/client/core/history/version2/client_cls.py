import struct
import os
import file_oprt
import client_cmd

<<<<<<< HEAD:python_full_stack/project/FTP/client/core/history/version2/client_cls.py

class Action():
=======
# !原来客户端的类也是错的，类的继承好复杂
# !看答案再说吧
class Client(socket.socket):
>>>>>>> 4f185f75ee6397228269610797629977cba9e91d:python_full_stack/project/FTP/client/core/client_cls.py
    #? 这是一个客户端需要与服务端通信，所以要继承socket类
    def __init__(self, request):
        # ? 需要初始化一
<<<<<<< HEAD:python_full_stack/project/FTP/client/core/history/version2/client_cls.py
        self.request = request
=======

        # self.request = super().accept(ip_port)
>>>>>>> 4f185f75ee6397228269610797629977cba9e91d:python_full_stack/project/FTP/client/core/client_cls.py

    #? 主页
    def homepage(self):
        print(self.recv(1024).decode('utf-8'))
        a = 1
        while a:
            flag = input("1 登录\n2 注册\n>>>")
            self.send(flag.encode('utf-8'))
            if flag == "1":
                self.login(self.request)
                a = 0
            elif flag == "2":
                self.regist(self.request)
                a = 0
            else:
                print("输入错误， 请重新输入")

    #? 注册
    def regist(self):
        #? 接收输入用户名提示
        print(self.recv(1024).decode('utf-8'))
        new_id = input(">>>")
        self.send(new_id.encode('utf-8'))
        #? 注册用户名是否重复
        id_res = self.recv(1024).decode('utf-8')
        print(id_res)
        while id_res == "用户名重复":
            new_id = input("请输入用户名")
            self.send(new_id.encode('utf-8'))
        #? id_res是创建用户名的结果，如果不重复，那么接收输入密码提示
        # print(self.recv(1024).decode('utf-8'))
        new_pwd = input(">>>")
        self.send(new_pwd.encode('utf-8'))
        #? 接收注册结果
        print(self.recv(1024).decode('utf-8'))

    #? 登录
    def login(self):
        #? 接收用户名输入提示
        print(self.recv(1024).decode('utf-8'))
        user_id = input(">>>")
        self.send(user_id.encode('utf-8'))
        #? 接收密码输入提示
        print(self.recv(1024).decode('utf-8'))
        user_pwd = input(">>>")
        self.send(user_pwd.encode('utf-8'))
        #? 接收登陆提示
        print(self.recv(1024).decode('utf-8'))

    #? 命令执行
    def run_cmd(self, command):
        if command == '发送':
            file_oprt.send_file(self)
        elif command == '接收':
            file_oprt.recv_file(self)
        else:
            client_cmd.cmd_res(command, self)
