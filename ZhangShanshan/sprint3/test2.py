# -*- coding: cp936 -*-
import env,VirusInfo,sql
env.ReadCfg('cfg.txt')
dinfo = VirusInfo.GetInfo('sample.txt')
for k, v in dinfo.items():
    #print k,':',v
    pass
s0="""a:4:{s:15:"text_processing";s:1:"0";s:10:"max_length";s:3:"100";s:14:"allowed_values";s:614:"Win9x WinNT 
Win9x
未打GDI+漏洞补丁
未打MS04-028补丁的英文版WinXP SP1
Win9x Win2000 WinXP
Win9x WinNT Win2000 WinXP Win2003 
Win9x Win2000 WinXP Win2003
DOS
DOS Win3.1
Win9x WinNT Win2000 WinXP
WinNT Win2000 WinXP Win2003
Win2000 WinXP
Win32
WinNT Win2000
Win2000 WinXP Win2003
Win9x Win2000
Win9x WinMe WinNT Win2000 Win2003
Win9x WinMe WinNT Win2000 WinXP Win2003
Win9x WinMe WinNT Win2000 WinXP
Win9x WinNT Win2000
Win9x WinMe Win2000 WinXP
Win98
Win9x WinMe
Win9x WinMe Win2000
Win9x WinXP
WinNT Win2000 WinXP
WinNT
Win9x WinNT Win2000 Unix Linux
其它
WinXP Win2003";s:18:"allowed_values_php";s:0:"";}"""
q=sql.AddNodeSql(7000,7000,13,1234568,dinfo,s0)
print q



