# Creater: ChuanTong.Huang
# Emain:  ChuanTong.Huang@gmail.com
# Version: v0.1
# Date: 2008-08-18 14:23:48


# Database: mogbenchdb
# Table: 'admin'
# 
CREATE DATABASE IF NOT EXISTS mogbenchdb;
use mogbenchdb;

CREATE TABLE IF NOT EXISTS `admin` (
  `aID` mediumint(8) unsigned NOT NULL auto_increment,
  `aLoginID` char(50) NOT NULL UNIQUE,
  `aPsw` char(100) NOT NULL default '',
  `aEmail` char(100) NOT NULL default '',
  PRIMARY KEY  (`aID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1; 

# Database: mogbenchdb
# Table: 'klog'
# 
CREATE TABLE IF NOT EXISTS `klog` (
  `lID` bigint(20) unsigned NOT NULL auto_increment,
  `aloginID` char(100) NOT NULL ,
  `logTime` DATETIME NOT NULL,
  `logEvent` text NOT NULL,
  PRIMARY KEY  (`lID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1; 

# Database: mogbenchdb
# Table: 'mogfs_group'
# 
CREATE TABLE IF NOT EXISTS `mogfs_group` (
  `mID` int(10) unsigned NOT NULL auto_increment,
  `mName` char(100) NOT NULL default '',
  `mdbIP` char(100) NOT NULL default '',
  `mdbName` varchar(100) NOT NULL default '',
  `mdbUser` varchar(100) NOT NULL default '',
  `mdbPsw` varchar(100) NOT NULL default '',
  PRIMARY KEY  (`mID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1; 

# Database: mogbenchdb
# Table: 'trackers'
# 
CREATE TABLE IF NOT EXISTS `trackers` (
  `trackerID` mediumint(10) NOT NULL auto_increment,
  `MogGroupID`int(10) unsigned NOT NULL default 0,
  `trackerIP` char(50) NOT NULL,
  `trackerPort` int(4) NOT NULL default '6001',
  PRIMARY KEY  (`trackerID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1; 

insert into `admin`(aLoginID,aPsw) values('admin','21232f297a57a5a743894a0e4a801fc3');
