'''
Created on 2020年4月10日

@author: likecan
'''
#coding=utf-8


from Appium_PO_Model.Page.SetUp_Page import setup_page
from Appium_PO_Model.Utils.Element_Action import element_action
from adodbapi.examples.xls_read import driver
class setup_page_handle(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.setup = setup_page()
        self.elem_action = element_action()
        
        
    def biometrics_password_click(self,driver):
        self.elem_action.touchtap(self.setup.biometrics_password(driver))
        
    
    def face_recognized_click(self,driver):
        self.elem_action.touchtap(self.setup.face_recognized(driver))
    
    
    def input_password(self,driver):
        self.elem_action.send_content(self.setup.input_password_blank(driver),self.setup.password())
        
        
    def del_face_data_click(self,driver):
        self.elem_action.touchtap(self.setup.del_face_data(driver))
        
        
    def start_record_face_click(self,driver):  
        self.elem_action.touchtap(self.setup.start_record_face(driver))
        
        
    def is_face_data_exist(self,driver):
        return self.elem_action.is_item_exis(self.setup.face_data_existed(driver))
    
    def move_face(self,driver):
        if self.setup.phone_move_left(driver):
            return 'left'
        elif self.setup.phone_move_right(driver):
            return 'right'
        elif self.setup.phone_move_up(driver):
            return 'up'
        elif self.setup.phone_move_down(driver):
            return 'down'