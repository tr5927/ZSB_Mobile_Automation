#from poco import poco
import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.PageObject.Others.Others import Others
from ZSB_Mobile.Common_Method import *
import os

class test_Others():
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
#start_app("com.zebra.soho_app")
sleep(3.0)

login_page = Login_Screen(poco)
others = Others(poco)

#
#
def test_Others_TestcaseID_47972():
    pass
#
# login_page.click_Menu_HamburgerICN()
#
# sleep(1)
#
# """ Select the Printer Settings """
# others.click_Printer_Settings()
#
# others.swipe_left()
# """ Select a printer """
# others.click_selected_printer()
# sleep(2)
#
# """ Click on the icon """
# others.click_icon()
# sleep(1)
#
# """Click On the Demo video"""
# others.click_demo_video()
# sleep(5)
#
# """Close The Demo Video"""
# others.close_demo_video()
#
#
def test_Others_TestcaseID_49203():
    pass
#
# """Click On the Three dots of the Home page Printer"""
# others.click_three_dots()
#
# """Click on the Delete Button"""
# others.click_delete_button()
#
# """Verify the text image (Currently The text cannot be extracted so verifying using the name)"""
# others.verify_delete_printer_text()
#
# """Check cancel and delete button exists"""
# others.check_cancel_and_delete_button()
#
# """cancel the delete printer dialogue"""
# others.click_cancel_delete_printer()
#
#
# def test_Others_TestcaseID_47946():
#     pass
#
# """take the prvious number of cartridges"""
# previous = others.get_no_of_left_cartridge()
# print(previous)
#
# """click on navigation option"""
# login_page.click_Menu_HamburgerICN()
#
# """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
# others.click_Printer_Settings()
# others.click_selected_printer()
# sleep(2)
# n=2
#
# """test the printer to print the label"""
# for i in range(n):
#     others.click_test_print()
#     sleep(2)
#
# sleep(1)
# """Go to the Home Page"""
# login_page.click_Menu_HamburgerICN()
# others.click_home_button()
# sleep(2)
#
# """After printing Get the number of cartridges"""
# after = others.get_no_of_left_cartridge()
# print(after)
#
# """Check wheather the cartridges are updated"""
# res = others.check_auto_update_cartridge(previous,after,n)
# if res:
#     print("success")
# else:
#     print("Failed")


"""BELOW NEED TO BE COMPLETED"""


def test_Others_TestcaseID_45793():
    pass

# print("hello")
# start_app("com.google.android.googlequicksearchbox")
#
# others.click_google_search_bar()
# others.enter_the_text_in_goole("https://zsbportal.zebra.com/")
# others.click_enter()
# others.wait_for_element_appearance("Continue with Google",10)
# login_page.click_Loginwith_Google()
# sleep(4)
# login_page.click_zebra_test_850_account()

# others.wait_for_element_appearance_text("Home",10)
#
# others.click_hamburger_button_in_Google()
# sleep(2)
# others.click_Printer_Settings_in_google()
#
# others.click_hamburger_button_in_Google()
#
# others.click_selected_printer_in_google()
#
# """others.google_scroll_down()"""
# others.scroll_down_till_printer_test_label_in_google()
# sleep(1)
# n = 2
# for i in range(n):
#     others.click_google_print_test_button()
#     sleep(5)

# """others.change_Darkness_level_in_google(50)"""

# others.wait_for_element_appearance_text("Home",10)
# others.click_hamburger_button_in_Google()
#
# others.wait_for_element_appearance("Notifications",5)
#
# others.click_notifications_button_in_google()
# others.click_hamburger_button_in_Google()
# res = others.check_text_history()
# if not res:
#     others.scroll_up(1)
#"""Clear The Notifications in google if present"""
# google_notification = others.get_notification_text_in_google()
#
# print(google_notification)
# sleep(2)


