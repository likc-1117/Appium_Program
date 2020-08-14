'''
Created on 2019年11月15日

@author: likecan
'''
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Appium_PO_Model.Utils.Get_Config import get_config
from Appium_PO_Model.Utils.Key_Code import key_code
class get_element_config(object):
    '''
    classdocs
    '''


    def __init__(self):
#         self.driver = base_driver().get_driver()
        self.get_element_config = get_config()
        
        
    def get_local_by_element(self,element,driver=None):
        '''
        从指定元素配置文件中获取指定节点下的元素信息，并返回元素对象
        '''
        #get_page_ini = get_config('..\\Config\\LocalElement.ini')
        element_vlue = self.get_element_config.get_config_by_section_key(element)
        element_value_type = element_vlue.split('#')[0]
        element = element_vlue.split('#')[1].replace('!',':')#使用configparser读取配置文件时，由于在配置文件中默认了冒号与等号功能相同，因此需要将配置文件中的元素信息中的冒号改成感叹号，此处再更改回来
        try:
            if element_vlue:
                if element_value_type == 'id':
                    return driver.find_element_by_id(element)
                elif element_value_type == 'classname':
                    return driver.find_element_by_class_name(element)
                elif element_value_type == 'text':
                    return driver.find_element_by_android_uiautomator('new UiSelector().text("'+str(element)+'")')
                elif element_value_type == 'xpath':
                    return driver.find_element_by_xpath(element)
                elif element_value_type == 'accessibility':
                    return driver.find_element_by_accessibility_id(element)
                elif element_value_type == 'desc':
                    return driver.find_element_by_android_uiautomator('new UiSelector().description("'+str(element)+'")')
                elif element_value_type == 'content':
                    return str(element)
                elif element_value_type == 'web':
                    return self.get_webview(element,driver)
                elif element_value_type == 'tost':
                    return self.get_tost(element,driver)
            else:
                return False
        except Exception as e:
            print(e)
            return False
        
    def back(self,driver):
        driver.press_keycode(key_code.KEYCODE_BACK.value)
        
    def home(self,driver):
        driver.keyevent(key_code.KEYCODE_HOME.name)
        
    def power(self,driver):
        driver.keyevent(key_code.KEYCODE_POWER.name)

    def get_webview(self,web_element,driver):
        time.sleep(10)
        web_view = driver.contexts  # 获取当前界面的所有子界面信息
        print(web_view)
        driver.switch_to.context(web_view[1])
        web_element_result = driver.find_element_by_link_text(web_element)
        driver.switch_to.context(web_view[0])
        driver.find_element_by_id('com.android.browser:id/back').click()
        return web_element_result

    def get_tost(self, tost_message,driver):  # 使用xpath定位
        tost_element = ('xpath', "//*[contains(@text," + tost_message + ")]")
        return WebDriverWait(driver, 10, 0.1).until(
            ec.presence_of_element_located(tost_element))  # 在10秒中内每间隔0.1秒去识别tost_element所指向的元素
        
        
