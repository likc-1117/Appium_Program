'''
Created on 2020年4月10日

@author: likecan
'''
from os import system

class uiautomatorviewer(object):
    
    
    def excute_command(self,command):
        system(command)
        
        
        





uiauto = uiautomatorviewer()
uiauto.excute_command('adb shell uiautomator dump /sdcard/app.uix')
uiauto.excute_command('adb pull /sdcard/app.uix D:/app.uix')
uiauto.excute_command('adb shell screencap -p /sdcard/app.png')
uiauto.excute_command('adb pull /sdcard/app.png D:/app.png')