# start_app("com.zebra.soho_app")
# others.wait_for_element_appearance("Home",15)
# sleep(2)
#
# login_page.click_Menu_HamburgerICN()
# others.click_notifications_button()
#
# Android_notification = others.get_notification_text_in_Android()
# sleep(3)
#
# res = others.verify_notifications(google_notification,Android_notification)
# print(res)


def test_Others_TestcaseID_45874():
    pass

# """Mention the vesrion number expected"""
# expected_version_no = "1.4.4619"
#
# """click on the hamburger icon"""
# login_page.click_Menu_HamburgerICN()
#
# """get the version number of the current device"""
# actual_version_no = others.get_the_version_no()
#
# """If vesrion number not same generate error"""
# if expected_version_no!=actual_version_no:
#     raise Exception("Vesrion no did not match")

def test_Others_TestcaseID_47955():
    pass

# # login_page.click_Menu_HamburgerICN()
# # others.click_Printer_Settings()
# names, id = others.get_printer_names()
# others.select_printer_1(id[1])
# others.rename_printer(id[1],names[2])
# sleep(2)
# res = others.verify_text_update_printer_name()
#
# print(res)
# # if res:
# #     print("ok")
# # else:
# #     raise Exception("text dint match")

def test_Others_TestcaseID_45798():
    pass

# login_page.click_Menu_HamburgerICN()
# """Click on the profile edit"""
# others.click_on_profile_edit()
#
# """verify the default image"""
# res = others.verify_default_image()
# if not res:
#     raise Exception("default image not found")
#
# """select upload photo gallery"""
# others.click_upload_photo()
#
# """select photo gallery"""
# others.select_photo_gallery()
#
# others.go_back()
# others.go_back()
# sleep(3)
#
# """verify the default image"""
# res = others.verify_default_image()
# if not res:
#     raise Exception("default image not found")
#
# """Select Camera upload"""
# others.click_upload_photo()
# others.select_camera()
#
# others.go_back()
# others.go_back()
#
# """verify the default image"""
# res = others.verify_default_image()
# if not res:
#     raise Exception("default image not found")
#


def test_Others_TestcaseID_47945():
    pass

# login_page.click_Menu_HamburgerICN()
# others.click_Printer_Settings()
#
# names, id = others.get_printer_names()
# others.select_printer_1(id[1])
#
# others.rename_printer(id[1],"")
# others.click_enter()
#
# res = others.get_null_name_error_and_space_for_printer_name()
# if res:
#     print("ok")
# else:
#     raise Exception("null value accepted")
#
# others.rename_printer(id[1],"    ")
# others.click_enter()
#
# if res:
#     print("ok")
# else:
#     raise Exception("Space  accepted")


def test_temp_2():
    pass

# print("hello")
# start_app("com.google.android.googlequicksearchbox")
#
# others.click_google_search_bar()
# others.enter_the_text_in_goole("https://zsbportal.zebra.com/")
# others.click_enter()
# sleep(5)
# login_page.click_Loginwith_Google()
# sleep(4)
# login_page.click_zebra_test_account()
# sleep(5)
# others.click_hamburger_button_in_Google()
# sleep(2)
# others.click_edit_profile_in_google()
# sleep(1)
# others.click_hamburger_button_in_Google()
# sleep(1)
#
# others.verify_default_image()
#
# """PASS First letter of first name and last name as parameters with space"""
# res = others.verify_default_image_in_google("Z T")
# if not res:
#     raise Exception("default image not found")



def test_Others_TestcaseID_45796():
    pass

# login_page.click_Menu_HamburgerICN()
# others.click_on_profile_edit()
#
# res = others.verify_default_image()
# if not res:
#     raise Exception("default image not found")
#
# res = others.check_remove_image_button_exists()
# if res:
#     raise Exception("Remove image button found")
#
# others.click_upload_photo()
# others.select_photo_gallery()
#
# others.select_first_image_from_gallery()
# sleep(3)
# res = others.verify_default_image()
# if res:
#     raise Exception("default image found")
#
# res = others.check_remove_image_button_exists()
# if not res:
#     raise Exception("Remove image button not found")
#
# others.click_remove_image_button()
# sleep(2)
# res = others.verify_default_image()
# if not res:
#     raise Exception("default image not found")



