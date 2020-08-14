#coding = utf-8


from appium import webdriver
from Appium_PO_Model.Utils.Get_Config import get_config
from Appium_PO_Model.Utils.Device_Config import device_config
class base_driver(object):
    

    
    def __android_driver(self,app_name,phone_id):
        '''
        配置待测终端的参数，并返回设备对象
        param device_param:设备信息，{'device_name':设备串号,'package_type':操作的app类型（app则表示需要安装，package则表示是包名类名启动）,'app_name':需要操作的应用名称}
        return: 返回设备对象，此对象以挂载到appiumserver上
        '''
        device_infor = device_config()
        phone_caps = {}
        get_package_config = get_config('..\\Config\\App_Package_Activity.ini')
        app_package_infor = get_package_config.get_config_by_section_key(app_name)
        phone_caps['platformName'] = 'Android'
        #phone_caps['automationName'] = 'UiAutomator2'
        phone_caps['deviceName'] = phone_id
        if app_package_infor[0] == 'package':
            phone_caps['appPackage'] = app_package_infor[1].split('/')[0]
            phone_caps['appActivity'] = app_package_infor[1].split('/')[1]
        else:
            phone_caps['app'] = app_package_infor[1]
        phone_caps['noReset'] = True
        driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub'%str(device_infor.get_device_infor_from_config(phone_caps['deviceName'])['port']),phone_caps)
        return driver
    
    
    
    
    
    def get_driver(self,app_name,phone_id):
        return self.__android_driver(app_name,phone_id)

