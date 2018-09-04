ubuntu18.04 安装mongodb并使用Robo 3T连接Mongodb数据库
From：https://www.cnblogs.com/soaeon/p/9068756.html
MongoDB 官网：https://www.mongodb.com
MongoDB 官网安装教程：https://docs.mongodb.com/tutorials/install-mongodb-on-ubuntu/
MongoDB 教程：http://www.runoob.com/mongodb/mongodb-tutorial.html

1. 前提：
系统：ubuntu18.04  64位 
数据库:mongodb
GUI:Robo 3T  2018.3.0
描述： mongodb 安装在局域网内的ubuntu的机子上面，  在win 下面使用Robo 3T 
链接Mongodb 数据库

2. 安装mongodb 数据库

    导入公钥
    Ubuntu软件包管理器apt（高级软件包工具）需要软件分销商的GPG密钥来确保软件包的一致性和真实性。 运行此命令将MongoDB密钥导入到您的服务器

    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5   

    修改源文件列表
    使用以下命令在/etc/apt/sources.list.d/中添加一个MongoDB源：

    echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

    更新源 
    sudo apt-get  update

    安装Mongodb
    sudo apt-get install -y mongodb-org

    启动MongoDB并将其添加为在启动时启动的服务：

    systemctl start mongod
    systemctl enable mongod

    进入mongodb 
    mongo

    至此  mongodb 已安装完毕， 下面我们来用Robo 3t  链接一下 mongodb 


3. 添加管理员
    第一步： 我们先修改配置文件，允许远程登陆

    找到 /etc/mongod.conf 文件，  如果这个文件没有编辑的权限  请先修改权限（sudo chmod 777  /etc/mongod.conf） 
    将 bindIp:  127.0.0.1  修改为：bindIp:  0.0.0.0 
    重启一下mongodb:
    sudo service mongod restart

    ======================================================

管理mongod
    >> mongod  服务器
    >> mongo   客户端

    配置文件在/etc/mongod.conf
    默认端口27017

启动
    sudo service mongod start
停止
    sudo service mongod stop

使用终端连接
    这个shell就是mongodb的客户端，同时也是一个js的编译器
    >> mongo

命令
    db查看当前数据库名称
    db.stats()查看当前数据库信息

终端退出连接
    exit
    或ctrl+c

===============================================================
数据库切换
查看当前数据库名称
    db

查看所有数据库名称
列出所有在物理上存在的数据库
    show dbs
    ex:
    show dbs
    admin   0.000GB
    config  0.000GB
    local   0.000GB

切换数据库
    如果数据库不存在，则指向数据库，但不创建，直到插入数据或创建集合时数据库才被创建
    use 数据库名称           mongo不存在创建数据库的命令，直接使用即可
    默认的数据库为test，如果你没有创建新的数据库，集合将存放在test数据库中

数据库删除
    删除当前指向的数据库
    如果数据库不存在，则什么也不做
    db.dropDatabase()

    =====================================================================

集合（可以理解成mysql中的表）的创建：
    语法
    db.createCollection(name, options)

    name是要创建的集合的名称
    options是一个文档，用于指定集合的配置
    选项​​参数是可选的，所以只需要到指定的集合名称。以下是可以使用的选项列表：
    例1：不限制集合大小
    db.createCollection("stu")
    例2：限制集合大小，后面学会插入语句后可以查看效果
    参数capped：默认值为false表示不设置上限，值为true表示设置上限
    参数size：当capped值为true时，需要指定此参数，表示上限大小，当文档达到上限时，会将之前的数据覆盖，单位为字节
    db.createCollection("sub", { capped : true, size : 10 } )

查看当前数据库的集合：
语法
    show collections

删除：
语法
    db.集合名称.drop()

=====================================================================
数据类型
    Object ID：文档ID
    String：字符串，最常用，必须是有效的UTF-8
    Boolean：存储一个布尔值，true或false
    Integer：整数可以是32位或64位，这取决于服务器
    Double：存储浮点值
    Arrays：数组或列表，多个值存储到一个键
    Object：用于嵌入式的文档，即一个值为一个文档
    Null：存储Null值
    Timestamp：时间戳
    Date：存储当前日期或时间的UNIX时间格式

object id
    每个文档都有一个属性，为_id，保证每个文档的唯一性
    可以自己去设置_id插入文档
    如果没有提供，那么MongoDB为每个文档提供了一个独特的_id，类型为objectID
    objectID是一个12字节的十六进制数
    前4个字节为当前时间戳
    接下来3个字节的机器ID
    接下来的2个字节中MongoDB的服务进程id
    最后3个字节是简单的增量值(理论上永远不会重复)

插入
语法（document可以理解为MySQL的一行数据）
    db.集合名称.insert(document)

查询集合所有数据
语法
    db.集合名称.find()

更新：
语法
    db.集合名称.update(
    <query>,
    <update>,
    {multi: <boolean>}
    )

    参数query:查询条件，类似sql语句update中where部分
    参数update:更新操作符，类似sql语句update中set部分
    参数multi:可选，默认是false，表示只更新找到的第一条记录，值为true表示把满足条件的
    文档全部更新
    例3：全文档更新
    db.stu.update({name:'hr'},{name:'mnc'})

    例4：指定属性更新，通过操作符$set
    db.stu.insert({name:'hr',gender:0})
    db.stu.update({name:'hr'},{$set:{name:'hys'}})
    例5：修改多条匹配到的数据
    db.stu.update({},{$set:{gender:0}},{multi:true})

保存：
语法
    db.集合名称.save(document)
    如果文档的_id已经存在则修改，如果文档的_id不存在则添加
例6
    db.stu.save({_id:'20160102','name':'yk',gender:1})
例7
    db.stu.save({_id:'20160102','name':'wyk'})

删除：
语法
    db.集合名称.remove(
    <query>,
    {
        justOne: <boolean>
    }
    )

    参数query:可选，删除的文档的条件
    参数justOne:可选，如果设为true或1，则只删除一条，默认false，表示删除多条
    例8：只删除匹配到的第一条

    db.stu.remove({gender:0},{justOne:true})
    列9：删除所有
    db.stu.remove({},{})















