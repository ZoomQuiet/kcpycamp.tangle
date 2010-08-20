# Creater: ChuanTong.Huang
# Emain:  ChuanTong.Huang@gmail.com
# Version: v0.6
# Saved: 2008-08-26 20:29:50
# 

CREATE DATABASE IF NOT EXISTS mogbenchdb;
use mogbenchdb;

# Database: mogbenchdb
# Table: 'admin'
CREATE TABLE IF NOT EXISTS `admin` (
  `aID` mediumint(8) unsigned NOT NULL auto_increment,
  `aLoginID` char(50) NOT NULL,
  `aPsw` char(100) NOT NULL default '',
  `aEmail` char(100) NOT NULL default '',
  PRIMARY KEY  (`aID`),
  UNIQUE KEY `aLoginID` (`aLoginID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1; 


# Database: mogbenchdb
# Table: 'config'
CREATE TABLE IF NOT EXISTS `config` (
  `aid` int(10) unsigned NOT NULL auto_increment,
  `flushTime` int(11) NOT NULL default '0',
  PRIMARY KEY  (`aid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1; 


# Database: mogbenchdb
# Table: 'device_status'
CREATE TABLE IF NOT EXISTS `device_status` (
  `mogid` mediumint(9) NOT NULL default '0',
  `hostid` mediumint(9) NOT NULL default '0',
  `devid` bigint(20) NOT NULL default '0',
  `status` char(20) NOT NULL default '',
  PRIMARY KEY  (`mogid`,`devid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1; 


# Database: mogbenchdb
# Table: 'django_content_type'
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1; 


# Database: mogbenchdb
# Table: 'django_session'
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1; 


# Database: mogbenchdb
# Table: 'django_site'
CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL auto_increment,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1; 


# Database: mogbenchdb
# Table: 'host_status'
CREATE TABLE IF NOT EXISTS `host_status` (
  `mogid` mediumint(9) NOT NULL default '0',
  `hostid` mediumint(9) NOT NULL default '0',
  `status` char(20) NOT NULL default '',
  PRIMARY KEY  (`hostid`,`mogid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1; 


# Database: mogbenchdb
# Table: 'klog'
CREATE TABLE IF NOT EXISTS `klog` (
  `lID` bigint(20) unsigned NOT NULL auto_increment,
  `aloginID` char(100) NOT NULL,
  `logTime` datetime NOT NULL,
  `logEvent` text NOT NULL,
  PRIMARY KEY  (`lID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1; 


# Database: mogbenchdb
# Table: 'mogfs_group' 
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
CREATE TABLE IF NOT EXISTS `trackers` (
  `trackerID` mediumint(10) NOT NULL auto_increment,
  `MogGroupID` int(10) unsigned NOT NULL default '0',
  `trackerIP` char(50) NOT NULL,
  `trackerPort` int(4) NOT NULL default '6001',
  `status` char(20) NOT NULL default 'alive',
  PRIMARY KEY  (`trackerID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1; 

INSERT INTO `admin`(aLoginID,aPsw) values('admin','21232f297a57a5a743894a0e4a801fc3');
INSERT INTO config (flushTime) VALUES(60);

