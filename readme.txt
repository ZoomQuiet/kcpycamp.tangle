= 蟒营仓库使用规约 =
 属主:yusulian 
 历史:
    080818 ZoomQuiet apeended svn.ignore 说明
    080728 ZoomQuiet fixed apeended doc. ctrl. elements
    080728 YSL creat

== 根目录分配 ==
仓库根/
  +- release   产品发布出口
  +- branches  分支产品入口
  +- tasks     任务分支入口
  +- tangle    个人开发入口
  `- trunk     产品主线

== 目录使用策略 ==
0. tangle   中开辟各人私用目录，进行探索开发
1. tasks    中组织主要产品之外的任务型开发代码
2. trunk    主线开发,根据不同项目分目录进行
    + 自由读写
    + 作为日常开发环境,随时加入新功能
    + 对应 http://kcpy.rdev.kingsoft.net/beta 发布
3. release  发布版本,根据不同项目的不同发布版本命名目录进行;
    + 只读,仅仅能由项目经理检入
    + 作为产品版本的陈列馆,和发布管理的自动化部署使用
    + 对应 http://kcpy.rdev.kingsoft.net/item 发布
4. branches 分支维护,根据不同项目的不同大版本组织目录进行;
    + 自由读写
    + 作为产品版本的测试发布环境
    + 对应 http://kcpy.rdev.kingsoft.net/demo 发布
== 忽略说明 ==
/svn.ignore 文件是仓库禁止检入文件后缀列表，凡是无法检入时，注意对比一下...
