/*
MySQL Data Transfer
Source Host: 192.168.1.160
Source Database: kchhd
Target Host: 192.168.1.160
Target Database: kchhd
Date: 2008-9-1 10:20:07
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for intervieweegroup
-- ----------------------------
DROP TABLE IF EXISTS `intervieweegroup`;
CREATE TABLE `intervieweegroup` (
  `ID` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL default '',
  `Description` varchar(255) default '',
  PRIMARY KEY  (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for intervieweegroup_resumeinfo_relation
-- ----------------------------
DROP TABLE IF EXISTS `intervieweegroup_resumeinfo_relation`;
CREATE TABLE `intervieweegroup_resumeinfo_relation` (
  `GroupID` int(11) NOT NULL,
  `ResumeID` int(11) NOT NULL,
  PRIMARY KEY  (`GroupID`,`ResumeID`),
  KEY `ResumeID` (`ResumeID`),
  CONSTRAINT `intervieweegroup_resumeinfo_relation_ibfk_3` FOREIGN KEY (`GroupID`) REFERENCES `intervieweegroup` (`ID`),
  CONSTRAINT `intervieweegroup_resumeinfo_relation_ibfk_4` FOREIGN KEY (`ResumeID`) REFERENCES `resumeinfo` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for interviewer_interviewinfo_relation
-- ----------------------------
DROP TABLE IF EXISTS `interviewer_interviewinfo_relation`;
CREATE TABLE `interviewer_interviewinfo_relation` (
  `InterviewInfoID` int(11) NOT NULL,
  `InterviewerID` int(11) NOT NULL,
  PRIMARY KEY  (`InterviewInfoID`,`InterviewerID`),
  KEY `InterviewerID` (`InterviewerID`),
  CONSTRAINT `interviewer_interviewinfo_relation_ibfk_3` FOREIGN KEY (`InterviewerID`) REFERENCES `user` (`ID`),
  CONSTRAINT `interviewer_interviewinfo_relation_ibfk_4` FOREIGN KEY (`InterviewInfoID`) REFERENCES `interviewinfo` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for interviewinfo
-- ----------------------------
DROP TABLE IF EXISTS `interviewinfo`;
CREATE TABLE `interviewinfo` (
  `ID` int(11) NOT NULL COMMENT '对每一次面试的唯一编号，',
  `TableVerID` int(11) default NULL COMMENT '本次面试所使用的评议表版本号',
  `Result` varchar(255) NOT NULL default '' COMMENT '本次面试结果',
  `Addr` varchar(255) NOT NULL default '' COMMENT '面试地点',
  `Times` int(11) NOT NULL COMMENT '第几次面试',
  `DateTime` varchar(255) NOT NULL default '' COMMENT '面试时间',
  `Dept` varchar(255) NOT NULL default '',
  `IsOvertime` int(11) NOT NULL COMMENT '面试是否结束,没结束为0，结束了为1',
  `IntervieweeID` int(11) default NULL,
  PRIMARY KEY  (`ID`),
  KEY `VerNum` (`TableVerID`),
  KEY `GID` (`Result`),
  KEY `IntervieweeID` (`IntervieweeID`),
  CONSTRAINT `interviewinfo_ibfk_3` FOREIGN KEY (`IntervieweeID`) REFERENCES `user` (`ID`),
  CONSTRAINT `interviewinfo_ibfk_4` FOREIGN KEY (`TableVerID`) REFERENCES `tableversion` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for maintitle
-- ----------------------------
DROP TABLE IF EXISTS `maintitle`;
CREATE TABLE `maintitle` (
  `ID` int(11) NOT NULL,
  `Name` varchar(255) collate utf8_unicode_ci NOT NULL default '',
  PRIMARY KEY  (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for question_interviewinfo_relation
-- ----------------------------
DROP TABLE IF EXISTS `question_interviewinfo_relation`;
CREATE TABLE `question_interviewinfo_relation` (
  `QuestionsID` int(11) NOT NULL,
  `InterviewID` int(11) NOT NULL,
  `Answer` varchar(255) collate utf8_unicode_ci default '',
  PRIMARY KEY  (`QuestionsID`,`InterviewID`),
  KEY `InterviewID` (`InterviewID`),
  KEY `QuestionsID` (`QuestionsID`),
  CONSTRAINT `question_interviewinfo_relation_ibfk_3` FOREIGN KEY (`InterviewID`) REFERENCES `interviewinfo` (`ID`),
  CONSTRAINT `question_interviewinfo_relation_ibfk_4` FOREIGN KEY (`QuestionsID`) REFERENCES `questions` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for questions
-- ----------------------------
DROP TABLE IF EXISTS `questions`;
CREATE TABLE `questions` (
  `ID` int(11) NOT NULL COMMENT '问答的唯一标识',
  `Description` text NOT NULL COMMENT '问题述描',
  PRIMARY KEY  (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for resumeinfo
-- ----------------------------
DROP TABLE IF EXISTS `resumeinfo`;
CREATE TABLE `resumeinfo` (
  `ID` int(11) NOT NULL default '0',
  `CardID` varchar(255) NOT NULL default '' COMMENT '身份证号',
  `Name` varchar(255) NOT NULL default '' COMMENT '姓名',
  `Sex` varchar(255) NOT NULL default '',
  `School` varchar(255) default '' COMMENT '学校',
  `Subject` varchar(255) default '' COMMENT '专业',
  `Grade` varchar(255) default '' COMMENT '年纪',
  `Telephone` varchar(11) default '' COMMENT '系联电话',
  `Native` varchar(255) default '',
  `Addr` varchar(255) default '',
  `AddrPhone` varchar(11) default '' COMMENT '家庭联系电话',
  `Email` varchar(255) default '',
  `QQ` varchar(255) default '',
  `ForeignLanguage` text COMMENT '外语水平（含英语四六级成绩）',
  `Character` text COMMENT '性格特点',
  `Programming` text COMMENT '程序设计相关比赛获奖情况',
  `MathAndPhysics` text COMMENT ' 数学、物理相关比赛获奖情况',
  `Scholarships` text COMMENT '三好生和奖学金获得情况',
  `Project` text COMMENT '项目开发经历(与C/C++，JAVA相关的项目经验，注明每个项目的代码量)',
  `SchoolDuty` text COMMENT '干部任职情况（包括：校、院、班、社团）',
  `MoreInfo` text COMMENT '其他情况（兴趣爱好及其他情况说明）',
  `Advice` text COMMENT '您认为谁的编程能力不错（请在同学中推荐3-5人）',
  `ResumePath` varchar(255) default '' COMMENT '简历存放路径',
  `PhotoPath` varchar(255) default '' COMMENT '照片存放路径',
  `UserID` int(11) default NULL,
  PRIMARY KEY  (`ID`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `resumeinfo_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for subtitle
-- ----------------------------
DROP TABLE IF EXISTS `subtitle`;
CREATE TABLE `subtitle` (
  `ID` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL default '',
  `MainTitleID` int(11) default NULL,
  PRIMARY KEY  (`ID`),
  KEY `MainTitleID` (`MainTitleID`),
  CONSTRAINT `subtitle_ibfk_2` FOREIGN KEY (`MainTitleID`) REFERENCES `maintitle` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for subtitle_tableversion_relation
-- ----------------------------
DROP TABLE IF EXISTS `subtitle_tableversion_relation`;
CREATE TABLE `subtitle_tableversion_relation` (
  `SubTitleID` int(11) NOT NULL,
  `TableVerID` int(11) NOT NULL,
  PRIMARY KEY  (`SubTitleID`,`TableVerID`),
  KEY `TableVerID` (`TableVerID`),
  CONSTRAINT `subtitle_tableversion_relation_ibfk_3` FOREIGN KEY (`SubTitleID`) REFERENCES `subtitle` (`ID`),
  CONSTRAINT `subtitle_tableversion_relation_ibfk_4` FOREIGN KEY (`TableVerID`) REFERENCES `tableversion` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for tableversion
-- ----------------------------
DROP TABLE IF EXISTS `tableversion`;
CREATE TABLE `tableversion` (
  `ID` int(11) NOT NULL,
  `UsedCounts` int(11) default '0',
  `VerNumber` int(11) NOT NULL default '0',
  PRIMARY KEY  (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `ID` int(11) NOT NULL,
  `AccountID` varchar(255) NOT NULL default '',
  `Name` varchar(255) NOT NULL default '',
  `Type` varchar(255) NOT NULL default '',
  `Pwd` varchar(255) NOT NULL default '',
  `Dept` varchar(255) default '',
  `IsEffect` int(11) NOT NULL default '1' COMMENT '标识是否无效，IsEffect?,Int型，0表示无效，1表示有效，非空，默认值为1',
  PRIMARY KEY  (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records 
-- ----------------------------
INSERT INTO `interviewer_interviewinfo_relation` VALUES ('123', '3245');
INSERT INTO `interviewer_interviewinfo_relation` VALUES ('234', '3245');
INSERT INTO `interviewer_interviewinfo_relation` VALUES ('2305', '3245');
INSERT INTO `interviewer_interviewinfo_relation` VALUES ('2521', '3245');
INSERT INTO `interviewer_interviewinfo_relation` VALUES ('3286', '3245');
INSERT INTO `interviewer_interviewinfo_relation` VALUES ('3735', '3245');
INSERT INTO `interviewer_interviewinfo_relation` VALUES ('3802', '3245');
INSERT INTO `interviewer_interviewinfo_relation` VALUES ('5851', '3245');
INSERT INTO `interviewer_interviewinfo_relation` VALUES ('6747', '3245');
INSERT INTO `interviewer_interviewinfo_relation` VALUES ('9670', '3245');
INSERT INTO `interviewinfo` VALUES ('123', '1', 'fail', 'F8_801', '1', '2008-08-15 10:49:25', 'wps', '1', '5432');
INSERT INTO `interviewinfo` VALUES ('234', '1', 'fail', 'F7_707', '1', '2008-09-02 10:50:26', 'wps', '1', '5432');
INSERT INTO `interviewinfo` VALUES ('1886', null, '', 'asdf', '0', 'adfasd', 'WPS', '0', '6328');
INSERT INTO `interviewinfo` VALUES ('2305', null, '', 'place111', '0', 'time111', 'WPS', '1', '584');
INSERT INTO `interviewinfo` VALUES ('2346', null, '', 'F8-801', '0', '2008-8-25 12:30', 'WPS', '1', '54');
INSERT INTO `interviewinfo` VALUES ('2521', null, '', 'place111', '0', '12:30 8.30', 'WPS', '0', '1236');
INSERT INTO `interviewinfo` VALUES ('3286', null, '', 'addr', '0', 'time', 'WPS', '1', '54');
INSERT INTO `interviewinfo` VALUES ('3735', null, '', 'F8', '0', '2008', 'WPS', '1', '584');
INSERT INTO `interviewinfo` VALUES ('3802', null, 'fail', 'F8-801', '0', '2008-8-25 12:30', 'WPS', '1', '5432');
INSERT INTO `interviewinfo` VALUES ('4751', null, '', 'asdf', '0', 'asd', 'WPS', '1', '584');
INSERT INTO `interviewinfo` VALUES ('5851', null, '', '601', '0', '2008-9-1 12:00', 'WPS', '0', '1624');
INSERT INTO `interviewinfo` VALUES ('6747', null, 'pass', 'F9', '0', '2008', 'WPS', '1', '9832');
INSERT INTO `interviewinfo` VALUES ('9670', null, '', '4234', '0', '23423', 'WPS', '0', '1537');
INSERT INTO `maintitle` VALUES ('1350', '自我评价');
INSERT INTO `maintitle` VALUES ('1820', '1');
INSERT INTO `maintitle` VALUES ('1830', '主菜单');
INSERT INTO `maintitle` VALUES ('2399', '2');
INSERT INTO `maintitle` VALUES ('2853', '1\r\n');
INSERT INTO `maintitle` VALUES ('4109', 'may');
INSERT INTO `maintitle` VALUES ('4134', '编程能力');
INSERT INTO `maintitle` VALUES ('5627', '分析设计能力');
INSERT INTO `maintitle` VALUES ('7005', '23412341234');
INSERT INTO `maintitle` VALUES ('8129', '补充项');
INSERT INTO `maintitle` VALUES ('8380', '加分项目');
INSERT INTO `maintitle` VALUES ('9131', 'kakaka');
INSERT INTO `maintitle` VALUES ('9750', 'A');
INSERT INTO `maintitle` VALUES ('9774', '综合素质');
INSERT INTO `maintitle` VALUES ('9865', 'abc');
INSERT INTO `question_interviewinfo_relation` VALUES ('1', '5851', '11111111');
INSERT INTO `questions` VALUES ('1', '平常喜欢用什么编程?');
INSERT INTO `questions` VALUES ('2', '为什么会喜欢这种语言');
INSERT INTO `resumeinfo` VALUES ('142', '123456', 'sara', '0', '北师大', '软件工程', '04', '137*****', '', '海湾', '0756——***', 'dizhisha@163.com', '109678616', '123你好', '开朗', '厄……nadfioah ', '厄……', '', '', '班长，学习部部长', '', '你好', 'F:\\Karrigell-2.4.0\\webapps\\kchhd\\web\\uploadFiles\\1.jpg', ' ', '5432');
INSERT INTO `resumeinfo` VALUES ('3229', 'fasd', 'fasd', '0', 'dfas', 'asd', 'fas', 'f', 'fas', 'dfas', 'df', 'dfa', 'df', ' ', 'dfd', '', '', '', '', '', '', '', ' ', ' ', '54');
INSERT INTO `resumeinfo` VALUES ('3725', '123456789', '训练营', '0', '金山软件', '计算机科学与技术', '2008', '0756-888888', '广东珠海', '广东珠海', '0756-888888', 'kingsodt@kingsoft', '88888888', '8', '用心快乐', '广东省程序设计一等奖', '数学第一', '国家励志奖学金', 'WPS', '主席', '足球', '求总', '', '', '5572');
INSERT INTO `resumeinfo` VALUES ('4308', ' ', '123', ' ', '', '', '', '', '', '', '', '', '', null, null, null, null, null, null, null, null, null, 'F:\\Karrigell-2.4.0\\webapps\\kchhd\\web\\uploadFiles\\DB表名 Class名 .txt', '', '3628');
INSERT INTO `resumeinfo` VALUES ('5021', 'asdfasdf', 'fasd', '0', 'fasdf', '', '', '', '', '', '', 'asdfasd', '', '', '', 'ffasdfasf', '', '', '', '', '', '', '', '', '7044');
INSERT INTO `resumeinfo` VALUES ('5294', '', 'nigg ', '0', 'njhnklh', '', '', '', '', '', '', '', '', '', '', 'jh jh', '', '', '', '', '', '', '', '', '9832');
INSERT INTO `resumeinfo` VALUES ('6226', '你好', '你好', '0', '你好', '', '你好', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1236');
INSERT INTO `resumeinfo` VALUES ('6922', '', 'test', '0', 'test', 'test', 'test', 'test', 'test', ' ', ' ', ' ', ' ', ' ', ' ', '', '', '', '', '', '', '', ' ', ' ', '1233');
INSERT INTO `resumeinfo` VALUES ('7076', '4444444454544544545', '龙', '0', '**大学', 'X专业', '4', '13911111111', 'gg', 'addr', '3229390', '556655', '1293021', '4', 'kailang', '程序设计11', '数学，物理', '三好学生', '项目经验', '干部任职情况', '其他兴趣', '推荐的人', '', '', '1624');
INSERT INTO `resumeinfo` VALUES ('7585', 'qrq', 'ewrq', '0', 'qwere', '', '', 'wrwe', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'F:\\Karrigell-2.4.0\\webapps\\kchhd\\control\\uploadFiles\\DB表名 Class名 .txt', '', '8453');
INSERT INTO `subtitle` VALUES ('2311', '计算机原理', '4134');
INSERT INTO `subtitle` VALUES ('2456', '文档', '8380');
INSERT INTO `subtitle` VALUES ('2775', '开发工具开发环境', '4134');
INSERT INTO `subtitle` VALUES ('2846', '职业认识', '9774');
INSERT INTO `subtitle` VALUES ('2924', '调试程序能力', '4134');
INSERT INTO `subtitle` VALUES ('2940', '性格特点', '9774');
INSERT INTO `subtitle` VALUES ('3079', '专业加分', '8380');
INSERT INTO `subtitle` VALUES ('3741', '沟通表达', '9774');
INSERT INTO `subtitle` VALUES ('3937', '编程语言', '4134');
INSERT INTO `subtitle` VALUES ('3969', '数据结构与算法', '4134');
INSERT INTO `subtitle` VALUES ('4614', '形象外表', '9774');
INSERT INTO `subtitle` VALUES ('4940', '建模能力', '5627');
INSERT INTO `subtitle` VALUES ('5614', '公司认识', '9774');
INSERT INTO `subtitle` VALUES ('6160', '压力', '8129');
INSERT INTO `subtitle` VALUES ('6848', '学习能力', '9774');
INSERT INTO `subtitle` VALUES ('7046', '自我认知', '9774');
INSERT INTO `subtitle` VALUES ('8186', '代码构架能力', '5627');
INSERT INTO `subtitle` VALUES ('9727', '计划能力', '9774');
INSERT INTO `subtitle` VALUES ('9812', '技术性', '8129');
INSERT INTO `subtitle` VALUES ('9837', '社交能力', '9774');
INSERT INTO `tableversion` VALUES ('1', '12', '21');
INSERT INTO `user` VALUES ('1', '1', '1', 'admin', '111', null, '1');
INSERT INTO `user` VALUES ('54', 'rfweatf', '刘翔345', 'interviewee', '1234', 'wps', '0');
INSERT INTO `user` VALUES ('123', 'abc', 'abc', 'abc', 'abc', 'abc', '0');
INSERT INTO `user` VALUES ('584', 'shanshan', 'sara', 'interviewee', '123', 'WPS', '1');
INSERT INTO `user` VALUES ('1192', '333333-', '333', 'assistant', '33', null, '0');
INSERT INTO `user` VALUES ('1233', 'test', 'f', 'interviewee', '123', null, '0');
INSERT INTO `user` VALUES ('1236', 'huangjian11', '1231444gg', 'interviewee', '1', 'wps', '1');
INSERT INTO `user` VALUES ('1338', 'rr', '1', 'interviewee', '1', null, '1');
INSERT INTO `user` VALUES ('1537', '657657567575', '555', 'interviewee', '555', 'wps', '1');
INSERT INTO `user` VALUES ('1624', 'long', 'long', 'interviewee', '11', 'wps', '1');
INSERT INTO `user` VALUES ('1655', '8888888', '88', 'interviewee', '88', null, '0');
INSERT INTO `user` VALUES ('1722', '4564646', '4', 'interviewee', '4', null, '0');
INSERT INTO `user` VALUES ('1939', 'lbibibibbibii', '111444', 'assistant', '16', null, '0');
INSERT INTO `user` VALUES ('1972', 'tt', 't', 'interviewer', '1', null, '1');
INSERT INTO `user` VALUES ('1991', 'yyy', '姗姗', 'assistant', '123', null, '1');
INSERT INTO `user` VALUES ('2617', 'oooooooo', 'ooo3333333555sss', 'assistant', 'ooo', null, '0');
INSERT INTO `user` VALUES ('3245', 'hello', '6781111', 'interviewer', '1', 'WPS', '1');
INSERT INTO `user` VALUES ('3391', '1111', '', 'interviewer', '1', '过程改进', '1');
INSERT INTO `user` VALUES ('3409', 'lbibibibbibii33', '11133', 'interviewer', 's', null, '1');
INSERT INTO `user` VALUES ('3628', '123', '123', 'interviewee', '123', null, '1');
INSERT INTO `user` VALUES ('3740', 'huangjian11111', '12312222222555', 'interviewer', '12212', null, '0');
INSERT INTO `user` VALUES ('4293', '7', 'interviewee', 'mmmm', 'mmmmmmmmmmmmmm', null, '1');
INSERT INTO `user` VALUES ('4384', 'asdf', '', 'interviewer', 'a', 'sasdf', '0');
INSERT INTO `user` VALUES ('4540', 'kitty', 'cat', 'interviewee', '123', '毒霸', '0');
INSERT INTO `user` VALUES ('4548', 'eeee', 'ee', 'interviewee', '1', null, '1');
INSERT INTO `user` VALUES ('5032', 'huangjian', '1', 'admin', '1', 'WPS', '1');
INSERT INTO `user` VALUES ('5415', 'mianshiguan', '', 'interviewer', '123', 'wps', '0');
INSERT INTO `user` VALUES ('5432', 'sara', 'shanshan666', 'interviewee', '1234', 'WPS', '1');
INSERT INTO `user` VALUES ('5572', 'xunlianying', '训练营', 'interviewee', '8888', null, '1');
INSERT INTO `user` VALUES ('5606', 'longlong', '11111', 'interviewee', '1', null, '1');
INSERT INTO `user` VALUES ('5755', 'dizhishaya', '1', 'interviewee', '1', null, '0');
INSERT INTO `user` VALUES ('5759', 'aa', 'a', 'assistant', 'a', null, '1');
INSERT INTO `user` VALUES ('5898', '2', 'tanjl03', 'interviewee', '2', null, '1');
INSERT INTO `user` VALUES ('5925', '0000000000000', '0', 'interviewee', '0', null, '0');
INSERT INTO `user` VALUES ('6328', '11111', '22222', 'interviewee', '123', 'wps', '0');
INSERT INTO `user` VALUES ('6819', '111111', '1333', 'interviewee', '1', null, '0');
INSERT INTO `user` VALUES ('6945', 'may', 'may', 'assistant', '123', null, '0');
INSERT INTO `user` VALUES ('7044', 'hhh', 'hhh', 'interviewee', '123', null, '1');
INSERT INTO `user` VALUES ('7208', '000000000000044', '444', 'interviewee', '4', null, '0');
INSERT INTO `user` VALUES ('7441', 'aa', 'asd', 'interviewee', '1', null, '1');
INSERT INTO `user` VALUES ('7767', '13213131313', '1eeeee', 'interviewee', '1', null, '0');
INSERT INTO `user` VALUES ('7846', '22322', '22', 'interviewee', '1', '1', '1');
INSERT INTO `user` VALUES ('8088', '面试官', '', 'interviewer', '123', '毒霸', '1');
INSERT INTO `user` VALUES ('8118', 'rrr', '1', 'interviewer', '1', null, '1');
INSERT INTO `user` VALUES ('8453', 'all', '1', 'interviewee', '1', null, '1');
INSERT INTO `user` VALUES ('8636', '888888888888888', '88', 'interviewee', '888', null, '0');
INSERT INTO `user` VALUES ('9009', '4234', '342', 'interviewee', '432', null, '0');
INSERT INTO `user` VALUES ('9064', '111', '11', 'interviewee', 's', null, '0');
INSERT INTO `user` VALUES ('9234', '3', 'asfsdf', 'interviewer', '3', null, '1');
INSERT INTO `user` VALUES ('9367', '666666666666666', '66', 'interviewee', '66', null, '0');
INSERT INTO `user` VALUES ('9411', '4', 'assistant', 'assistant', '4', null, '1');
INSERT INTO `user` VALUES ('9832', 'huangxx', 'huna', 'interviewee', '123', 'wps', '1');
