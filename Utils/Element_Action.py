#coding=utf-8
from appium.webdriver.common.touch_action import TouchAction
class element_action(object):


    def touchtap(self,element):
        element.click()

    def is_item_exis(self,element):
        if element:
            print('识别成功')
            return True
        return  False

    def touch_long_tap(self,driver,element):
        TouchAction(driver).long_press(element,duration=5).perform()
    
    
    def screen_on(self,driver,from_element,to_element):
        
        pass
    
    def send_content(self,element,content):
        element.send_keys(content)
        
    
    
    
        
        
    def get_phone_size(self,driver):
        window_size = driver.get_window_size()
        return window_size
        
    
    def swip_to_element(self,driver,element):
        pass
    
    def swip_screen_by_element(self,driver,from_element,to_element,duration = None):
        '''
        从一个元素滑动到另一个元素
        param from_element:开始滑动的元素
        param to_element:结束滑动的元素
        '''
        driver.scroll(from_element,to_element,duration)
    

    def __swip_left(self,driver, duration=None):
        start_x = self.get_phone_size(driver)['width'] / 10 * 9
        end_x = self.get_phone_size(driver)['width'] / 10
        y = self.get_phone_size(driver)['height'] / 2
        driver.swipe(start_x, y, end_x, y, duration)

    def __swip_right(self,driver, duration=None):
        start_x = self.get_phone_size(driver)['width'] / 10
        end_x = self.get_phone_size(driver)['width'] / 10 * 9
        y = self.get_phone_size(driver)['height'] / 2
        driver.swipe(start_x, y, end_x, y, duration)

    def __swip_up(self,driver, duration=None):
        start_y = self.get_phone_size(driver)['height'] / 10 * 7
        end_y = self.get_phone_size(driver)['height'] / 10
        x = self.get_phone_size(driver)['width'] / 2
        driver.swipe(x, start_y, x, end_y, duration)

    def __swip_down(self,driver, duration=None):
        start_y = self.get_phone_size(driver)['height'] / 10
        end_y = self.get_phone_size(driver)['height'] / 10 * 7
        x = self.get_phone_size(driver)['width'] / 2
        driver.swipe(x, start_y, x, end_y, duration)

    def swip_screen(self,driver, swip_direction, duration=None):
        if swip_direction == 'left':
            self.__swip_left(driver,duration)
        elif swip_direction == 'right':
            self.__swip_right(driver,duration)
        elif swip_direction == 'up':
            self.__swip_up(driver,duration)
        elif swip_direction == 'down':
            self.__swip_down(driver,duration)
        else:
            raise Exception('diercton Error')