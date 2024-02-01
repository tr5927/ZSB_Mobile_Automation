from airtest.core.api import connect_device, auto_setup, start_app, sleep, text, stop_app
from poco.drivers.ios import iosPoco
from self import self

from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_iOS import App_Settings_Screen_iOS
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_iOS import Add_A_Printer_Screen_iOS
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_iOS import Login_Screen_iOS


class iOS_App_Settings:
    pass


uuid = "00008101-00051D400144001E"
Bonding = connect_device("ios:///http+usbmux://" + uuid)
poco = iosPoco(device=Bonding)

auto_setup(logdir="./", compress=3,
           devices=[f"ios:///http+usbmux://{uuid}"])
start_app("com.zebra.soho")
sleep(3)

login_screen_ios = Login_Screen_iOS(poco)
app_settings_page_ios = App_Settings_Screen_iOS(poco)
add_a_printer_page_ios = Add_A_Printer_Screen_iOS(poco)

# def test_AppSettings_TestcaseID_45688():
#     """""""""Verify Wifi Settings"""""
#
#
# """""Install the latest production app on the phone & printer should be added"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""
#
# login_screen_ios = Login_Screen_iOS(poco)
# app_settings_page_ios = App_Settings_Screen_iOS(poco)

# start_app("com.zebra.soho")
# login_screen_ios.clcik_Login_Btn()
# login_screen_ios.click_Continue_Btn()
# sleep(4)
# """""select the login with google option"""
# login_screen_ios.click_Loginwith_Google()
# sleep(2)
# """""""provide google user id & password if it is a fresh installation"""
# login_screen_ios.click_GoogleID_Field()
# sleep(2)
# login_screen_ios.click_Enter_Password_Field()
# sleep(2)
# # login_screen_ios.Enter_Google_Password()
# """"enter the password"""
# poco(text("Swdvt@#123"))
# sleep(4)
# """""""sometimes Next is not displaying"""""""
# # login_screen_ios.click_Password_Nextbtn()
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# login_screen_ios.click_Menu_HamburgerICN()
# """""click on the printer settings tab"""
# app_settings_page_ios.click_Printer_Settings()
# sleep(4)
# """""click on the printer tab"""
# app_settings_page_ios.click_PrinterName_On_Printersettings()
# sleep(3)
# """"Verify the Test print button text & tab"""
# app_settings_page_ios.Test_Print_button_is_present_on_printer_settings_page()
# # """""""""""" click on the wifi tab option""""""""""""
# app_settings_page_ios.click_wifi_tab()
# # sleep(3)
# """""""""validate the Current network text"""""
# app_settings_page_ios.test_CurrentNetwork_Txt_is_present_on_printer_settings_page()
# """""""Validate the Network status text is present on the printer settings screen"""""""
# app_settings_page_ios.test_Network_Status_Txt_is_present_on_printer_settings_page()
# """"validate network status result text on the printer settings screen"""
# app_settings_page_ios.get_text_Network_Status_Result_Txt()
# # """""""" Verify IP address text is present on the printer settings screen"""""""
# app_settings_page_ios.get_text_IPAddress_Txt()
# # """""""" Verify IP address result text"""""""
# app_settings_page_ios.get_text_IPAddress_Result_Txt()
# # """"""""Verify the message You can save upto 5 network profiles to your saved networks after Manage Networks"""
# app_settings_page_ios.IS_Present_Save_Network_Message_Txt()
# """""""verify manage networks text is present & clickable"""""""
# sleep(2)
# app_settings_page_ios.click_Manage_Networks_Btn()
# sleep(2)
# """""""""""""Click on continue button on the Bluetooth Connection required popup"""""""
# app_settings_page_ios.accept_Continue_popup()
# """""""""Verify the Cancel button on the Bluetooth_Connection_Failed_Popup"""""
# sleep(20)
# app_settings_page_ios.Cancel_is_present_on_Bluetooth_Connection_Failed_Popup()
# """""""verify the continue button and click on that"""""""
# app_settings_page_ios.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
# sleep(4)
# """""""Verify the red remove icon next to the network name"""""
# app_settings_page_ios.click_Red_Icon_to_remove_network()
# sleep(5)
# """"""""Verify the Add Network text & button & click on that"""""""""""""""""
# app_settings_page_ios.click_Add_Network()
# sleep(3)
# """""""""""""Verify Add network page is opening and verify the text"""""""
# app_settings_page_ios.get_text_Add_Network()
# """""""select the previously deleted network"""
# app_settings_page_ios.click_deleted_network()
# sleep(3)
# """""""""validate the Current network text"""""
# app_settings_page_ios.test_CurrentNetwork_Txt_is_present_on_printer_settings_page()
# """""7 to 10 need to check on Web portal"""
# stop_app("com.zebra.soho")
# # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_45689():
#     """""""""Check Change Theme Function Works"""""
#
#
# """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
# """""Check whether App is installed or not"""
# # """"""start the app""""""
# start_app("com.zebra.soho")
# sleep(5)
# # """"""""click hamburger menu""""""
# login_screen_ios.click_Menu_HamburgerICN()
# # """"""""click three dot on workspace""""
# app_settings_page_ios.click_Three_Dot_On_Workspace()
# """""""verify edit text"""""""
# app_settings_page_ios.get_text_Edit_Txt()
# # """"click on change theme"""
# app_settings_page_ios.click_Change_Theme()
# # # """""verify change theme page pop ups by verifying the change theme header"""
# app_settings_page_ios.get_text_Change_Theme_Header()
# sleep(1)
# """""""change 5 theme and check it should get saved and then need to tap on exit"""""""
# app_settings_page_ios.check_Change_Electic_Theme()
# sleep(3)
# # """""click save & exit button"""
# app_settings_page_ios.click_Save_Exit_Btn()
# # """""""SMBM-986 is still present """""""
# # """"""""After applying the theme check whether it is navigating back to home page not verifying the background image as there is no element present """"""z
# sleep(3)
# app_settings_page_ios.Home_text_is_present_on_homepage()
# """""click on hamburger icon on home page"""
# login_screen_ios.click_Menu_HamburgerICN()
# sleep(4)
# """"click on three dot icon on workspace"""""
# app_settings_page_ios.click_Three_Dot_On_Workspace()
# """"click on change theme"""
# app_settings_page_ios.click_Change_Theme()
# """""check Bohemian theme"""
# sleep(3)
# app_settings_page_ios.check_Change_Bohemian_Theme()
# sleep(3)
# # """""click save & exit button"""
# app_settings_page_ios.click_Save_Exit_Btn()
# sleep(3)
# app_settings_page_ios.Home_text_is_present_on_homepage()
# """""click on hamburger icon on home page"""
# login_screen_ios.click_Menu_HamburgerICN()
# sleep(4)
# """"click on three dot icon on workspace"""""
# app_settings_page_ios.click_Three_Dot_On_Workspace()
# """"click on change theme"""
# app_settings_page_ios.click_Change_Theme()
# """""check Professional theme"""
# poco.scroll()
# sleep(3)
# app_settings_page_ios.check_Change_Professional_Theme()
# sleep(3)
# # """""click save & exit button"""
# app_settings_page_ios.click_Save_Exit_Btn()
# sleep(3)
# app_settings_page_ios.Home_text_is_present_on_homepage()
# """""click on hamburger icon on home page"""
# login_screen_ios.click_Menu_HamburgerICN()
# sleep(4)
# """"click on three dot icon on workspace"""""
# app_settings_page_ios.click_Three_Dot_On_Workspace()
# """"click on change theme"""
# app_settings_page_ios.click_Change_Theme()
# """""check Maker theme"""
# poco.scroll()
# poco.scroll()
# sleep(3)
# app_settings_page_ios.check_Change_Maker_Theme()
# sleep(3)
# # """""click save & exit button"""
# app_settings_page_ios.click_Save_Exit_Btn()
# sleep(3)
# """"""""
# app_settings_page_ios.Home_text_is_present_on_homepage()
# """""click on hamburger icon on home page"""
# login_screen_ios.click_Menu_HamburgerICN()
# sleep(4)
# """"click on three dot icon on workspace"""""
# app_settings_page_ios.click_Three_Dot_On_Workspace()
# """"click on change theme"""
# app_settings_page_ios.click_Change_Theme()
# """""check Modern theme"""
# sleep(3)
# app_settings_page_ios.check_Change_Modern_Theme()
# sleep(3)
# # """""click save & exit button"""
# app_settings_page_ios.click_Save_Exit_Btn()
# sleep(3)
# app_settings_page_ios.Home_text_is_present_on_homepage()
# stop_app("com.zebra.soho")
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_45690():
#     """""""""Update Unit of Measure in Mobile App, check it will sync to Web Portal and Printer Tools"""""
#
#
# """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
# """""Check whether App is installed or not"""
#
# """""start the app"""
# start_app("com.zebra.soho")
# sleep(5)
# # """"""""click hamburger menu""""""
# login_screen_ios.click_Menu_HamburgerICN()
# """"click on the pen icon near the user name"""
# app_settings_page_ios.click_pen_Icon_near_UserName()
# sleep(1)
# poco.scroll()
# # """"""""verify units of measurement text is present or not""""""
# app_settings_page_ios.check_If_Units_of_Measurements_Is_Present()
# """""""verify  Inches is the by default value is displaying"""""""
# app_settings_page_ios.Inches_is_displaying()
# # """"""""click on Units of measurements""""""
# app_settings_page_ios.click_Units_of_Measurements()
# sleep(2)
# # """"""""Verify all the available values""""""
# app_settings_page_ios.verify_Milimetres_Is_Present()
# app_settings_page_ios.verify_Centimetres_Is_Present()
# app_settings_page_ios.verify_Inches_Is_Present()
# sleep(2)
# """"click on Centimeters option"""
# app_settings_page_ios.click_Centimeters()
# sleep(1)
# # """"""""verify the updated message popup""""""
# app_settings_page_ios.verify_updated_msg()
# # """""""Click on the hamburger icon"""""""
# sleep(2)
# login_screen_ios.click_Menu_HamburgerICN()
# """""click on the home tab"""
# app_settings_page_ios.click_Home_Tab()
# sleep(2)
# """""""""verify printer details, everything should display in centimeters"""""
# app_settings_page_ios.verify_printer_details_in_Centimeters()
# sleep(2)
# login_screen_ios.click_Menu_HamburgerICN()
# """""click on my design tab"""
# app_settings_page_ios.click_My_Design()
# sleep(4)
# """""verify the design size under my design"""
# app_settings_page_ios.verify_My_Details_Design_in_Centimeters()
# login_screen_ios.click_Menu_HamburgerICN()
# app_settings_page_ios.click_pen_Icon_near_UserName()
# sleep(1)
# poco.scroll()
# app_settings_page_ios.click_Units_of_Measurements()
# sleep(2)
# app_settings_page_ios.click_Inches()
# sleep(2)
# """""stop the app"""
# stop_app("com.zebra.soho")
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_45691():
#     """""""""Edit Workspace - upload and remove image"""""
#
#
# """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
# """""Check whether App is installed or not"""
#
# """"start the app"""""
# start_app("com.zebra.soho")
# login_screen_ios.click_Menu_HamburgerICN()
# app_settings_page_ios.click_Three_Dot_On_Workspace()
# app_settings_page_ios.click_Edit_Txt()
# sleep(2)
# """""verify the Edit workspace text"""
# app_settings_page_ios.get_text_Edit_Workspace()
# # """"""click upload photo""""""
# app_settings_page_ios.click_upload_photo()
# sleep(2)
# # """""click on the 1st image"""
# app_settings_page_ios.click_First_Image()
# sleep(2)
# """click on the save & exit"""
# app_settings_page_ios.click_Save_Exit_Btn()
# sleep(2)
# app_settings_page_ios.click_Three_Dot_On_Workspace()
# app_settings_page_ios.click_Edit_Txt()
# sleep(2)
# app_settings_page_ios.click_Remove_Image()
# app_settings_page_ios.Is_Present_Profile_Avatar_Letter()
# sleep(2)
# app_settings_page_ios.click_upload_photo()
# sleep(1)
# app_settings_page_ios.click_Back_Icon()
# sleep(2)
# app_settings_page_ios.click_Save_Exit_Btn()
# sleep(2)
# """""stop the app"""
# stop_app("com.zebra.soho")
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_45692():
#     """""""""Edit Workspace - Update workspace name"""""
#
#
# """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
#
# """""Check whether App is installed or not"""
# # """"""""""""start the app"""""""""""""
# start_app("com.zebra.soho")
# sleep(3)
# login_screen_ios.click_Menu_HamburgerICN()
# app_settings_page_ios.click_Three_Dot_On_Workspace()
# app_settings_page_ios.click_Edit_Txt()
# sleep(2)
# """""verify the Edit workspace text"""
# app_settings_page_ios.get_text_Edit_Workspace()
# """"Verify Workspace Name Text"""
# sleep(2)
# app_settings_page_ios.Is_Present_Workspace_Name_Text()
# # """"""""click on workspace name""""
# app_settings_page_ios.click_Workspace_Name_Text_Field()
# """""clear workspace name text field"""
# app_settings_page_ios.Clear_Workspace_Name()
# sleep(2)
# """"Click on keyboard back icon"""
# app_settings_page_ios.click_Keyboard_back_Icon()
# # """"""""""""""""""Verify save & exit option is not there""""""""""""""
# # app_settings_page.Verify_SaveExit_Option_Is_Not_There()
# """""click on back icon on edit workspace"""
# app_settings_page_ios.click_back_Icon_On_Edit_Workspace()
# app_settings_page_ios.click_Three_Dot_On_Workspace()
# app_settings_page_ios.click_Edit_Txt()
# sleep(2)
# # """"""""Check the previous Workspace name is displaying""""""
# app_settings_page_ios.Is_Present_Workspace_Name()
# app_settings_page_ios.click_Workspace_Name_Text_Field()
# app_settings_page_ios.Clear_Workspace_Name()
# sleep(2)
# app_settings_page_ios.click_Workspace_Name_Text_Field()
# """"verify the workspace field by giving space """
# app_settings_page_ios.Update_Workspace_Name_With_Space()
# sleep(3)
# """"Click on keyboard back icon"""
# app_settings_page_ios.click_Keyboard_back_Icon()
# sleep(3)
# app_settings_page_ios.click_Save_Exit_Btn()
# sleep(3)
# app_settings_page_ios.click_Three_Dot_On_Workspace()
# app_settings_page_ios.click_Edit_Txt()
# app_settings_page_ios.click_Workspace_Name_Text_Field()
# app_settings_page_ios.Clear_Workspace_Name()
# sleep(2)
# """"Click on keyboard back icon"""
# app_settings_page_ios.click_Keyboard_back_Icon()
# sleep(1)
# app_settings_page_ios.click_Workspace_Name_Text_Field()
# """"verify the workspace field by special characters with more than 30 characters """
# app_settings_page_ios.Update_Workspace_Name_With_Special_Characters_with_30_characters()
# sleep(3)
# """"Click on keyboard back icon"""
# app_settings_page_ios.click_Keyboard_back_Icon()
# sleep(3)
# """""click on save & exit button"""
# app_settings_page_ios.click_Save_Exit_Btn()
# sleep(3)
# app_settings_page_ios.click_Three_Dot_On_Workspace()
# app_settings_page_ios.click_Edit_Txt()
# """"""""""Verify the workspace updated name"""""""""""""""
# app_settings_page_ios.Verify_Updated_Name()
# sleep(3)
# app_settings_page_ios.click_Workspace_Name_Text_Field()
# app_settings_page_ios.Clear_Workspace_Name()
# sleep(2)
# """"Click on keyboard back icon"""
# app_settings_page_ios.click_Keyboard_back_Icon()
# app_settings_page_ios.click_Workspace_Name_Text_Field()
# app_settings_page_ios.Update_Workspace_Name_with_Original_Name()
# sleep(3)
# app_settings_page_ios.click_Keyboard_back_Icon()
# sleep(3)
# """""click on save & exit button"""
# app_settings_page_ios.click_Save_Exit_Btn()
# sleep(3)
# """"stop the app"""
# stop_app("com.zebra.soho")
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_45705():
#     """""""""Verify account profile update for non-Zebra user"""""
#
#
# """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
# """""Check whether App is installed or not"""
#
# # """""""start the app"""""""
# start_app("com.zebra.soho")
# # """"""""click hamburger menu""""""
# login_screen_ios.click_Menu_HamburgerICN()
# """"click on the pen icon near the user name"""
# app_settings_page_ios.click_pen_Icon_near_UserName()
# """""""verify First name text is present"""""""
# app_settings_page_ios.Is_Present_First_Name_Text()
# """""""verify last name text is present"""""""
# app_settings_page_ios.Is_Present_Last_Name_Text()
# """""click first name text field"""
# app_settings_page_ios.click_First_Name_Text_Field()
# """"clear first name field"""
# app_settings_page_ios.clear_First_Name()
# """""Update first name with special characters with 30 characters"""
# app_settings_page_ios.Update_First_Name_With_Special_Characters_with_30_characters()
# sleep(3)
# """""click last name text field"""
# app_settings_page_ios.click_Last_Name_Text_Field()
# """"clear Last name field"""
# app_settings_page_ios.clear_Last_Name()
# """""Update last name with special characters with 30 characters"""
# app_settings_page_ios.Update_Last_Name_With_Special_Characters_with_30_characters()
# sleep(3)
# """""click keyboard back icon"""
# app_settings_page_ios.click_Keyboard_back_Icon()
# """"verify the updated names message"""
# app_settings_page_ios.verify_Your_changes_have_been_saved_Message()
# sleep(3)
# """""click First name text field"""
# app_settings_page_ios.click_First_Name_Text_Field()
# """"clear First name field"""
# app_settings_page_ios.clear_First_Name()
# """Update the default First name"""
# app_settings_page_ios.Update_Default_First_Name()
# sleep(3)
# """""click last name text field"""
# app_settings_page_ios.click_Last_Name_Text_Field()
# """"clear Last name field"""
# app_settings_page_ios.clear_Last_Name()
# """Update the default Last name"""
# app_settings_page_ios.Update_Default_Last_Name()
# # """"stop the app"""
# stop_app("com.zebra.soho")
# """"""change password link is not opening the correct page---SMBM-1098, due to this bug could not automate"""""
# """""""change email is not yet implemented so could not automate this
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



