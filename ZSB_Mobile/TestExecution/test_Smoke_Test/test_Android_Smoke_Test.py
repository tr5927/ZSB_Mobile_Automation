from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.PageObject.Smoke_Test.Smoke_Test_Android import Smoke_Test_Android


class Android_App_Settings:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
start_app("com.zebra.soho_app")
sleep(2.0)

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
smoke_test_android = Smoke_Test_Android(poco)

def test_AppSettings_TestcaseID_45875():
    """	Fresh Install the app with apk/or from Google Store (Android) or from test flight/Apple Store (iOS)."""


"""Freshly install the app"""
"""start the app"""""
common_method.Start_The_App()
common_method.relaunch_app()
common_method.uninstall_App()
common_method.install_App()

"""""Can't automate testflight build installation """


def test_AppSettings_TestcaseID_45876():
    """	Check basic functions work well after upgrading"""


""""Setup:
1. The previous version has already been installed in test device
2. Sign in the test account, with 1 printer added
3. There is at least one design in My designs"""""

"""start the app"""""
common_method.Start_The_iOSApp()
""""Uninstall the already installed app"""
common_method.uninstall_App()
"""""Upgrade Android App """
common_method.Upgrade_Android_App()
"""start the app"""
common_method.Start_The_iOSApp()
"""""""Verify the Already added Printer"""
app_settings_page.Verify_Printer_is_already_added()
login_page.click_Menu_HamburgerICN()
app_settings_page.click_My_Design()
add_a_printer_screen.click_FirstOne_In_MyDesign()
add_a_printer_screen.click_Print_Option()
add_a_printer_screen.click_Print_Button()
""""Verify manually it should print successfully"""
add_a_printer_screen.click_Back_Icon_On_Print_Screen()
login_page.click_Menu_HamburgerICN()
add_a_printer_screen.click_Common_Design()
add_a_printer_screen.click_FirstOne_Design_In_Common_Design()
add_a_printer_screen.click_FirstOne_In_Common_Design()
add_a_printer_screen.click_Print_Option()
add_a_printer_screen.click_Print_Button()
"""Verify manually it should print successfully"""
add_a_printer_screen.click_Back_Icon_On_Print_Screen()
login_page.click_Menu_HamburgerICN()
app_settings_page.click_Printer_Settings()
app_settings_page.click_PrinterName_On_Printersettings()
app_settings_page.click_Printer_Name_Text_Field()
app_settings_page.Update_PrinterName_With_Different_Valid_Name()
app_settings_page.Verify_Printer_Name_Updated_Message()
app_settings_page.click_PrinterName_On_Printersettings()
app_settings_page.click_Printer_Name_Text_Field()
app_settings_page.Update_PrinterName()
common_method.Stop_The_iOSApp()
smoke_test_android.Open_Device_Files()
smoke_test_android.click_PDF_File()
smoke_test_android.click_share_option()
smoke_test_android.click_ZSB_Series_To_Print()
smoke_test_android.click_Print_Option()
"""Verify manually it should print successfully"""
""""""" Open printer cover manually"""""
""""""start the app"""""""""""
Common_Method.Start_The_iOSApp()
""""Check the status on home page is shown as Cover Open"""""
smoke_test_android.Verify_Cover_Open_Text_Is_Present()
"""""Close the printer cover manually"""""""
""""Check the status back to Online"""""""
smoke_test_android.Verify_Printer_Online_Text_Is_Present()
""""Stop the App"""
common_method.Stop_The_iOSApp()