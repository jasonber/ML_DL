def regist(request):
    #? 接收输入用户名提示
    print(request.recv(1024).decode('utf-8'))
    new_id = input(">>>")
    request.send(new_id.encode('utf-8'))
    #? 注册用户名是否重复
    id_res = request.recv(1024).decode('utf-8')
    print(id_res)
    while id_res == "用户名重复":
        new_id = input("请输入用户名")
        request.send(new_id.encode('utf-8'))
    #? id_res是创建用户名的结果，如果不重复，那么接收输入密码提示
    # print(request.recv(1024).decode('utf-8'))
    new_pwd = input(">>>")
    request.send(new_pwd.encode('utf-8'))
    #? 接收注册结果
    print(request.recv(1024).decode('utf-8'))