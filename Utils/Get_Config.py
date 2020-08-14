'''
Created on 2019年10月16日

@author: likecan
'''
#coding=utf-8
import configparser
class get_config(object):



    def __init__(self, config_path=None):
        if config_path == None:
            self.cofig_addr = '..\\Config\\LocalElement.ini'
        else:
            self.config_addr = config_path
        self.get_config = configparser.ConfigParser()
        self.get_config.read(self.config_addr, encoding='utf-8')#从给定的配置文件中读取内容，并形成对象
    
    def get_config_by_key(self,key_name):
        for ini_sections in self.get_config.sections():#获取指定配置文件下的所有根节点的名称并返回名称列表（即所有用中括号括起来的内容并形成列表）
            if self.get_config.has_option(ini_sections, key_name):#判断指定关键字在不在某一个根节点中
                return self.get_config.get(ini_sections, key_name)#返回关键字对应的元素信息
        return None
    
    
    def get_config_by_section_key(self,key_name,key_section = 'app'):
        if self.get_config.has_option(key_section, key_name):
            get_config_result = self.get_config.get(key_section, key_name)
            return get_config_result.split('#')
        return None
    
    
    def set_config(self,key_section,key_option,key_value):
        self.get_config.set(key_section, key_option, key_value)


    

    