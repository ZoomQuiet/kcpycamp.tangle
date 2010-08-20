sample.txt 病毒分析样本
config.txt 字段名配置,冒号:左边为病毒分析样本可能出现的关键字,右边为数据库表           中的字段名,字段名不分先后顺序
hello.py 未分离模块, 把sample.txt中的信息插入到virus表中
         实现(1)从sample.txt中分离字段名和值并存入字典,用到两个函数	                HasKey(s,dk),Token(s,dk)
	     (2)拼接sql串
             (3)连接数据库并查询


		 


