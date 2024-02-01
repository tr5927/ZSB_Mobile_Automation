from turtle import up

import self
from poco import poco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

import ZSB_Mobile.TestExecution.test_Help
import ZSB_Mobile.TestExecution.test_App_Settings
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Data_Sources_Screen import Data_Sources_Screen
from ZSB_Mobile.PageObject.Login_Screen import *

from ZSB_Mobile.PageObject.Add_A_Printer_Screen import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.APP_Settings_Screen import App_Settings_Screen
from ZSB_Mobile.PageObject.Help_Screen import Help_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Printer_Management_Screen import Printer_Management_Screen


class Android_App_Help:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
start_app("com.zebra.soho_app")
sleep(2.0)

common_method = Common_Method()
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)

def test_DataSources_TestcaseID_47942():
    """""""""test"""""



# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# sleep(2)
# login_page.click_GooglemailId()
# sleep(5)
# login_page.add_Account()
# sleep(2)
# login_page.Enter_Google_UserID()
# sleep(2)
# login_page.click_Emailid_Nextbtn()
# sleep(4)
# """"To enter password need to use the 2nd method """
# login_page.Enter_Google_Password()
# # poco(text("Swdvt@#123"))
# # sleep(2)
# login_page.click_Password_Nextbtn()
# sleep(7)
# help_page.chooseAcc()
"""Click hamburger icon to expand menu"""
sleep(5)
login_page.click_Menu_HamburgerICN()
sleep(5)
"""Click My Data"""
data_sources_page.click_My_Data()
sleep(5)
"""Click Add File"""
data_sources_page.click_Add_File()
sleep(5)
"""Click Upload file"""
data_sources_page.click_Upload_File()
sleep(5)
"""Select File to upload"""
data_sources_page.select_File_To_Upload()
sleep(5)
"""Verify Progress Indicator"""
data_sources_page.verifyProgressIndicator()
sleep(10)
"""Verify if file uploaded succesfully"""
common_method.swipe_screen([0.9, 0.3482905982905983], [0.22037037037037038, 0.3482905982905983], 3)
data_sources_page.verify_File_Data()