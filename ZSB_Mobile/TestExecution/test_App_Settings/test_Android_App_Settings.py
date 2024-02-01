from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings_Screen import App_Settings_Screen
from ZSB_Mobile.PageObject.Add_A_Printer_Screen import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Login_Screen import Login_Screen


class Android_App_Settings:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
start_app("com.zebra.soho_app")
sleep(2.0)


def test_AppSettings_TestcaseID_45688():
    """""""""Verify Wifi Settings"""""

"""""Install the latest production app on the phone"""""""""
"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""Check whether App is installed or not"""
# # #"""""""" Allow pop up before login for the fresh installation""""""""
# login_page.click_LoginAllow_Popup()
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# sleep(2)
# """""provide google user id & password if it is a fresh installation"""
# login_page.click_GoogleID_Field()
# sleep(2)
#
# login_page.click_Bluetooth_Allow()
# """""""""""""""Always use this to login"""""""""""""""
# login_page.click_GooglemailId()
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
# """""""click on the left hamburger menu on the home page"""""""""
login_page.click_Menu_HamburgerICN()
"""""click on the printer settings tab"""
app_settings_page.click_Printer_Settings()
sleep(4)
# """""click on the printer tab"""
# app_settings_page.click_PrinterName_On_Printersettings()
# sleep(3)
# # """""""""""" click on the wifi tab option""""""""""""
# app_settings_page.click_wifi_tab()
# sleep(3)
# """""""""validate the Current network text and result"""""
# app_settings_page.get_text_CurrentNetwork_Txt()
# # """"""Verify the newtwork name text""""""
# app_settings_page.get_text_Network_Name_Txt()
# """""""Validate the Network status text"""""""
# app_settings_page.get_text_Network_Status_Txt()
# """"validatenetworkstatusresulttext"""
# app_settings_page.get_text_Network_Status_Result_Txt()
# # """""""" Verify IP address text"""""""
# app_settings_page.get_text_IPAddress_Txt()
# # """""""" Verify IP address result text"""""""
# app_settings_page.get_text_IPAddress_Result_Txt()
# # """"""""Verify the message You can save upto 5 network profiles to your saved networks after Manage Networks"""
# app_settings_page.IS_Present_Save_Network_Message_Txt()
# """""""verify manage networks text is present & clickable"""""""
# app_settings_page.click_Manage_Networks_Btn()
# sleep(3)




# def test_AppSettings_TestcaseID_45689():
#     """""""""VCheck Change Theme Function Works"""""
#
# """""Install the latest production app on the phone"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
# login_page = Login_Screen(poco)
# app_settings_page = App_Settings_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""Check whether App is installed or not"""
# """""""" Allow pop up before login for the fresh installation""""""""
# login_page.click_LoginAllow_Popup()
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# sleep(2)
# """""provide google user id & password if it is a fresh installation"""
# # login_page.click_GoogleID_Field()
# # sleep(2)
# """""""""""""""Always use this to login"""""""""""""""
# login_page.click_GooglemailId()
# sleep(2)
# login_page.Enter_Google_UserID()
# sleep(2)
# login_page.click_Emailid_Nextbtn()
# sleep(4)
# """"To enter password need to use the 2nd method """
# # login_page.Enter_Google_Password()
# # poco(text("Swdvt@#123"))
# # sleep(2)
# login_page.click_Password_Nextbtn()
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_Threedot_On_Workspace()