def test_Others_TestcaseID_45797():
    pass

# login_page.click_Menu_HamburgerICN()
# others.click_on_profile_edit()
#
# res = others.verify_default_image()
# if not res:
#     raise Exception("default image not found")
#
# res = others.check_remove_image_button_exists()
# if res:
#     raise Exception("Remove image button found")
#
# others.click_upload_photo()
# others.select_camera()
# try:
#     res = others.verify_text_camera_permission()
#     if res:
#         print("ok")
#     else:
#         pass
#         #raise Exception("text not matched")
#
#     others.click_allow()
# except:
#     try:
#         others.click_allow()
#     except:
#         pass
#
#
# sleep(1)
# others.capture_the_image_button()
# others.retake_the_image_button()
# others.capture_the_image_button()
# others.use_the_image_button()
#
# sleep(3)
# res = others.verify_default_image()
# if res:
#     raise Exception("default image found")
#
# res = others.check_remove_image_button_exists()
# if not res:
#     raise Exception("Remove image button not found")
#
# others.click_remove_image_button()
# sleep(2)
# res = others.verify_default_image()
# if not res:
#     raise Exception("default image not found")



def test_Others_TestcaseID_45795():
    """need to complete"""
    pass

# start_app("com.zebra.soho_app")
#
# others.wait_for_element_appearance("Home",10)
#
# login_page.click_Menu_HamburgerICN()
# others.click_notifications_button()
#
# Android_notification = others.get_notification_text_in_Android()
# sleep(3)
#
# login_page.click_Menu_HamburgerICN()
# others.click_on_profile_edit()
# others.scroll_down()
# others.click_log_out_button()
# others.wait_for_element_appearance("Login",10)
# login_page.click_loginBtn()
# sleep(5)
# login_page.click_Loginwith_Google()
# sleep(6)
# login_page.click_zebra_test_account()
# others.wait_for_element_appearance("Home",20)
# login_page.click_Menu_HamburgerICN()
# others.click_notifications_button()
#
# Android_notification_after_logout = others.get_notification_text_in_Android()
#
# res=others.check_two_arrays_same(Android_notification,Android_notification_after_logout)
# if not res:
#     print("Notifications are not same after log out")
#
#
# stop_app("com.zebra.soho_app")
# start_app("com.zebra.soho_app")
#
# others.wait_for_element_appearance("Home",10)
#
#
# login_page.click_Menu_HamburgerICN()
# others.click_notifications_button()
#
# Android_notification_after_closing_app = others.get_notification_text_in_Android()
#
# res = others.check_two_arrays_same(Android_notification,Android_notification_after_closing_app)
#
# if not res:
#     print("Notifications did not appear after reopening the app")
#
# others.uninstall_and_install_zsb_series_on_google_play()
# others.open_the_zsb_series_app_in_play_store()
# others.wait_for_element_appearance("Login",10)
# others.check_allow_permission_for_location()
# login_page.click_loginBtn()
# sleep(5)
# login_page.click_Loginwith_Google()
# sleep(6)
# login_page.click_zebra_test_account()
# others.wait_for_element_appearance("Home",20)
#
# login_page.click_Menu_HamburgerICN()
# others.click_notifications_button()
#
# Android_notification_after_deleting_app = others.get_notification_text_in_Android()
#
# res = others.check_two_arrays_same(Android_notification,Android_notification_after_deleting_app)
# if res:
#     print("Notifications did not disappear after deleting the app")



def test_Others_TestcaseID_45800():
    """Need to complete"""
    pass
