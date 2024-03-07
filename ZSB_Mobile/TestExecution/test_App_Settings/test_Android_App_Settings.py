from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen


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


# def test_AppSettings_TestcaseID_47918():
#     """	Verify ZSB app permission works fine."""


# """start the app"""
# common_method.Start_The_App()
# """""Install the latest production app on the phone & printer should be added"""""""""
#
# """""Check whether App is installed or not"""
# """"""" Allow pop up before login for the fresh installation"""""""
# login_page.click_LoginAllow_Popup()
# """""for the first installation click on the zsb series popup"""
# login_page.click_Allow_ZSB_Series_Popup()
# """""""click on the login button"""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# sleep(2)
# """""""""""""""Always use this to login"""""""""""""""
# login_page.click_GooglemailId()
# sleep(2)
# login_page.Enter_Google_UserID()
# sleep(2)
# login_page.click_Emailid_Nextbtn()
# sleep(4)
# """"enter password """
# poco(text("Swdvt@#123"))
# sleep(2)
# login_page.click_Password_Nextbtn()
# sleep(7)
# """""Relaunch the app"""
# common_method.relaunch_app()
# """Permission is not displaying"""
# login_page.Verify_LoginAllow_Popup_IS_Not_Displaying()
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_45688():
#     """""""""Verify Wifi Settings"""""
#
# """""Install the latest production app on the phone & printer should be added"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
# login_page = Login_Screen(poco)
# app_settings_page = App_Settings_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""Check whether App is installed or not"""
# """""""" Allow pop up before login for the fresh installation""""""""
# login_page.click_LoginAllow_Popup()
# """""for the first installation click on the zsb series popup"""
# login_page.click_Allow_ZSB_Series_Popup()
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# sleep(2)
# """""""""""""""Always use this to login"""""""""""""""
# login_page.click_GooglemailId()
# sleep(2)
# login_page.Enter_Google_UserID()
# sleep(2)
# login_page.click_Emailid_Nextbtn()
# sleep(4)
# """"enter password """
# poco(text("Swdvt@#123"))
# sleep(2)
# login_page.click_Password_Nextbtn()
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# login_page.click_Menu_HamburgerICN()
# """""click on the printer settings tab"""
# app_settings_page.click_Printer_Settings()
# sleep(4)
# """""click on the printer tab"""
# app_settings_page.click_PrinterName_On_Printersettings()
# sleep(3)
# """"Verify the Test print button text & tab"""
# app_settings_page.Test_Print_button_is_present_on_printer_settings_page()
# # """""""""""" click on the wifi tab option""""""""""""
# app_settings_page.click_wifi_tab()
# # sleep(3)
# """""""""validate the Current network text"""""
# app_settings_page.test_CurrentNetwork_Txt_is_present_on_printer_settings_page()
# """""""Validate the Network status text is present on the printer settings screen"""""""
# app_settings_page.test_Network_Status_Txt_is_present_on_printer_settings_page()
# """"validate network status result text on the printer settings screen"""
# app_settings_page.get_text_Network_Status_Result_Txt()
# # """""""" Verify IP address text is present on the printer settings screen"""""""
# app_settings_page.get_text_IPAddress_Txt()
# # """""""" Verify IP address result text"""""""
# #app_settings_page.get_text_IPAddress_Result_Txt()
# # """"""""Verify the message You can save upto 5 network profiles to your saved networks after Manage Networks"""
# app_settings_page.IS_Present_Save_Network_Message_Txt()
# """""""verify manage networks text is present & clickable"""""""
# sleep(2)
# app_settings_page.click_Manage_Networks_Btn()
# sleep(2)
# """""""""""""Click on continue button on the Bluetooth Connection required popup"""""""
# app_settings_page.accept_Continue_popup()
# """""""""Verify the Cancel button on the Bluetooth_Connection_Failed_Popup"""""
# sleep(20)
# app_settings_page.Cancel_is_present_on_Bluetooth_Connection_Failed_Popup()
# """"""verify the continue button and click on that""""""""
# app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
# sleep(4)
# """"""""""Verify the red remove icon next to the network name"""""
# app_settings_page.click_Red_Icon_to_remove_network()
# sleep(5)
# """"""""Verify the Add Network text & button & click on that"""""
# app_settings_page.click_Add_Network()
# sleep(3)
# """""""""""""Verify Add network page is opening and verify the text"""""""
# app_settings_page.get_text_Add_Network()
# """""""select the previously deleted network"""
# app_settings_page.click_deleted_network()
# sleep(3)
# """""""""validate the Current network text"""""
# app_settings_page.test_CurrentNetwork_Txt_is_present_on_printer_settings_page()
# """""7 to 10 need to check on Web portal"""
# stop_app("com.zebra.soho_app")
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_45689():
#     """""""""Check Change Theme Function Works"""""
#
# """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
# """""Check whether App is installed or not"""
# # """"""start the app""""""
# start_app("com.zebra.soho_app")
# # """"""""click hamburger menu""""""
# login_page.click_Menu_HamburgerICN()
# # """"""""click three dot on workspace""""
# app_settings_page.click_Three_Dot_On_Workspace()
# """""""verify edit text"""""""
# app_settings_page.get_text_Edit_Txt()
# # """"click on change theme"""
# app_settings_page.click_Change_Theme()
# # # """""verify change theme page pop ups by verifying the change theme header"""
# app_settings_page.get_text_Change_Theme_Header()
# sleep(1)
# """""""change 5 theme and check it should get saved and then need to tap on exit"""""""
# app_settings_page.check_Change_Electic_Theme()
# sleep(3)
# # """""click save & exit button"""
# app_settings_page.click_Save_Exit_Btn()
# # """""""SMBM-986 is still present """""""
# # """"""""After applying the theme check whether it is navigating back to home page not verifying the background image as there is no element present """"""z
# sleep(3)
# app_settings_page.Home_text_is_present_on_homepage()
# """""click on hamburger icon on home page"""
# login_page.click_Menu_HamburgerICN()
# sleep(4)
# """"click on three dot icon on workspace"""""
# app_settings_page.click_Three_Dot_On_Workspace()
# """"click on change theme"""
# app_settings_page.click_Change_Theme()
# """""check Bohemian theme"""
# sleep(3)
# poco.scroll()
# app_settings_page.check_Change_Bohemian_Theme()
# sleep(3)
# # """""click save & exit button"""
# app_settings_page.click_Save_Exit_Btn()
# sleep(3)
# app_settings_page.Home_text_is_present_on_homepage()
# """""click on hamburger icon on home page"""
# login_page.click_Menu_HamburgerICN()
# sleep(4)
# """"click on three dot icon on workspace"""""
# app_settings_page.click_Three_Dot_On_Workspace()
# """"click on change theme"""
# app_settings_page.click_Change_Theme()
# """""check Professional theme"""
# poco.scroll()
# sleep(3)
# app_settings_page.check_Change_Professional_Theme()
# sleep(3)
# # """""click save & exit button"""
# app_settings_page.click_Save_Exit_Btn()
# sleep(3)
# app_settings_page.Home_text_is_present_on_homepage()
# """""click on hamburger icon on home page"""
# login_page.click_Menu_HamburgerICN()
# sleep(4)
# """"click on three dot icon on workspace"""""
# app_settings_page.click_Three_Dot_On_Workspace()
# """"click on change theme"""
# app_settings_page.click_Change_Theme()
# """""check Maker theme"""
# poco.scroll()
# poco.scroll()
# sleep(3)
# app_settings_page.check_Change_Maker_Theme()
# sleep(3)
# # """""click save & exit button"""
# app_settings_page.click_Save_Exit_Btn()
# sleep(3)
# """"""""
# app_settings_page.Home_text_is_present_on_homepage()
# """""click on hamburger icon on home page"""
# login_page.click_Menu_HamburgerICN()
# sleep(4)
# """"click on three dot icon on workspace"""""
# app_settings_page.click_Three_Dot_On_Workspace()
# """"click on change theme"""
# app_settings_page.click_Change_Theme()
# """""check Modern theme"""
# sleep(3)
# app_settings_page.check_Change_Modern_Theme()
# sleep(3)
# # """""click save & exit button"""
# app_settings_page.click_Save_Exit_Btn()
# sleep(3)
# app_settings_page.Home_text_is_present_on_homepage()
# stop_app("com.zebra.soho_app")
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_45690():
#     """""""""Update Unit of Measure in Mobile App, check it will sync to Web Portal and Printer Tools"""""
#
#
# """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
# """""Check whether App is installed or not"""
# """""start the app"""
# start_app("com.zebra.soho_app")
# sleep(3)
# # """"""""click hamburger menu""""""
# login_page.click_Menu_HamburgerICN()
# """"click on the pen icon near the user name"""
# app_settings_page.click_pen_Icon_near_UserName()
# sleep(1)
# poco.scroll()
# # """"""""verify units of measurement text is present or not""""""
# app_settings_page.check_If_Units_of_Measurements_Is_Present()
# """""""verify  Inches is the by default value is displaying"""""""
# app_settings_page.Inches_is_displaying()
# # """"""""click on Units of measurements""""""
# app_settings_page.click_Units_of_Measurements()
# sleep(2)
# # """"""""Verify all the available values""""""
# app_settings_page.verify_Milimetres_Is_Present()
# app_settings_page.verify_Centimetres_Is_Present()
# app_settings_page.verify_Inches_Is_Present()
# sleep(2)
# """"click on Centimeters option"""
# app_settings_page.click_Centimeters()
# sleep(1)
# # """"""""verify the updated message popup""""""
# app_settings_page.verify_updated_msg()
# # """""""Click on the hamburger icon"""""""
# sleep(2)
# login_page.click_Menu_HamburgerICN()
# """""click on the home tab"""
# app_settings_page.click_Home_Tab()
# sleep(2)
# """""""""verify printer details, everything should display in centimeters"""""
# app_settings_page.verify_printer_details_in_Centimeters()
# sleep(2)
# login_page.click_Menu_HamburgerICN()
# """""click on my design tab"""
# app_settings_page.click_My_Design()
# sleep(4)
# """""verify the design size under my design"""
# app_settings_page.verify_My_Details_Design_in_Centimeters()
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_pen_Icon_near_UserName()
# sleep(1)
# poco.scroll()
# app_settings_page.click_Units_of_Measurements()
# sleep(2)
# app_settings_page.click_Inches()
# sleep(2)
# """""stop the app"""
# stop_app("com.zebra.soho_app")
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_45691():
#     """""""""Edit Workspace - upload and remove image"""""
#
#
# """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
# """""Check whether App is installed or not"""
# """"start the app"""""
# start_app("com.zebra.soho_app")
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_Three_Dot_On_Workspace()
# app_settings_page.click_Edit_Txt()
# sleep(2)
# """""verify the Edit workspace text"""
# app_settings_page.get_text_Edit_Workspace()
# #""""""click upload photo""""""
# app_settings_page.click_upload_photo()
# sleep(2)
# # """""click on the 1st image"""
# app_settings_page.click_First_Image()
# sleep(2)
# """click on the save & exit"""
# app_settings_page.click_Save_Exit_Btn()
# sleep(2)
# app_settings_page.click_Three_Dot_On_Workspace()
# app_settings_page.click_Edit_Txt()
# sleep(2)
# app_settings_page.click_Remove_Image()
# app_settings_page.Is_Present_Profile_Avatar_Letter()
# sleep(2)
# app_settings_page.click_upload_photo()
# sleep(1)
# app_settings_page.click_Back_Icon()
# sleep(2)
# app_settings_page.click_Save_Exit_Btn()
# sleep(2)
# """""stop the app"""
# stop_app("com.zebra.soho_app")
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_45692():
#     """""""""Edit Workspace - Update workspace name"""""
#
# """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
#
#
# """""Check whether App is installed or not"""
# # """"""""""""start the app"""""""""""""
# start_app("com.zebra.soho_app")
# sleep(3)
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_Three_Dot_On_Workspace()
# app_settings_page.click_Edit_Txt()
# sleep(2)
# """""verify the Edit workspace text"""
# app_settings_page.get_text_Edit_Workspace()
# """"Verify Workspace Name Text"""
# sleep(2)
# app_settings_page.Is_Present_Workspace_Name_Text()
# # """"""""click on workspace name""""
# app_settings_page.click_Workspace_Name_Text_Field()
# """""clear workspace name text field"""
# app_settings_page.Clear_Workspace_Name()
# sleep(2)
# """"Click on keyboard back icon"""
# app_settings_page.click_Keyboard_back_Icon()
# # """"""""""""""""""Verify save & exit option is not there""""""""""""""
# # app_settings_page.Verify_SaveExit_Option_Is_Not_There()
# """""click on back icon on edit workspace"""
# app_settings_page.click_back_Icon_On_Edit_Workspace()
# app_settings_page.click_Three_Dot_On_Workspace()
# app_settings_page.click_Edit_Txt()
# sleep(2)
# # """"""""Check the previous Workspace name is displaying""""""
# app_settings_page.Is_Present_Workspace_Name()
# app_settings_page.click_Workspace_Name_Text_Field()
# app_settings_page.Clear_Workspace_Name()
# sleep(2)
# app_settings_page.click_Workspace_Name_Text_Field()
# """"verify the workspace field by giving space """
# app_settings_page.Update_Workspace_Name_With_Space()
# sleep(3)
# """"Click on keyboard back icon"""
# app_settings_page.click_Keyboard_back_Icon()
# sleep(3)
# app_settings_page.click_Save_Exit_Btn()
# sleep(3)
# app_settings_page.click_Three_Dot_On_Workspace()
# app_settings_page.click_Edit_Txt()
# app_settings_page.click_Workspace_Name_Text_Field()
# app_settings_page.Clear_Workspace_Name()
# sleep(2)
# """"Click on keyboard back icon"""
# app_settings_page.click_Keyboard_back_Icon()
# sleep(1)
# app_settings_page.click_Workspace_Name_Text_Field()
# """"verify the workspace field by special characters with more than 30 characters """
# app_settings_page.Update_Workspace_Name_With_Special_Characters_with_30_characters()
# sleep(3)
# """"Click on keyboard back icon"""
# app_settings_page.click_Keyboard_back_Icon()
# sleep(3)
# """""click on save & exit button"""
# app_settings_page.click_Save_Exit_Btn()
# sleep(3)
# app_settings_page.click_Three_Dot_On_Workspace()
# app_settings_page.click_Edit_Txt()
# """"""""""Verify the workspace updated name"""""""""""""""
# app_settings_page.Verify_Updated_Name()
# sleep(3)
# app_settings_page.click_Workspace_Name_Text_Field()
# app_settings_page.Clear_Workspace_Name()
# sleep(2)
# """"Click on keyboard back icon"""
# app_settings_page.click_Keyboard_back_Icon()
# app_settings_page.click_Workspace_Name_Text_Field()
# app_settings_page.Update_Workspace_Name_with_Original_Name()
# sleep(3)
# app_settings_page.click_Keyboard_back_Icon()
# sleep(3)
# """""click on save & exit button"""
# app_settings_page.click_Save_Exit_Btn()
# sleep(3)
# """"stop the app"""
# stop_app("com.zebra.soho_app")
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# """"""""""""""""""""""""""""""need to execute"""""""""""""""""""""""""""""""""""
# def test_AppSettings_TestcaseID_45705():
#     """""""""Verify account profile update for non-Zebra user"""""
#
#
# """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
# """""Check whether App is installed or not"""
# # """""""start the app"""""""
# start_app("com.zebra.soho_app")
# # """"""""click hamburger menu""""""
# login_page.click_Menu_HamburgerICN()
# """"click on the pen icon near the user name"""
# app_settings_page.click_pen_Icon_near_UserName()
# """""""verify First name text is present"""""""
# app_settings_page.Is_Present_First_Name_Text()
# """""""verify last name text is present"""""""
# app_settings_page.Is_Present_Last_Name_Text()
# """""click first name text field"""
# app_settings_page.click_First_Name_Text_Field()
# """"clear first name field"""
# sleep(3)
# app_settings_page.clear_First_Name()
# """""Update first name with special characters with 30 characters"""
# app_settings_page.Update_First_Name_With_Special_Characters_with_30_characters()
# sleep(3)
# poco.scroll()
# sleep(3)
# """""click last name text field"""
# app_settings_page.click_Last_Name_Text_Field()
# """"clear Last name field"""
# app_settings_page.clear_Last_Name()
# """""Update last name with special characters with 30 characters"""
# app_settings_page.Update_Last_Name_With_Special_Characters_with_30_characters()
# sleep(3)
# """""click keyboard back icon"""
# app_settings_page.click_Keyboard_back_Icon()
# """"verify the updated names message"""
# app_settings_page.verify_Your_changes_have_been_saved_Message()
# sleep(3)
# """""click First name text field"""
# app_settings_page.click_First_Name_Text_Field()
# """"clear First name field"""
# app_settings_page.clear_First_Name()
# """Update the default First name"""
# app_settings_page.Update_Default_First_Name()
# sleep(3)
# """""click last name text field"""
# app_settings_page.click_Last_Name_Text_Field()
# """"clear Last name field"""
# app_settings_page.clear_Last_Name()
# """Update the default Last name"""
# app_settings_page.Update_Default_Last_Name()
# # """"""change password link is not opening the correct page---SMBM-1098, due to this bug could not automate"""""
# # """""""change email is not yet implemented so could not automate this
# # """"stop the app"""
# stop_app("com.zebra.soho_app")
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_47790():
#     """"Verify token refresh doesn't log app out."""
# """Couldnot automate as it is asking to keep the app ideal for more than 1 hour and check the behaviour"""""""""
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_47810():
    """"Verify recently printer labels text shouldn't overlap on theme background picture."""""
