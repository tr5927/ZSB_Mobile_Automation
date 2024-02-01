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


def test_DataSources_TestcaseID_45757():
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
# sleep(5)
login_page.click_Menu_HamburgerICN()
sleep(5)
data_sources_page.clickMyDesigns()
# poco("My Designs").click()
sleep(5)
data_sources_page.selectDesignCreatedAtSetUp()
# poco("android.view.View")[5].click()
sleep(5)
data_sources_page.clickPrint()
# poco("Print").click()
sleep(5)
data_sources_page.verifyPhotoOptions()

poco.scroll()
data_sources_page.expandPhotoOptions()
# poco("android.view.View")[4].click()
sleep(5)
data_sources_page.chooseCameraToClickPhoto()
# poco("Camera").click()
sleep(5)
data_sources_page.Camera_Shutter()
# poco("com.google.android.GoogleCamera:id/shutter_button").click()
# sleep(5)
# poco("com.google.android.GoogleCamera:id/shutter_button").click()
data_sources_page.clickPrint()
# poco("Print").click()