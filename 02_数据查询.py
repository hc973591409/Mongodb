基本查询：
方法find()：查询
    db.集合名称.find({条件文档})
方法findOne()：查询，只返回第一个
    db.集合名称.findOne({条件文档})

方法pretty()：将结果格式化，就shell中显示好看点，没啥用
    db.集合名称.find({条件文档}).pretty()

比较运算符：
    等于，默认是等于判断，没有运算符
    小于$lt
    小于或等于$lte
    大于$gt
    大于或等于$gte
    不等于$ne
    例1：查询名称等于课程为java
    # 字段可以不用"""约束
    db.class.find({title:"jave"})
    例2：查询课时大于10的
    db.class.find({day:{$gt:10}})

逻辑运算符：
    逻辑与：默认是逻辑与的关系 ,逗号连接就可以
    例3：查询课时大于10 且 title==C++
    db.class.find({day:{$gte:10},title:'C++'})
    逻辑或：使用$or
    例4：查询课时小于10 获取 title=Python
    db.class.find({$or:[{day:{$lte:10}},{title:'Python'}]})

    逻辑与或都用：
    例五：查询day<10，或 title==C++ 且 day>10
    db.class.find({$or:[{title:'html5'},{day:{$gte:10}}],day:{$lte:10}})

    范围运算符：
    使用"$in"，"$nin" 判断是否在某个范围内
    例6：查询课时为2，4
    db.class.find({day:{$in:[2,4]}})

    正则表达式：
    查询ja开头的课程
    db.class.find({title:/^ja/})

    自定义查询：
    使用$where后面写一个函数，返回满足条件的数据
    例7：查询title的学生
    db.class.find({$where:function(){
    return this.day>10
    }})

Limit:
    用于读取指定数量的文档
    语法：
    db.集合名称.find().limit(NUMBER)

    参数NUMBER表示要获取文档的条数
    如果没有指定参数则显示集合中的所有文档

    例1：查询3条学生信息
    db.stu.find().limit(3)

    skip
    方法skip()：用于跳过指定数量的文档
    语法：
    db.集合名称.find().skip(NUMBER)
    例2：查询从第3条开始的学生信息
    db.class.find().skip(2)

skip和limit配合使用
    查询第5至8条数据
    db.class.find().skip(4).limit(3)

投影：
在查询到的返回结果中，只选择必要的字段，而不是选择一个文档的整个字段
如：一个文档有5个字段，需要显示只有3个，投影其中3个字段即可
    语法：
    参数为字段与值，值为1表示显示，值为0不显示
    db.集合名称.find({},{字段名称:1,...})

    只显示课程名：
    db.class.find({},{title:1,_id:0})

排序：
    db.集合名称.find().sort({字段:1,...})
    参数1为升序排列
    参数-1为降序排列

    按照课时升序排列
    db.class.find({}).sort({day:1})

    按照课时降序排列
    db.class.find({}).sort({day:-1})