#
#
# """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
# """""Check whether App is installed or not"""
# # """"""start the app""""""
# start_app("com.zebra.soho_app")
# """""Click on hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on  home tab"""
# app_settings_page.click_Home_Tab()
# sleep(2)
# """""verify printer is already added or not"""
# app_settings_page.Verify_Printer_is_already_added()
# sleep(1)
# """""""verify recently printed labels is present"""""""
# app_settings_page.Is_Present_Recently_Printed_Labels_Text()
# """""""verify first recent lebel is present"""""""
# app_settings_page.Is_Present_Firstone_In_Recently_Printed_Label()
# """click on the first recently present label"""
# app_settings_page.click_Firstone_In_Recently_Prtinted_Label()
# sleep(3)
# stop_app("com.zebra.soho_app")
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_47820():
#     """"Verify ZSB app home page (overview page) should scroll to the bottom of the list in Recently Printed Labels"""""
#
#
# """"Precondition:""
# 1. Install the latest production app on the tablet
# 2. Prepare a production with printer added and sign in
# 3. There are 6 Recently Printed Lables present in account"""""

# """""""start the app"""""""
# start_app("com.zebra.soho_app")
# login_page.click_Menu_HamburgerICN()
# """"click on  home tab"""
# app_settings_page.click_Home_Tab()
# sleep(2)
# """""verify printer is already added or not"""
# app_settings_page.Verify_Printer_is_already_added()
# sleep(1)
# """""""verify recently printed labels is present"""""""
# app_settings_page.Is_Present_Recently_Printed_Labels_Text()
# """""""verify first recent lebel is present"""""""
# app_settings_page.Is_Present_Firstone_In_Recently_Printed_Label()
# poco.scroll()
# """"Verify buy more labels is present"""
# app_settings_page.Is_Present_Buy_More_Labels()
# sleep(3)
# stop_app("com.zebra.soho_app")
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_AppSettings_TestcaseID_47825():
#     """""Verify ZSB app doesn't shows error as "Logout failed. Please try logging out again"."""""
#
#
# """Precondition:
# 1. Registered a production user
# 2. Install production Mobile App into test device"""
#
# """""""start the app"""""""
# start_app("com.zebra.soho_app")
# sleep(3)
# """""click on hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """""click on the pen icon near to user name"""
# app_settings_page.click_pen_Icon_near_UserName()
# """Verify User settings text is present"""
# app_settings_page.Is_Present_User_Settings_Text()
# """"Scroll till the delete button"""
# app_settings_page.Scroll_till_Delete_Account()
# """"Verify Logout button"""
# app_settings_page.Is_Present_Logout_Btn()
# """"click on the delete account button"""
# app_settings_page.click_Delete_Account_Btn()
# """"Verify Delete account text is present"""
# app_settings_page.verify_Delete_Account_Text()
# """verify Please Acknowledge text is present"""""
# app_settings_page.verify_Please_Acknowledge_Text()
# """""verify & click on first checkbox """
# app_settings_page.click_First_Checkbox()
# """""verify & click on second checkbox """
# app_settings_page.click_Second_Checkbox()
# """""verify & click on third checkbox """
# app_settings_page.click_Third_Checkbox()
# """verify security message text is present"""""
# app_settings_page.verify_Security_Message_Text()
# """click on cancel button"""
# app_settings_page.click_Cancel_Btn()
# """verify setting text is present"""
# app_settings_page.Is_Present_User_Settings_Text()
# """"verify & click on delete account button"""
# app_settings_page.click_Delete_Account_Btn()
# """""verify & click on first checkbox """
# app_settings_page.click_First_Checkbox()
# """""verify & click on second checkbox """
# app_settings_page.click_Second_Checkbox()
# app_settings_page.click_Third_Checkbox()
# """"click on the confirm button to delete the account"""
# app_settings_page.click_Confirm_Btn_To_DeleteAccount()
# """"verify zebra logo is present"""
# app_settings_page.Is_Present_Zebra_Logo()
# """verify ZSB printer image is displaying"""""
# app_settings_page.Is_Present_ZSB_Printer_Icon()
# """""Verify login page Important messsage text"""
# app_settings_page.Verify_Login_Page_Important_Message_Text()
# """click on login button"""
# login_page.click_loginBtn()
# """""""select the login with google option"""""""""
# app_settings_page.click_Continue_with_Google()
# """"if automatically google login issue is fixed then uncomment the belo codes, we need to change the code """
# """"verify delete account pop up message"""
# app_settings_page.Is_Present_Delete_Account_Popup()
# """"click on cancel button on the pop up"""
# app_settings_page.click_Cancel_on_Delete_Account_Popup()
# """"verify settings text is displaying"""
# app_settings_page.Is_Present_User_Settings_Text()
# """""stop the app"""
# stop_app("com.zebra.soho_app")
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_47879():
#     """""Verify typo and guide message is correct on Searching For your printer page."""""
#
#
# """Precondition:
# 1. Registered a production user
# 2. Install production Mobile App into test device"""""
#
# """""""start the app"""""""
# start_app("com.zebra.soho_app")
# sleep(3)
# """"click on hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """""click on Add a printer"""
# add_a_printer_screen.click_Add_A_Printer()
# """""click on start Button"""
# add_a_printer_screen.click_Start_Button()
# # #""""screen freeze to verify all the elements"""
# # #app_settings_page.screen_freeze_for_30_seconds()
# """"verify searching for your printer text"""
# add_a_printer_screen.Verify_Searching_for_your_printer_Text()
# """"verify printer led not flashing text"""
# add_a_printer_screen.Verify_Printer_LED_Not_Flashing_Text()
# """Verify to find your printer text"""
# add_a_printer_screen.Verify_To_Find_Your_Printer_Text()
# """""stop the app"""
# stop_app("com.zebra.soho_app")

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#
# def test_AppSettings_TestcaseID_47880():
#     """""Verify "Done" Button and text "LED light Behavior Support" position is correct in Printer LED Guide dialog."""""
#
#
# """start the app"""
# start_app("com.zebra.soho_app")
# sleep(3)
# """"click on hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """click on add a printer"""
# add_a_printer_screen.click_Add_A_Printer()
# """click on start button"""
# add_a_printer_screen.click_Start_Button()
# """verify searching for your printer text"""
# add_a_printer_screen.Verify_Searching_for_your_printer_Text()
# """"click on printer led not flashing link"""
# add_a_printer_screen.click_Printer_LED_Not_Flashing_Link()
# """"verify led light behaviour support text"""
# add_a_printer_screen.Verify_LED_Light_Behavior_Support_Text()
# """"verify the position of all the buttons"""
# add_a_printer_screen.Verify_the_Position_of_all_the_Buttons()
# """click on the printer led guide done button"""
# add_a_printer_screen.click_Printer_LED_Guide_Done_Btn()
# """"stop the app"""
# stop_app("com.zebra.soho_app")


# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# need to add id for 2 steps in the last
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_AppSettings_TestcaseID_47881():
#     """""Verify "How to Unpair Bluetooth" dropdown list should expend with small size screen device."""""
#
#
# """"Precondition:
# 1. Registered a production user
# 2. Install production Mobile App into test device
# 3. Login Mobile App with user already added printer"""""

# """start the app"""
# start_app("com.zebra.soho_app")
# sleep(3)
# """"verify home text is displaying on the home screen"""
# app_settings_page.Home_text_is_present_on_homepage()
# """click on three dot on added printer on home page"""
# app_settings_page.click_Three_Dot_On_Added_Printer_On_HomePage()
# """""click on delete printer button"""
# app_settings_page.click_Delete_Printer_Button()
# """verify delete printer page"""
# app_settings_page.Verify_Delete_Printer_Page()
# """"click delete printer button"""
# app_settings_page.click_Delete_Printer_Button()
# """"verify final delete printer text"""
# app_settings_page.Verify_Final_Delete_Printer_Text()
# """"click yes delete button"""
# app_settings_page.click_Yes_Delete_Button()
# """click on unpair bluetooth dropdown list"""""
# app_settings_page.Verify_And_click_Unpair_Bluetooth_dropdown_list()
# """"verify UI of unpair bluetooth dropdown list """
# app_settings_page.Verify_UI_Of_Unpair_Bluetooth_dropdown_list()
# """"stop the app"""
# stop_app("com.zebra.soho_app")
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# """"Already added in Others subarea""""""""""""""""""""""""""""""""""""""""""""""""""
# def test_AppSettings_TestcaseID_47910():
#     """""Verify pull-down screen twice then the prints left value can refresh success in home page."""""
#
# """start the app"""
# start_app("com.zebra.soho_app")
# sleep(3)
# app_settings_page.Verify_Printer_is_already_added()
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_47911():
#     """ Verify auto Label Feed On Printer Cover Close value doesn't retrieve in progress after changing darkness level."""
#
#
# """start the app"""
# start_app("com.zebra.soho_app")
# sleep(3)
# """"verify printer is already added"""
# app_settings_page.Verify_Printer_is_already_added()
# """click on the hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on Printer settings tab"""
# app_settings_page.click_Printer_Settings()
# """"click on printer name on the printer settings page"""
# app_settings_page.click_PrinterName_On_Printersettings()
# """verify general tab text"""
# app_settings_page.Verify_General_Tab_Text()
# """"verify printer name text"""
# app_settings_page.Verify_Printer_Name_Text()
# """verify darkness level bar is present & change the darkness level"""
# app_settings_page.Verify_Darkness_Level_Bar()
# """"change the darkness level"""
# app_settings_page.Change_Darkness_Level_Bar()
# """verify the darkness updated message"""
# app_settings_page.Verify_Darkness_Updated_Message()
# """Verify auto Label Feed On Printer Cover Close value enable/disable option"""
# app_settings_page.Check_toggle_button()
# """click on the toggle button"""
# app_settings_page.click_toggle_button()
# """"stop the app"""
# stop_app("com.zebra.soho_app")


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_47913():
#     """Verify ZSB app doesn't stuck in Printer registration process when there is a network drop."""
#
#
# """start the app"""
# start_app("com.zebra.soho_app")
# sleep(3)
# """click on the hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on add a printer"""
# add_a_printer_screen.click_Add_A_Printer()
# """"click on start button"""
# add_a_printer_screen.click_Start_Button()
# """verify searching for your printer text"""
# add_a_printer_screen.Verify_Searching_for_your_printer_Text()
# """"Verify Select your printer text"""
# add_a_printer_screen.Verify_Select_your_printer_Text()
# """click on the printer name to select the printer"""
# add_a_printer_screen.Click_The_Printer_Name_To_Select()
# """click on select button"""
# add_a_printer_screen.click_Select_Button()
# """""verify pairing your printer text"""
# add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
# """""""Allow Bluetooth pairing popup 1 & 2"""""""
# add_a_printer_screen.click_Bluetooth_pairing_Popup1()
# add_a_printer_screen.click_Bluetooth_pairing_Popup2()
# """"Searching for wifi networks text is displaying"""
# add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
# """""Click on select different Network"""
# add_a_printer_screen.click_Select_Different_Network()
# """click on zebra network"""
# add_a_printer_screen.click_Zebra_Network()
# """"enter password"""""
# add_a_printer_screen.Enter_Password()
# poco(name="Submit").click()
# poco(name="Connecting to Wi-Fi Network").exists()
# sleep(7)
# poco(name="Registering your Printer").exists()
# poco(name="Connected!").exists()
# poco(name="Finish Setup").click()
# sleep(3)
# """"stop the app"""
# stop_app("com.zebra.soho_app")
# """""""""done"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_47914():
#     """Android Only- Verify there is no unknown printer appeared in the Bluetooth list."""
#
#
# """start the app"""
# start_app("com.zebra.soho_app")
# sleep(3)
# """"verify home text is displaying on the home screen"""
# app_settings_page.Home_text_is_present_on_homepage()
# """click on the hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on add a printer"""
# add_a_printer_screen.click_Add_A_Printer()
# """"click on start button"""
# add_a_printer_screen.click_Start_Button()
# """"Verify Select your printer text"""
# add_a_printer_screen.Verify_Select_your_printer_Text()
# """"Verify Discovered Devices Text is present"""
# add_a_printer_screen.Verify_Discovered_Devices_Text()
# """Verify the list of printers details displaying"""
# add_a_printer_screen.Verify_same_ZSB_image_for_all_items()
# """"stop the app"""
# stop_app("com.zebra.soho_app")
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_47915():
#     """Printer Bluetooth List displays printers which have already been added even if "Show All Printers" is not selected."""
# """start the app"""
# start_app("com.zebra.soho_app")
# sleep(3)
# """"verify home text is displaying on the home screen"""
# app_settings_page.Home_text_is_present_on_homepage()
# """click on the hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on add a printer"""
# add_a_printer_screen.click_Add_A_Printer()
# """"click on start button"""
# add_a_printer_screen.click_Start_Button()
# """"Verify Select your printer text"""
# add_a_printer_screen.Verify_Select_your_printer_Text()
# """click on Show all printers"""
# add_a_printer_screen.click_Show_All_Printers()
# """Verify the already added printer is not displaying"""
# # add_a_printer_screen.Verify_Already_Added_Printer_IS_Not_Displaying()
# """"stop the app"""
# common_method.Stop_The_App()
# # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