#
# login_page.click_Menu_HamburgerICN()
# others.click_on_profile_edit()
#
# first_name = "zebras"
# others.edit_first_name(first_name)
# sleep(5)
#
# last_name = "ts"
# others.edit_last_name(last_name)
# sleep(5)
#
# current_first_name = others.get_first_name()
# current_last_name = others.get_last_name()
#
# if first_name == current_first_name and last_name == current_last_name:
#     print("ok")
# else:
#     raise Exception("dint update")

# others.scroll_down()
# others.change_password_for_user_account()
# sleep(5)
# others.enter_user_name_for_change_password("zebratest851@gmail.com")
# sleep(3)
# others.click_on_submit()
# sleep(5)
# # others.go_back()
# others.change_old_password_to_new_password("Zebra#987654321","Zebra#851851851")
# others.click_on_submit()
# sleep(2)
# res = others.check_password_changed_successfully()
# if not res:
#     raise Exception("password changed confirmation dint receive")
#
# others.click_here_to_login_after_changing_password()


def test_Others_TestcaseID_45803():
    pass

# res = others.check_printer_online_status()
# if res == "Online":
#     print("ok")
# else:
#     raise Exception("Printer is in offline state turn it on")
#
# login_page.click_Menu_HamburgerICN()
#
# """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
# others.click_Printer_Settings()
#
# """Returns printer name as dictionary format"""
# res = others.get_printers()
#
# """pass the printer name"""
# others.click_printer(res["a"])
# sleep(2)
#
# others.click_test_print()
# login_page.click_Menu_HamburgerICN()
#
# others.click_home_button()
#
# res = others.check_printer_online_status()
# if res == "Paper out":
#     print("ok")
# else:
#     raise Exception("Paper out should be shown")
#
# """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
# others.click_Printer_Settings()
#
# """Returns printer name as dictionary format"""
# res = others.get_printers()
#
# """pass the printer name"""
# others.click_printer(res["a"])
# sleep(2)
#
# others.click_test_print()
#
# login_page.click_Menu_HamburgerICN()
#
# others.click_home_button()
#
# res = others.check_printer_online_status()
# if res == "Online":
#     print("ok")
# else:
#     raise Exception("Printer is in offline state turn it on")

def test_Others_TestcaseID_45804():
    pass

# res = others.check_printer_online_status()
# if res == "Online":
#     print("ok")
# else:
#     raise Exception("Printer is not in Online state")
#
# others.select_first_label_from_home()
# others.click_print_button()
# sleep(3)
# others.check_error_print_preview()
#
# others.click_print_button()
# sleep(4)
#
# others.click_left_arrow()
#
#
# res = others.check_printer_online_status()
# if res == "Offline":
#     print("ok")
# else:
#     raise Exception("Printer is not in Offline state")

def test_Others_TestcaseID_45804():
    pass

# res = others.check_printer_online_status()
# if res == "Online":
#     print("ok")
# else:
#     raise Exception("Printer is not in Online state")
#
# others.select_first_label_from_home()
# others.click_print_button()
# sleep(3)
# others.check_error_print_preview()
#
# others.click_print_button()
# sleep(4)
# others.click_left_arrow()
#
#
# res = others.check_printer_online_status()
# if res == "Cover Open":
#     print("ok")
# else:
#     raise Exception("Printer is not in Cover Open state")
#
#
# others.select_first_label_from_home()
# others.click_print_button()
# sleep(3)
# others.check_error_print_preview()
#
# others.click_print_button()
# sleep(4)
#
# others.click_left_arrow()

def test_Others_TestcaseID_46963():
    pass
# login_page.click_Menu_HamburgerICN()
# others.click_Printer_Settings()
# res = others.get_printers()
# others.click_printer(res["zsbdp12"])
# others.click_wifi_button()
# others.click_manage_network_button()
# res = others.check_bluetooth_connection_required_diloge()
# if not res:
#     raise Exception("dilague dint show")
# others.click_continue_in_bluetooth_connection_required()
# others.scroll_down()
# others.click_add_network_button()
# sleep(10)
# others.scroll_down()
# others.scroll_down()
# others.scroll_down()
# others.scroll_down()
# others.scroll_down()
# others.scroll_down()
# others.scroll_down()
#

