超级管理员：
为了更安全的访问mongodb，需要访问者提供用户名和密码，于是需要在mongodb中创建用户
采用了角色-用户-数据库的安全管理方式
常用系统角色如下：
    root：只在admin数据库中可用，超级账号，超级权限
    Read：允许用户读取指定数据库
    readWrite：允许用户读写指定数据库
创建超级管理用户
    use admin
    db.createUser({
        user:'admin',
        pwd:'admin',
        roles:[{role:'root',db:'admin'}]
    })

修改配置文件
    sudo vi /etc/mongod.conf
启用身份验证
注意：keys and values之间一定要加空格, 否则解析会报错
    security:
    authorization: enabled
重启服务
    sudo service mongod stop
    sudo service mongod start
终端连接
    mongo -u 'admin' -p '123' --authenticationDatabase 'admin'

普通用户管理：
使用超级管理员登录，然后进入用户管理操作
查看当前数据库的用户
    use test1
    show users

创建普通用户
    db.createUser({user:'python3',pwd:'123',roles:[{role:'readWrite',db:'py3'}]})
终端连接
    mongo -u python3 -p 123 --authenticationDatabase py3

切换数据库，执行命令查看效果
修改用户：可以修改pwd、roles属性
    db.updateUser('t1',{pwd:'456'})