from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ZSB_Mobile.PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ZSB_Mobile.PageObject.Smoke_Test.Smoke_Test_Android import Smoke_Test_Android
from ZSB_Mobile.PageObject.Others import Others


class Android_App_Settings:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# start_app("com.zebra.soho_app")
sleep(2.0)

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
smoke_test_android = Smoke_Test_Android(poco)
registration_page = Registration_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
others = Others
aps_notification = APS_Notification(poco)

""""""""""Fresh build installation is required,app should be loggedin"""""""""""""""
"""""Setup:
1. The APS has been ready and turn on in the Android device(Reference path : Settings -> Connection & sharing -> print)
2. The target printers are connected with the target mobile app login account
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_49144():
    """Check all supported formats files or informations can be printed by the printer service"""


common_method.Start_The_App()
login_page.click_Menu_HamburgerICN()
app_settings_page.click_pen_Icon_near_UserName()
app_settings_page.Scroll_till_Delete_Account()
app_settings_page.click_Logout_Btn()
common_method.Stop_The_App()
aps_notification.Stop_Android_App()
aps_notification.Stop_Android_App()
aps_notification.click_Mobile_SearchBar()
aps_notification.click_On_Searchbar2()
aps_notification.Enter_Files_Text_On_SearchBar()
aps_notification.click_Files_Folder()
aps_notification.click_Drive_Searchbar()
aps_notification.click_Drive_Searchbar2()
aps_notification.click_PDF_File_From_The_List()
aps_notification.click_Suggestion_PDF_File()
aps_notification.click_PDF_ON_Result()
aps_notification.click_ON_Three_Dot()
aps_notification.click_Print_Option()
