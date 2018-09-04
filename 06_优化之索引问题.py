查询调试：
    执行查询语句 db.t1.find({name:'张无忌'}).explain(executionStats)
    建立索引：db.t1.ensureIndex({name:1})        （1是升序，-1是降序）
    再次查询寻：db.t1.find({name:'张无忌'}).explain(executionStats)