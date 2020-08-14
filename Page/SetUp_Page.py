'''
Created on 2020年4月9日

@author: likecan
'''
from Utils.Get_Element_Config import get_element_config
class setup_page(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.get_element = get_element_config()
        
        
        
        
    def biometrics_password(self,driver):
        '''
        生物识别和密码
        '''
        return self.get_element.get_local_by_element('rec_password', driver)
    
    
    def face_recognized(self,driver):
        '''
        人脸识别
        '''
        return self.get_element.get_local_by_element('face_rec', driver)
    
    
    def input_password_blank(self,driver):
        '''
        密码输入栏
        '''
        return self.get_element.get_local_by_element('pin', driver)
    
    
    def password(self):
        '''
        密码
        '''
        return self.get_element.get_local_by_element('password')
    
    def face_data_existed(self,driver):
        '''
        人脸数据是否已经存在
        '''
        return self.get_element.get_local_by_element('face_data_exist', driver)
    
    
    def del_face_data(self,driver):
        '''
        确认删除已存在的人脸数据
        '''
        return self.get_element.get_local_by_element('del_face', driver)
    
    
    
    def start_record_face(self,driver):
        '''
        开始录入人脸
        '''
        return self.get_element.get_local_by_element('start_record_face', driver)
    
    
    
    def phone_move_left(self,driver):
        '''
        设备左移一点
        '''
        return self.get_element.get_local_by_element('move_left', driver)
    
    def phone_move_right(self,driver):
        '''
        设备右移一点
        '''
        return self.get_element.get_local_by_element('move_right', driver)
    
    
    def phone_move_up(self,driver):
        '''
        设备上移一点
        '''
        return self.get_element.get_local_by_element('move_up', driver)
    
    
    
    def phone_move_down(self,driver):
        '''
        设备下移一点
        '''
        return self.get_element.get_local_by_element('move_down', driver)
    
    
    
    def make_sure_face_in_phone(self,driver):
        '''
        确保是人脸在框里
        '''
        return self.get_element.get_local_by_element('make_sure_in', driver)
    
    