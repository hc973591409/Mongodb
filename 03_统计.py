方法count()用于统计结果集中文档条数
db.集合名称.find({条件}).count() 
或者
db.集合名称.count({条件})
查询课时大约10的的课程
    db.class.count({$where:function(){
        return this.day > 10
        }})

统计 j开头的个数
    db.class.count({$where:function(){
        return this.title.indexOf('j')==0
        }})


消除重复：
    方法distinct()对数据进行去重
    语法
    db.集合名称.distinct('去重字段',{条件})

新增属性，当day是偶数的是，让gender=0
db.class.update({$where:function(){
    return this.day%2==0
    }},{$set:{gender:0}},{multi:true})


查找课时大约10的，基于gender去重