# def test_AppSettings_TestcaseID_47917():
#         """Verify Printer’s name is too long which should not causes app get stuck and style error at Printer Settings page."""
#
# """start the app"""
# common_method.Start_The_App()
# sleep(3)
# """"verify home text is displaying on the home screen"""
# app_settings_page.Home_text_is_present_on_homepage()
# """click on the hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on printer settings tab"""""
# app_settings_page.click_Printer_Settings()
# app_settings_page.click_PrinterName_On_Printersettings()
# app_settings_page.click_Printer_Name_Text_Field()
# app_settings_page.clear_First_Name()
# """Rename the Printer Name with a long text (more than 30 characters)"""
# app_settings_page.Rename_PrinterName_With30_Characters()
# app_settings_page.click_Back_Icon()
# app_settings_page.Verify_Exceeding_Characters_Message()
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_Printer_Settings()
# app_settings_page.click_PrinterName_On_Printersettings()
# app_settings_page.click_Printer_Name_Text_Field()
# app_settings_page.clear_First_Name()
# app_settings_page.Update_PrinterName()
# app_settings_page.click_Back_Icon()
# common_method.Stop_The_App()
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_47923():
#     """Verify changing password should log out all clients."""

# common_method.Open_Google_Search_for_ZSBApp()
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



# def test_AppSettings_TestcaseID_47924():
#     """Verify Should not allow same printer name in all the clients.."""
# """start the app"""
# common_method.Start_The_App()
# sleep(3)
# """"verify home text is displaying on the home screen"""
# app_settings_page.Home_text_is_present_on_homepage()
# """click on the hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on printer settings tab"""""
# app_settings_page.click_Printer_Settings()
# app_settings_page.click_PrinterName_On_Printersettings()
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



