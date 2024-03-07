from airtest.core.api import connect_device, auto_setup, start_app, sleep, text, stop_app
from poco.drivers.ios import iosPoco
from self import self
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_iOS import App_Settings_Screen_iOS
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_iOS import Login_Screen_iOS
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_iOS import Add_A_Printer_Screen_iOS
from airtest.core.api import *
from poco import poco

from ZSB_Mobile.PageObject.Smoke_Test.Smoke_Test_iOS import Smoke_Test_iOS


class iOS_Smoke_Test:
    pass


# poco = iosPoco()

uuid = "00008101-00051D400144001E"
Bonding = connect_device("ios:///http+usbmux://" + uuid)
poco = iosPoco(device=Bonding)

auto_setup(logdir="./", compress=3,
           devices=[f"ios:///http+usbmux://{uuid}"])
start_app("com.zebra.soho")
sleep(5)

login_screen_ios = Login_Screen_iOS(poco)
app_settings_page_ios = App_Settings_Screen_iOS(poco)
add_a_printer_page_ios = Add_A_Printer_Screen_iOS(poco)
common_method = Common_Method(poco)
smoke_test_ios = Smoke_Test_iOS(poco)


# def test_AppSettings_TestcaseID_45875():
#     """	Fresh Install the app with apk/or from Google Store (Android) or from test flight/Apple Store (iOS)."""
#
#
# """Freshly install the app"""
# """start the app"""""
#
# common_method.Start_The_iOSApp()
# common_method.Stop_The_iOSApp()
# common_method.uninstall_iOS_app()
# common_method.install_iOS_app()
# common_method.Start_The_iOSApp()
# login_screen_ios.click_loginBtn()
# login_screen_ios.click_Continue_Btn_To_Login()
# """""Can't automate testflight build installation """
#

def test_AppSettings_TestcaseID_45876():
    """	Check basic functions work well after upgrading"""


""""Setup:
1. The previous version has already been installed in test device
2. Sign in the test account, with 1 printer added
3. There is at least one design in My designs"""""

""""Manually verify these below 3 steps as"""
"""start the app"""""
common_method.Start_The_iOSApp()
""""Upgrade the app, this needs to be executed manually"""
"""""""Verify the Already added Printer"""
app_settings_page_ios.Verify_Printer_is_already_added()
login_screen_ios.click_Menu_HamburgerICN()
app_settings_page_ios.click_My_Design()
add_a_printer_page_ios.click_FirstOne_In_MyDesign()
add_a_printer_page_ios.click_Print_Option()
add_a_printer_page_ios.click_Print_Button()
""""Verify manually it should print successfully"""
add_a_printer_page_ios.click_The_Back_Icon_Of_Print_Review_Screen()
login_screen_ios.click_Menu_HamburgerICN()
add_a_printer_page_ios.click_Common_Design_Tab()
add_a_printer_page_ios.click_FirstOne_Design_In_Common_Design()
add_a_printer_page_ios.click_FirstOne_In_Common_Design()
add_a_printer_page_ios.click_Print_Option()
add_a_printer_page_ios.click_Print_Button()
"""Verify manually it should print successfully"""
add_a_printer_page_ios.click_The_Back_Icon_Of_Print_Review_Screen()
add_a_printer_page_ios.click_The_Back_Icon_Of_Print_Review_Screen()
login_screen_ios.click_Menu_HamburgerICN()
app_settings_page_ios.click_Printer_Settings()
app_settings_page_ios.click_PrinterName_On_Printersettings()
app_settings_page_ios.click_Printer_Name_Text_Field()
app_settings_page_ios.Update_PrinterName_With_Different_Valid_Name()
app_settings_page_ios.verify_Printer_Name_Updated_Message()
app_settings_page_ios.click_PrinterName_On_Printersettings()
app_settings_page_ios.click_Printer_Name_Text_Field()
app_settings_page_ios.Update_PrinterName()
common_method.Stop_The_iOSApp()
"""""The below steps need to be verified manually""""""""""""""
6.Open any PDF file, then share to ZSB Series, print the file
Check the file can be printed out successfully
7. Open printer cover
Check the status on home page is shown as "Cover Open"
8. Close the printer cover
Check the status back to "Online"""""""""
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_45877():
#     """	Verify create a brand new user with unregistered user in Mobile App."""
#
#
# """"Setup:
# 1. Create a new email address
# (Need to match the new register email format, for IDC, it should be soho_swdvt_xxxx@xxxx.com, for CDC, it should be soho_swdvt_xxxx@xxxx.com)
# 2. Install the target build of ZSB app on mobile device"""""
#
# """start the app"""""
# common_method.Start_The_iOSApp()
# app_settings_page_ios.click_pen_Icon_near_UserName()
# app_settings_page_ios.Scroll_till_Delete_Account()
# app_settings_page_ios.click_Logout_Btn()
# login_screen_ios.click_loginBtn()
# login_screen_ios.click_Continue_Btn_To_Login()
# login_screen_ios.click_Login_With_Email_Tab()
# poco.scroll()
# smoke_test_ios.click_Register_Your_Email_Now_Option()
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_45878():
    """	Verify sign in as zebra, check link and delete one/google drive file works well"""


# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_45879():
    """Verify sign in as non-zebra, check link and delete one/google drive file works well"""


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_45880():
    """Verify sign in with non-zebra account, check the design linked different format file from local can be printed out successfully"""


# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_45881():
    """Verify sign in with social account, check the design linked different format file from Google Drive can be printed out successfully"""


# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_45882():
    """Verify sign in with non-Zebra account, check the design linked different format file from One Drive can be printed out successfully"""


common_method.Start_The_iOSApp()
login_screen_ios.click_Menu_HamburgerICN()
app_settings_page_ios.click_My_Design()
app_settings_page_ios.click_My_Design()
add_a_printer_page_ios.click_FirstOne_In_MyDesign()
add_a_printer_page_ios.click_Print_Option()
add_a_printer_page_ios.Verify_Design_Preview_Screen_With_Details()
add_a_printer_page_ios.click_Print_Button()
""""Verify manually it should print successfully"""
add_a_printer_page_ios.click_The_Back_Icon_Of_Print_Review_Screen()
add_a_printer_page_ios.click_SecondOne_In_MyDesign()
add_a_printer_page_ios.click_Print_Option()
add_a_printer_page_ios.click_Print_Button()
""""Verify manually it should print successfully"""
common_method.Stop_The_iOSApp()
"""""The below step needs to be verified manually"""
""""""""""2. Sign in the same account on Web portal, create design1, add text object, and link One Drive file with xlsx format. Create design2, add text object, and link One Drive file with csv format"""""""""

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_45883():
#     """Verify sign in sign out with registered social accounts in Mobile App."""
#
# """start the app"""
# common_method.Start_The_iOSApp()
# sleep(3)
# # login_screen_ios.click_Menu_HamburgerICN()
# # app_settings_page_ios.click_pen_Icon_near_UserName()
# # app_settings_page_ios.Scroll_till_Delete_Account()
# # app_settings_page_ios.click_Logout_Btn()
# login_screen_ios.click_loginBtn()
# login_screen_ios.click_Continue_Btn_To_Login()
# """""""""" check the 3 links at the bottom all can work ("copyright", "Terms & Conditions" and "Privacy Policy")"""""""""""
# smoke_test_ios.Verify_SignIn_With_Text_Is_Present()
# smoke_test_ios.click_Continue_With_Facebook_Option()
# """""due to some issue, it is directly login to the facebook account without asking for password"""
# login_screen_ios.click_Menu_HamburgerICN()
# smoke_test_ios.Verify_Facebook_UserName_Is_Displaying()
# app_settings_page_ios.click_pen_Icon_near_UserName()
# app_settings_page_ios.Scroll_till_Delete_Account()
# app_settings_page_ios.click_Logout_Btn()
# login_screen_ios.click_loginBtn()
# login_screen_ios.click_Continue_Btn_To_Login()
# smoke_test_ios.click_Continue_With_Apple_Option()
# smoke_test_ios.click_Continue_With_Password_ForApple_Login()
# smoke_test_ios.click_On_Password_Textfield()
# poco(text("Testing@123"))
# smoke_test_ios.click_On_Sign_In_Option()
# login_screen_ios.click_Menu_HamburgerICN()
# smoke_test_ios.Verify_Apple_UserName_Is_Displaying()
# app_settings_page_ios.click_pen_Icon_near_UserName()
# app_settings_page_ios.Scroll_till_Delete_Account()
# app_settings_page_ios.click_Logout_Btn()
# login_screen_ios.click_loginBtn()
# login_screen_ios.click_Continue_Btn_To_Login()
# login_screen_ios.click_Loginwith_Google()
# smoke_test_ios.Verify_Google_UserName_Is_Displaying()
# common_method.Stop_The_iOSApp()

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_45884():
#     """Add a printer- Out of the box user experience"""
#
#
# """""Test steps:
# 1. Turn off the testing printer, then use a toothpick to press the button on the printer back for about 10s, turn on the printer(Keep hold pressing the printer back button for about 20s)
# Check during this process, the power button is flashing white light, then flashing blue light and will auto feed the barcode info label. """""""""""
#
# """start the app"""
# common_method.Start_The_iOSApp()
# sleep(3)
# """"verify home text is displaying on the home screen"""
# app_settings_page_ios.Home_text_is_present_on_homepage()
# """click on the hamburger icon"""
# login_screen_ios.click_Menu_HamburgerICN()
# """"click on Add printer tab"""""
# add_a_printer_page_ios.click_Add_A_Printer()
# """"click on the start button"""
# add_a_printer_page_ios.click_Start_Button()
# """"Verify searching for your printer text"""
# add_a_printer_page_ios.Verify_Searching_for_your_printer_Text()
# """"verify select your printer text"""
# add_a_printer_page_ios.Verify_Select_your_printer_Text()
# """"select 2nd printer which you want to add"""
# add_a_printer_page_ios.click_2nd_Printer_Details_To_Add()
# """""click on select button"""
# add_a_printer_page_ios.click_Select_Button_On_Select_Your_Printer_Screen()
# """"verify pairing your printer text"""
# add_a_printer_page_ios.Verify_Pairing_Your_Printer_Text()
# """"accept Bluetooth pairing popup 1"""
# add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup1()
# """"accept Bluetooth pairing popup 2"""
# add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup2()
# """Verify Connect Wi-fi Network Text"""
# add_a_printer_page_ios.Verify_Connect_Wifi_Network_Text()
# """"click on connect button on connect wifi network screen"""
# add_a_printer_page_ios.click_Connect_Btn_On_Connect_Wifi_Network_Screen()
# """""""click password field on join network"""
# add_a_printer_page_ios.click_Password_Field_On_Join_Network()
# """"click submit button on join network"""
# add_a_printer_page_ios.click_Submit_Button_ON_Join_Network()
# """verify connecting to wifi network text"""
# add_a_printer_page_ios.Verify_Connecting_to_WiFi_Network_Text()
# """"verify need the printer driver text"""
# add_a_printer_page_ios.Verify_Need_the_Printer_Driver_Text()
# """""verify registering your printer text"""
# add_a_printer_page_ios.Verify_Registering_your_Printer_Text()
# """"click on finish setup button"""
# add_a_printer_page_ios.click_Finish_Setup_Button()
# app_settings_page_ios.Verify_Printer_is_already_added()
# """stop the app"""
# common_method.Stop_The_iOSApp()

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