# def test_AppSettings_TestcaseID_47790():
#     """"Verify token refresh doesn't log app out."""
# """Couldnot automate as it is asking to keep the app ideal for more than 1 hour and check the behaviour"""""""""
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_47810():
#     """"Verify recently printer labels text shouldn't overlap on theme background picture."""""
#
#
# """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
# """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
# """""Check whether App is installed or not"""
#
# # """"""start the app""""""
# start_app("com.zebra.soho")
# """""Click on hamburger icon"""
# login_screen_ios.click_Menu_HamburgerICN()
# """"click on  home tab"""
# app_settings_page_ios.click_Home_Tab()
# sleep(2)
# """""verify printer is already added or not"""
# app_settings_page_ios.Verify_Printer_is_already_added()
# sleep(1)
# """""""verify recently printed labels is present"""""""
# app_settings_page_ios.Is_Present_Recently_Printed_Labels_Text()
# """""""verify first recent lebel is present"""""""
# app_settings_page_ios.Is_Present_Firstone_In_Recently_Printed_Label()
# """click on the first recently present label"""
# app_settings_page_ios.click_Firstone_In_Recently_Prtinted_Label()
# stop_app("com.zebra.soho")
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_47820():
#     """"Verify ZSB app home page (overview page) should scroll to the bottom of the list in Recently Printed Labels"""""