# def test_AppSettings_TestcaseID_50031():
#     """Check the error message prompted when print test page and printer head open or offline"""
#
# """start the app"""
# common_method.Start_The_App()
# sleep(3)
# """"verify home text is displaying on the home screen"""
# app_settings_page.Home_text_is_present_on_homepage()
# """click on the hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on printer settings tab"""""
# app_settings_page.click_Printer_Settings()
# """"click on printer name on printyer settings page"""
# app_settings_page.click_PrinterName_On_Printersettings()
# """verify printer name text"""
# app_settings_page.Verify_Printer_Name_Text()
# """click test print button"""
# app_settings_page.click_Test_Print_Button()
# """"Verify Printed successfully text"""
# app_settings_page.Verify_Printed_Successfully_Text()
# """click test print button"""
# app_settings_page.click_Test_Print_Button()
# """"Open the printer cover manually"""
# """""verify error message of cover open"""
# app_settings_page.Verify_ErrorMessage_Text()
# common_method.Stop_The_App()
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_50333():
#     """Android only- Check it will back to manage network after clicking device’s back button""""""
# """"App should be in logged in condition & printer should be added""""
#
# ""start the app"""
# common_method.Start_The_App()
# """click on the hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on the printer settings tab"""
# app_settings_page.click_Printer_Settings()
# """click on the printer name"""
# app_settings_page.click_PrinterName_On_Printersettings()
# """"click on the wifi tab"""
# app_settings_page.click_wifi_tab()
# """click on the Manage network button"""
# app_settings_page.click_Manage_Networks_Btn()
# """"verify bluetooth connection required text"""
# app_settings_page.get_text_Bluetooth_connection_required_Txt()
# """click on keyboard back icon"""
# app_settings_page.click_Keyboard_back_Icon()
# """""Due to bug id SMBM-2243, step 5 is blocked"""
# """"verify bluetooth connection failed pop up"""
# app_settings_page.Verify_Bluetooth_Connection_Failed_Popup()
# """""click keyboard back icon"""
# app_settings_page.click_Keyboard_back_Icon()
# """"verify wifi tab & text is present"""
# app_settings_page.Verify_Wifi_Tab_Text()
# """stop the app"""""
# common_method.Stop_The_App()
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_51702():
#     """Check the UI of toggle buttons on Notification Settings""""""
# """"App should be in logged in condition & printer should be added""""
#
# ""start the app"""
# common_method.Start_The_App()
# """click on the hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on Notifications Tab"""
# app_settings_page.click_Notifications_Tab()
# """"Scroll till Notification Settings Tab"""
# app_settings_page.Scroll_Till_Notification_Settings_Tab()
# """click on notification settings tab"""
# app_settings_page.click_Notification_Settings_Tab()
# """"verify notification settings toggle buttons and text"""
# app_settings_page.Verify_NotificationSettings_Toggle_Buttons_Text_Present()
# """"scroll till messages tab"""
# app_settings_page.Scroll_Till_Messages_Tab()
# """""click Messages tab"""
# app_settings_page.click_Mesages_Tab()
# """verify messages text and toggle button"""
# app_settings_page.Verify_Messages_Text_And_Toggle_Buttons()
# """"click on hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """click on three dot icon"""
# app_settings_page.click_Three_Dot_On_Workspace()
"""""click change theme"""
app_settings_page.click_Change_Theme()
""""click on electic theme to change the theme"""
app_settings_page.check_Change_Electic_Theme()
"""click on save & exit"""
app_settings_page.click_Save_Exit_Btn()
"""verify notifications text is displaying"""
app_settings_page.Verify_Notifications_Text_IS_Displaying()
""""verify updated messages tab color"""
app_settings_page.Verify_Updated_MessagesTab_Color()
"""scroll right till Notification settings"""
app_settings_page.Scroll_Right()
"""click on Notification Settings tab"""
app_settings_page.click_Notification_Settings_Tab()
"""verify updtaed Notification settings messages"""
app_settings_page.Verify_Updated_Notifications_SettingsTab_Messages_Color()
"""click on hamburger menu"""
login_page.click_Menu_HamburgerICN()
"""click on three dot icon"""
app_settings_page.click_Three_Dot_On_Workspace()
"""click on change theme"""
app_settings_page.click_Change_Theme()
""""click on change modern theme"""
app_settings_page.check_Change_Modern_Theme()
"""click on dsave & exit button"""
app_settings_page.click_Save_Exit_Btn()
"""stop the app"""""
common_method.Stop_The_App()
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_51705():
#     """Check clicking the photo taken by camera will not affect uploading photo as user avatar""""""
# """"App should be in logged in condition & printer should be added""""
#
# ""start the app"""
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_pen_Icon_near_UserName()
# app_settings_page.Is_Present_User_Settings_Text()
# app_settings_page.click_upload_photo()
# app_settings_page.click_Mobile_Camera()
# app_settings_page.Click_Allow_popup()
#
# om.google.android.GoogleCamera:id/shutter_button



# def test_AppSettings_TestcaseID_51788():
#     """Check clicking the photo taken by camera will not affect uploading photo as user avatar""""""
# """"App should be in logged in condition & printer should be added""""
#
# ""start the app"""
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_pen_Icon_near_UserName()
# app_settings_page.Scroll_till_Delete_Account()
# app_settings_page.click_Logout_Btn()
# login_page.click_loginBtn()
# login_page.click_Login_With_Email_Tab()
# login_page.click_UserName_TextField()
# login_page.Enter_UserName()
# login_page.click_Password_TextField()
# login_page.Enter_Password()
# login_page.click_SignIn_Button()
# login_page.click_loginBtn()


