import socket
import json
import os
import sys

file_path = '/'.join(__file__.split('/')[:-1])
os.chdir(file_path)
os.getcwd()

def get_settings():
    #? 读取配置文件
    setting_json = ""
    with open("../conf/settings.json", "r", encoding="utf-8") as f:
        for line in f.read():
            setting_json += line
    setting_dic = json.loads(setting_json)
    return setting_dic

def client_conn(setting_dic, lisetn=5):
    #? 配置服务器信息
    IP_PORT = (setting_dic["IP"], setting_dic['PORT'])
    client = socket.socket()
    client.connect(IP_PORT)
    return client

def chat(client):
    #? 开始聊天
    flag = 0
    if flag == 0:
        data = client.recv().encode('utf-8')
        print(data)
    data = input('>>>>')
    data = client.recv(1024).encoding("utf-8")
    return data

def working():
    #? 循环聊天
    setting_dic = get_settings()
    client = client_conn(setting_dic)
    while True:
        data,request = chat(server)
        if data == "exit":
            break
        else:
            print(data)
    client.close()
    print('over')


if __name__ == '__main__':
    working()
