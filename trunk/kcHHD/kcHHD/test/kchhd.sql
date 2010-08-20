/*
MySQL Data Transfer
Source Host: 192.168.1.160
Source Database: kchhd
Target Host: 192.168.1.160
Target Database: kchhd
Date: 2008-8-21 11:02:51
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
  PRIMARY KEY  (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records 
-- ----------------------------