# others.click_enter_network_manually()

# others.enter_network_name("Zebra")
# others.click_join_network()
# sleep(3)
# login_page.click_Menu_HamburgerICN()
# others.click_home_button()

#
# login_page.click_Menu_HamburgerICN()
# others.click_Printer_Settings()
# res = others.get_printers()
# others.click_printer(res["zsbdp12"])
# others.click_wifi_button()
# others.click_manage_network_button()
# res = others.check_bluetooth_connection_required_diloge()
# if not res:
#     raise Exception("dilague dint show")
# others.click_continue_in_bluetooth_connection_required()
# others.scroll_down()
#
# res = others.get_network_names()
# others.swap_two_networks(res["NESTWIFI"], res["Zebra"])

# res = others.check_apply_changes_button_clickable()
# if not res:
#     raise Exception("Apply changes button not clickable")
# others.click_apply_changes_button()
# sleep(5)
# res = others.check_apply_changes_button_clickable()
# if res:
#     raise Exception("Apply changes button  clickable")
# res = others.get_network_names()
#
# others.delete_one_network(res["Zebra"])
# sleep(10)

# res = others.check_network_present("Zebra")
#
# if res:
#     raise Exception("network is not deleted")
# sleep(2)
# login_page.click_Menu_HamburgerICN()
# others.click_home_button()




def test_Others_TestcaseID_45802():
    pass

# login_page.click_loginBtn()
# sleep(2)
# others.click_on_sign_in_with_email()
# sleep(1)
# others.go_back()
#
# others.enter_user_name_in_sign_with_email("zebratest850@gmail.com")
#
# others.enter_password_in_sign_with_email("Zebra#123456789")
#
# # sleep_time = 60*29
# # sleep(sleep_time)
#
# others.click_on_sign_in()
# sleep(10)
#
# login_page.click_Menu_HamburgerICN()
# others.click_Printer_Settings()
# login_page.click_Menu_HamburgerICN()

def test_Others_TestcaseID_45872():
    pass
# login_page.click_loginBtn()
# sleep(2)
# others.click_on_sign_in_with_email()
# sleep(1)
# others.go_back()
#
# others.enter_user_name_in_sign_with_email("zebratest850@gmail.com")
#
# others.enter_password_in_sign_with_email("Zebra#123456789")
#
# sleep_time = 60*31
# sleep(sleep_time)
#
# others.click_on_sign_in()
#
# try:
#     others.wait_for_element_appearance("Home",10)
#     raise Exception("The page does not timeout")
# except:
#     pass


def test_Others_TestcaseID_47948():
    pass

# """login"""
# login_page.click_loginBtn()
# others.wait_for_element_appearance("Continue with Google",10)
# login_page.click_Loginwith_Google()
# others.wait_for_element_appearance_text("zebratest850@gmail.com",10)
# login_page.click_zebra_test_850_account()
# others.wait_for_element_appearance("Home")

# """print a test printer"""
#inp = int(input())

# login_page.click_Menu_HamburgerICN()
# others.click_Printer_Settings()
# others.select_printer_1("zsbdp12")
# others.scroll_down()
# others.click_test_print()
#
#
# login_page.click_Menu_HamburgerICN()
# others.click_home_button()
#
# """check the status of printer"""
# res = others.check_printer_online_status()
# if res == "Offline":
#     print("ok")



def test_Others_TestcaseID_45801():
    pass

