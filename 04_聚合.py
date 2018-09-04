聚合(aggregate)主要用于计算数据，类似sql中的sum()、avg()
db.集合名称.aggregate([{管道:{表达式}}])
在mongodb中，管道具有同样的作用，文档处理完毕后，通过管道进行下一次处理
常用管道
    $group：将集合中的文档分组，可用于统计结果
    $match：过滤数据，只输出符合条件的文档
    $project：修改输入文档的结构，如重命名、增加、删除字段、创建计算结果
    $sort：将输入文档排序后输出
    $limit：限制聚合管道返回的文档数
    $skip：跳过指定数量的文档，并返回余下的文档
    $unwind：将数组类型的字段进行拆分

常用表达式
    $sum：计算总和，$sum:1同count表示计数
    $avg：计算平均值
    $min：获取最小值
    $max：获取最大值
    $push：在结果文档中插入值到一个数组中
    $first：根据资源文档的排序获取第一个文档数据
    $last：根据资源文档的排序获取最后一个文档数据

1.$group
将集合中的文档分组，可用于统计结果
_id表示分组的依据，使用某个字段的格式为'$字段'
例1：统计男生、女生的总人数
    db.class.aggregate([{$group:{
        _id:'$gender',
        数量:{$sum:1}
        }
        }])

例2：求学生总人数、平均年龄(提示：设置_id=null就可以选中所有)
    db.class.aggregate([{$group:{
        _id : null,
        '人数':{$sum:1},
        '平均天数':{$avg:'$day'}
    }}])

例3：统计学生性别及学生姓名 所谓都是就是把统计的数据用一个数组存起来
    db.class.aggregate([{$group:{
        _id:'$gender',
        name:{$push:'$title'}
    }}])

使用$$ROOT可以将文档内容加入到结果集的数组中
    db.class.aggregate([{$group:{
        _id:'$gender',
        name:{$push:'$$ROOT'}
    }}])

$match：过滤数据，只输出符合条件的文档
例1：查询day大于10的学生
    db.class.aggregate([{$match:{
        day:{$gte:10}
        }
    }])

例2：查询课时大约10  的男生、女生人数
db.class.aggregate([{$match:{day:{$gt:10}}},
{$group:{
    _id:'$gender',
    人数:{$sum:1}
}}])

$project：修改输入文档的结构，如重命名、增加、删除字段、创建计算结果
例1：查询title day gender
    db.class.aggregate([{$project:{_id:0,title:1,day:1,gender:1}}])

例2：2$group查询男生女生人数，3$project输出总人数
    db.class.aggregate([{$group:{
        _id:'$gender',
        人数:{$sum:1}
    }},
    {$project:{
        _id:0,
        人数:1
    }}])

$sort
例1：查询学生信息，按day升序
    db.class.aggregate([{$sort:{day:1}}])

例2：查询男女人数，按人数降序排列
    db.class.aggregate([{$group:
    {
        _id:"$gender",
        人数:{$sum:1}
    }},{$sort:{人数:-1}}])

$limit：限制聚合管道返回的文档数
例1：查询3条学生的信息
    db.class.aggregate([{$limit:3}])

$skip：跳过指定数量的文档，并返回余下的文档

例2：查询从第3条开始的学生信息
    db.class.aggregate([{$skip:2}])

例3：统计男生、女生人数，按人数升序，取第二条数据
    db.class.aggregate([{$group:{
        _id:'$gender',
        人数:{$sum:1}
    }},{$sort:{人数:1}},{$skip:1},{$limit:1}])

    注意顺序：先写skip，再写limit

$unwind 将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值
    db.集合名称.aggregate([{$unwind:'$字段名称'}])
    db.t2.insert({_id:1,item:'t-shirt',size:['S','M','L']})
    db.t2.aggregate([{$unwind:'$size'}])
    # 会丢失数据
    防止数据丢失
    db.t2.aggregate([{$unwind:{
    path:'$size',
    preserveNullAndEmptyArrays:true
    } 
    }])

