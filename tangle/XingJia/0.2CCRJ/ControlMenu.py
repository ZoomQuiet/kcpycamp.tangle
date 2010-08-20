# -*- coding: cp936 -*-
# Filename: ControlMenu.py
from MainMenu import MainMenu
from HelpMenu import HelpMenu
from ModeMenu import ModeMenu
from CRJWORKING import CRJWORKING
from CustomMenu import CustomMenu
NULL = "NULL"
Quit = "Quit"
Help = "Help"
Default = "Default"
Custom = "Custom"
File = "File"
Folder = "Folder"
        
while True:
    szCmdMainMenu = MainMenu()    
    if szCmdMainMenu == Quit:
        break
    if szCmdMainMenu == Help:
        HelpMenu()       
    szTemp = szCmdMainMenu[0:4]
    if szTemp == File:
        szCmdModeMenu = ModeMenu()
        if szCmdModeMenu == Default:
            CRJWORKING(NULL, szCmdCustomMenu)
            continue
        if szCmdModeMenu == Quit:
            break
        if szCmdModeMenu == Custom:
            print "Custom"
            szCmdCustomMenu = CustomMenu()
            CRJWORKING(szCmdCustomMenu ,szCmdCustomMenu)
            continue            
    szTemp = szCmdMainMenu[0:6]
    if szTemp == Folder:
        szCmdModeMenu = ModeMenu()
        if szCmdModeMenu == Default:
            CRJWORKING(NULL, szCmdCustomMenu)
            continue
        if szCmdModeMenu == Quit:
            break
        if szCmdModeMenu == Custom:
            szCmdCustomMenu = CustomMenu()
            CRJWORKING(szCmdCustomMenu ,szCmdCustomMenu)
            continue       
        

# End of ControlMenu.py


        
         
        
         
         
