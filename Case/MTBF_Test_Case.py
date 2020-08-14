#coding=utf-8
import unittest,HTMLTestRunner,threading,datetime,time,multiprocessing
import sys
sys.path.append('./')
from Utils.Appium_Server import appium_server
class ParametrizedTestCase(unittest.TestCase):  
    '''
    用于unittest传参
    '''
    """ TestCase classes that want to be parametrized should 
        inherit from this class. 
    """  
    def __init__(self, methodName='runTest', param=None):  
        super(ParametrizedTestCase, self).__init__(methodName)  
        global case_param
        case_param = param  
#     @staticmethod  
#     def parametrize(testcase_class,name, device_param=None):  
#         """ Create a suite containing all tests taken from the given 
#             subclass, passing them the parameter 'param'. 
#         """  
#         testloader = unittest.TestLoader()  
#         testnames = testloader.getTestCaseNames(testcase_class)  
#         suite = unittest.TestSuite()  
# #         for name in testnames:  
# #             suite.addTest(testcase_klass(name, param=param))  
#         suite.addTest(testcase_class(name,device_param=device_param))
#         return suite 

class mtbf_test_case(ParametrizedTestCase):
#class mtbf_test_case(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls):
        print('this setup class')
        print('device_parm %s'%case_param)

    def setUp(self):
        print('this is setup')

    def test_add_new_contact(self):
        print('MTBF001 新增联系人')
        #self.assertEqual('1','2','Error')

    def test_dail(self):
        print('dail 10086')

    #@unittest.skip('mtbf_test_case')
    def test_send_sms(self):
        print('send new sms')
        

    def test_check_sms(self): 
        pass

    def test_app_download(self):
        print('download app')
        
        
    def test_a(self):
        a = {'1':4,'2':'aaaaa'}
        b = {'1':3}
        self.assertDictContainsSubset(b,a)

    @classmethod
    def tearDownClass(cls):
        print('this is teardown class')

    def tearDown(self):
        print('this is teradown')


    



def get_suite(device_name):
    test_case_suite = unittest.TestSuite()
    test_case_suite.addTest(mtbf_test_case('test_a'))
    #test_case_suite.addTests([mtbf_test_case('test_dail'),mtbf_test_case('test_send_sms'),mtbf_test_case('test_check_sms')])
    #unittest.TextTestRunner().run(test_case_suite)
    html_file = '.\\report\\report_'+str(device_name)+'_'+str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))+'.html'
    fp = open(html_file,mode='a',errors = 'ignore')
    HTMLTestRunner.HTMLTestRunner(fp).run(test_case_suite)




if __name__ == '__main__':
    get_suite('bbbb')
    #unittest.main()
    # server = appium_server()
    # server.main()
    # print(server.device_name_list)
#     time.sleep(20)
#     param.device_name = device_name_dict[0]
#     get_suite()
#     threads = []
#     for device_name in server.device_name_list:
#         print(device_name)
#         t = multiprocessing.Process(target=get_suite,args = (device_name,))
#         threads.append(t)
#     for t in threads:
#         t.start()
#         t.join()
    