# login_page.click_Menu_HamburgerICN()
# others.click_common_designs_button()
# others.search_designs("Address")
# sleep(4)
# others.select_first_design()
# sleep(4)
#
# others.search_designs("Asset")
# sleep(3)
# others.select_first_design()
#
# others.click_on_copy_to_my_designs()
# sleep(2)
#
# others.click_left_arrow()
# login_page.click_Menu_HamburgerICN()
# others.click_on_my_designs()
# others.search_designs("Asset")
# sleep(3)
# others.select_first_design()
#
# others.click_print_button()
# sleep(4)
#
# others.click_enter_data_for_design()
# others.enter_data_for_design("123456789")
# others.check_error_print_preview()
# sleep(3)
# res = others.check_the_swift_keyboard()
# if not res:
#     raise Exception("Keyboard not found")
#
# others.go_back()
# others.click_enter_text_for_design()
#
# others.check_error_print_preview()
#
# others.enter_text_for_design("My text")
# others.check_error_print_preview()
# sleep(3)
# res = others.check_the_swift_keyboard()
# if not res:
#     raise Exception("Keyboard not found")
# others.go_back()
# others.click_print_button()



def test_Others_TestcaseID_45794():
    pass

# """Generate less than 5 notifications"""
# login_page.click_Menu_HamburgerICN()
# others.click_notifications_button()
#
# Android_notification_before = others.get_notification_text_in_Android()
# sleep(3)
#
# #others.add_id_to_child_elem(Android_notification_before)
#
# others.click_down_arrow_button()
# others.click_dismiss_printer_notification()
#
# Android_notification_after = others.get_notification_text_in_Android()
#
# #others.add_id_to_child_elem(Android_notification_after)
#
# if len(Android_notification_before)>len(Android_notification_after):
#     print("Success")
# else:
#     raise Exception(" Notification dint dismiss ")
#
#
# print(Android_notification_before,)
# print(Android_notification_after)


def test_Others_TestcaseID_51703():
    pass

# others.install_zsb_series_on_google_play()
# sleep(30)
# others.open_the_zsb_series_app_in_play_store()
# others.check_allow_permission_for_location()
# login_page.click_loginBtn()
# sleep(5)
# login_page.click_Loginwith_Google()
# sleep(10)
# try:
#     login_page.click_zebra_test_account()
#     sleep(10)
# except:
#     pass
# res = others.check_home_page()
# if not res:
#     raise Exception("Not in Home page")

# others.uninstall_and_install_zsb_series_on_google_play()
# sleep(40)
# others.go_back()
# others.go_back()
# others.go_back()
# others.go_back()

# poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.01)
#
# while(1):
#     if others.check_zsb_app_icon():
#         t='present'
#         break
#     else:
#         poco.scroll()
#
# others.click_zsb_app_icon()
# sleep(10)

# others.check_allow_permission_for_location()
# login_page.click_loginBtn()
# sleep(5)
# login_page.click_Loginwith_Google()
# sleep(10)
# try:
#     login_page.click_zebra_test_account()
#     sleep(10)
# except:
#     pass
# res = others.check_home_page()
# if not res:
#     raise Exception("Not in Home page")

def test_Others_TestcaseID_45799():
    pass

# start_app("com.android.documentsui")
#
# t=''
#
# others.install_the_zsb_apk_in_files_android_8()
# sleep(3)
# res = others.check_app_is_installed_on_android_8()
# if res:
#     raise Exception("app is installed but it should not")
#
# others.go_back()
# others.go_back()

# poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.01)
#
# while(1):
#     if others.check_zsb_app_icon():
#         t='present'
#         break
#     else:
#         poco.scroll()
#
# if t == 'present':
#     raise Exception("app present")


def test_Others_TestcaseID_51704():
    pass