# """"Precondition:""
# 1. Install the latest production app on the tablet
# 2. Prepare a production with printer added and sign in
# 3. There are 6 Recently Printed Lables present in account"""""
#
# """""""start the app"""""""
# start_app("com.zebra.soho")
# login_screen_ios.click_Menu_HamburgerICN()
# """"click on  home tab"""
# app_settings_page_ios.click_Home_Tab()
# sleep(2)
# """""verify printer is already added or not"""
# app_settings_page_ios.Verify_Printer_is_already_added()
# sleep(1)
# """""""verify recently printed labels is present"""""""
# app_settings_page_ios.Is_Present_Recently_Printed_Labels_Text()
# """""""verify first recent lebel is present"""""""
# app_settings_page_ios.Is_Present_Firstone_In_Recently_Printed_Label()
# poco.scroll()
# """"Verify buy more labels is present"""
# app_settings_page_ios.Is_Present_Buy_More_Labels()
# stop_app("com.zebra.soho")
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_47825():
#     """""Verify ZSB app doesn't shows error as "Logout failed. Please try logging out again"."""""
#
#
# """Precondition:
# 1. Registered a production user
# 2. Install production Mobile App into test device"""
#
# """""""start the app"""""""
# start_app("com.zebra.soho")
# login_screen_ios.click_Menu_HamburgerICN()
# app_settings_page_ios.click_pen_Icon_near_UserName()
# app_settings_page_ios.click_Edit_Txt()
# app_settings_page_ios.Is_Present_Use_Settings_page()
# app_settings_page_ios.Scroll_till_Delete_Account()
# sleep(3)
# app_settings_page_ios.Is_Present_Logout_Btn()
# app_settings_page_ios.click_Delete_Account_Btn()
# sleep(3)
# app_settings_page_ios.verify_Three_Options_To_Continue()
# sleep(3)
# app_settings_page_ios.click_Cancel_Btn()
# app_settings_page_ios.Is_Present_User_Settings_Page()
# sleep(2)
# app_settings_page_ios.Scroll_till_Delete_Account()
# sleep(3)
# app_settings_page_ios.click_Delete_Account_Btn()
# app_settings_page_ios.click_Cancel_Btn()
# login_screen_ios.click_Logout()
# sleep(3)
# login_screen_ios.clcik_Login_Btn()
# login_screen_ios.click_Continue_Btn()
# sleep(4)
# """""select the login with google option"""
# login_screen_ios.click_Loginwith_Google()
# sleep(2)
# """""""provide google user id & password if it is a fresh installation"""
# login_screen_ios.click_GoogleID_Field()
# sleep(2)
# login_screen_ios.click_Enter_Password_Field()
# sleep(2)
# # login_screen_ios.Enter_Google_Password()
# """"enter the password"""
# poco(text("Swdvt@#123"))
# sleep(4)
# """""""sometimes Next is not displaying"""""""
# # login_screen_ios.click_Password_Nextbtn()
# sleep(7)
# app_settings_page_ios.Home_text_is_present_on_homepage()
# stop_app("com.zebra.soho")
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_AppSettings_TestcaseID_47879():
#     """""Verify typo and guide message is correct on Searching For your printer page."""""

# """Precondition:
# 1. Registered a production user
# 2. Install production Mobile App into test device"""""
#
# """""""start the app"""""""
# start_app("com.zebra.soho_app")
# sleep(3)
# login_screen_ios.click_Menu_HamburgerICN()
# add_a_printer_page_ios.click_Add_A_Printer()
# add_a_printer_page_ios.click_Start_Button()
# add_a_printer_page_ios.Verify_Searching_for_your_printer_Text()
# add_a_printer_page_ios.Verify_Printer_LED_Not_Flashing_Text()
# add_a_printer_page_ios.Verify_To_Find_Your_Printer_Text()
# add_a_printer_page_ios.Verify_Printer_LED_Image()
# stop_app("com.zebra.soho_app")
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