# cmd = 'adb install "C:\\Users\\tr5927\Downloads\ZsbMobile-stageOLD-4614.apk"'
# res = others.run_the_command(cmd)
#
# sleep(3)
# print(res)
#
# start_app("com.zebra.soho_app")
#
# sleep(10)
# others.check_allow_permission_for_location()
# login_page.click_loginBtn()
# sleep(5)
# login_page.click_Loginwith_Google()
# sleep(10)
# try:
#     login_page.click_zebra_test_account()
#     sleep(10)
# except:
#     pass
# res = others.check_home_page()
# if not res:
#     raise Exception("Not in Home page")
#
# cmd ='adb uninstall com.zebra.soho_app'
# res = others.run_the_command(cmd)
# print(res)
#
# sleep(2)
#
# cmd = 'adb install "C:\\Users\\tr5927\Downloads\ZsbMobile-stageOLD-4614.apk"'
# res = others.run_the_command(cmd)
# print(res)
#
# cmd = 'adb install "C:\\Users\\tr5927\Downloads\ZsbMobile-stage 4619.apk"'
# res = others.run_the_command(cmd)
# print(res)
#

# poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.01)
#
# while(1):
#     if others.check_zsb_app_icon():
#         t='present'
#         break
#     else:
#         poco.scroll()
# 
# others.click_zsb_app_icon()
# sleep(10)
# others.check_allow_permission_for_location()
# login_page.click_loginBtn()
# sleep(5)
# login_page.click_Loginwith_Google()
# sleep(10)
# try:
#     login_page.click_zebra_test_account()
#     sleep(10)
# except:
#     pass
# res = others.check_home_page()
# if not res:
#     raise Exception("Not in Home page")
#
#

def test_Others_TestcaseID_45807():
    pass
# recently_printed_labels_before = others.get_recently_printed_labels()
#
# login_page.click_Menu_HamburgerICN()
# others.click_common_designs_button()
# sleep(2)
# netw_1_common_designs = others.get_designs_visible_designs()
# login_page.click_Menu_HamburgerICN()
# others.click_on_my_designs()
# sleep(2)
# netw_1_my_designs = others.get_designs_visible_designs()
# login_page.click_Menu_HamburgerICN()
# others.click_on_my_data()
# sleep(2)
# netw_1_my_data = others.get_my_data_all()
#
#
# others.open_wifi_settings()
# sleep(3)
# others.select_wifi("POCO M3","1234567890")
# sleep(1)
#
# start_app("com.zebra.soho_app")
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# others.click_home_button()
# sleep(2)
# res = others.check_home_page()
# if not res:
#     raise Exception("home page not shown")
# recently_printed_labels_after = others.get_recently_printed_labels()
#
# res = others.check_same_after_switching_network(recently_printed_labels_before,recently_printed_labels_after)
# if not res:
#     print("changing network not showing files properly")
#
# sleep(4)
#
# """For Common Design"""
# others.open_wifi_settings()
# others.select_wifi("ZGuest","1234567890")
# sleep(1)
#
# start_app("com.zebra.soho_app")
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# others.click_common_designs_button()
# sleep(2)
# netw_2_common_designs = others.get_designs_visible_designs()
#
# res = others.check_same_after_switching_network(netw_1_common_designs,netw_2_common_designs)
# if not res:
#     print("changing network not showing files properly")
#
#
# """For My Design"""
# others.open_wifi_settings()
# sleep(1)
# others.select_wifi("POCO M3","1234567890")
# sleep(1)
#
# start_app("com.zebra.soho_app")
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# others.click_on_my_designs()
# sleep(2)
# netw_2_my_designs = others.get_designs_visible_designs()
#
# res = others.check_same_after_switching_network(netw_1_my_designs,netw_2_my_designs)
# if not res:
#     print("changing network not showing files properly")
#
# """For my data"""
#
# others.open_wifi_settings()
# sleep(1)
# others.select_wifi("ZGuest","1234567890")
# sleep(1)
#
# start_app("com.zebra.soho_app")
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# others.click_on_my_data()
# sleep(2)
# netw_2_my_data = others.get_my_data_all()
#
# res = others.check_same_after_switching_network(netw_1_my_data,netw_2_my_data)
# if not res:
#     print("changing network not showing files properly")











