# from poco import poco
import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ZSB_Mobile.PageObject.Others.Others import Others

import os


class test_Others():
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# start_app("com.zebra.soho_app")
# sleep(3.0)
template_management = Template_Management_Android(poco)
login_page = Login_Screen(poco)
common_method = Common_Method(poco)
others = Others(poco)


class test_Android_Template_Management:
    pass


def test_Template_Management_TestcaseID_45902():
    pass


""" need Complete """


# login_page.click_loginBtn()
# login_page.click_Loginwith_Google()
#
# """Enter the email"""
# email = "zebratest850@gmail.com"
# login_page.choose_a_google_account(email)
# common_method.wait_for_element_appearance("Home",10)

def test_Template_Management_TestcaseID_45903():
    pass


# login_page.click_loginBtn()
# login_page.click_Loginwith_Google()
#
# """Enter the email"""
# email = "zebratest850@gmail.com"
# login_page.choose_a_google_account(email)
# common_method.wait_for_element_appearance("Home",10)

# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# sleep(2)
#
# prev = template_management.get_first_design_in_my_designs()
# template_management.click_first_design_in_my_designs()
# template_management.click_print_button()
# common_method.wait_for_element_appearance_enabled("Print",10)
# template_management.click_print_button_enabled()
# sleep(2)
# template_management.click_left_arrow()
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# sleep(2)
# curr = template_management.get_first_design_in_recently_printed_labels()

# if prev != curr:
#     raise Exception("the top of recently printed label is not as expected")

# curr_mon,curr_date,curr_year = template_management.get_current_date()
# des_mon,des_date,des_year = template_management.get_design_last_print_date(curr)
# if curr_mon!=des_mon or curr_date!=des_date or curr_year!=des_year:
#     raise Exception("dates not matching")

def test_Template_Management_TestcaseID_45904():
    pass


# login_page.click_loginBtn()
# login_page.click_Loginwith_Google()
#
# """Enter the email"""
# email = "zebratest850@gmail.com"
# login_page.choose_a_google_account(email)
# common_method.wait_for_element_appearance("Home",10)

# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# sleep(2)
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# sleep(2)
# common_method.wait_for_element_appearance_namematches("Showing")
# total_my_designs = template_management.get_all_designs_in_my_designs()
# design_7 = total_my_designs[6]
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
#
#
# for i in total_my_designs[:6]:
#     common_method.wait_for_element_appearance_namematches("Showing.")
#     template_management.click_design_in_my_designs_by_full_name(i)
#     template_management.click_print_button()
#     common_method.wait_for_element_appearance_enabled("Print",15)
#     template_management.click_print_button_enabled()
#     try:
#         common_method.wait_for_element_appearance_namematches("Print complete",10)
#     except:
#         raise Exception("print_toast_dint_pop up")
#     common_method.wait_for_element_appearance_enabled("android.widget.Button",10)
#     template_management.click_left_arrow()
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_home_button()
#     sleep(2)
#     common_method.wait_for_element_appearance("Recently Printed Labels")
#     curr = template_management.get_first_design_in_recently_printed_labels()
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_my_designs_button()

# if prev != curr:
#     raise Exception("the top of recently printed label is not as expected")

# curr_mon,curr_date,curr_year = template_management.get_current_date()
# des_mon,des_date,des_year = template_management.get_design_last_print_date(curr)
# if curr_mon!=des_mon or curr_date!=des_date or curr_year!=des_year:
#     raise Exception("dates not matching")


def test_Template_Management_TestcaseID_45905():
    pass


# login_page.click_loginBtn()
# login_page.click_Loginwith_Google()
#
# """Enter the email"""
# email = "zebratest850@gmail.com"
# login_page.choose_a_google_account(email)
# common_method.wait_for_element_appearance("Home",10)


"""Copy design from common design to my design"""


# login_page.click_Menu_HamburgerICN()
# template_management.click_common_designs_button()
#
# template_management.search_designs("Address")
# template_management.wait_for_designs_in_comm_design()

# curr_des = template_management.get_name_of_first_categories()
# # template_management.select_first_design()
# template_management.click_first_design_in_common_design()
# template_management.click_on_copy_to_my_designs()
# sleep(2)
# template_management.click_left_arrow()
#
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# template_management.search_designs(curr_des)

# common_method.wait_for_element_appearance_namematches("Showing",20)
# template_management.click_first_design_in_my_designs()
# template_management.click_print_button()
# common_method.wait_for_element_appearance_enabled("Print",30)
# template_management.click_print_button_enabled()

# template_management.click_left_arrow()
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()

# common_method.wait_for_element_appearance("Recently Printed Labels")
# curr = template_management.get_first_design_in_recently_printed_labels()
#
# curr_mon,curr_date,curr_year = template_management.get_current_date()
# des_mon,des_date,des_year = template_management.get_design_last_print_date(curr)
# if curr_mon!=des_mon or curr_date!=des_date or curr_year!=des_year:
#     raise Exception("dates not matching")

def test_Template_Management_TestcaseID_45906():
    pass


# login_page.click_loginBtn()
# login_page.click_Loginwith_Google()
#
# """Enter the email"""
# email = "zebratest850@gmail.com"
# login_page.choose_a_google_account(email)
# common_method.wait_for_element_appearance("Home",10)


# """Copy design from common design to my design"""
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_common_designs_button()
#
# template_management.search_designs("Address")
# common_method.wait_for_element_appearance_namematches("Categories")
# template_management.select_first_design()

# template_management.wait_for_designs_in_comm_design()
#
# curr_des = template_management.get_name_of_first_categories()
# template_management.click_first_design_in_common_design()
# sleep(2)
#
# template_management.click_print_button()
# common_method.wait_for_element_appearance_enabled("Print",30)
# template_management.click_print_button_enabled()

"""Will fail if the first design is not updated with the recently printed label"""


# common_method.wait_for_element_appearance_enabled("android.widget.Button",10)
# template_management.click_left_arrow()
# common_method.wait_for_element_appearance_enabled("android.widget.Button",10)
# template_management.click_left_arrow()
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
#
# common_method.wait_for_element_appearance("Recently Printed Labels")
# curr = template_management.get_first_design_in_recently_printed_labels()
#
# curr_mon,curr_date,curr_year = template_management.get_current_date()
# des_mon,des_date,des_year = template_management.get_design_last_print_date(curr)
# if curr_mon!=des_mon or curr_date!=des_date or curr_year!=des_year:
#     raise Exception("dates not matching")

def test_Template_Management_TestcaseID_45907():
    pass


# if not template_management.verify_element_exists_by_name("Recently Printed Labels"):
#     raise Exception("no recently printed label text")

# """pass no of designs printed as parameter"""
# all_designs = template_management.get_all_designs_in_recently_printed_labels(6)
#
# names,sizes= template_management.get_names_and_sizes_in_recently_printed_labels(all_designs)
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
#
# common_method.wait_for_element_appearance("Recently Printed Labels")
#
# curr = template_management.click_first_design_in_recently_printed_labels()
# a = template_management.verify_options_clickable_in_design()
# if not a:
#     raise Exception("some options are not clickable")
#
# template_management.close_menu_of_design_in_home()
#
# template_management.check_the_dates_of_last_print_in_recent_print_labels(all_designs)
#
#
# template_management.click_and_close_menu_designs_in_home(all_designs)

# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
#
# # common_method.wait_for_element_appearance("Recently Printed Labels")

def test_Template_Management_TestcaseID_45908():
    pass


# prev = template_management.get_no_of_left_cartridge()
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# total = template_management.get_all_designs_in_my_designs()
# template_management.click_on_design_which_is_not_printed_yet(total)
#
# template_management.click_print_button()
# common_method.wait_for_element_appearance_enabled("Print",10)
# template_management.click_print_button_enabled()
# sleep(2)
# template_management.click_left_arrow()
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# curr = template_management.get_no_of_left_cartridge()
# if prev!=curr:
#     raise Exception("number of prints left is updated")
#
# """Turn on the printer to be Online """
# common_method.swipe_by_positions([0.5,0.5], [0.5,1.0])
#
# after = template_management.get_no_of_left_cartridge()
#
# if after-1 != curr:
#     raise Exception("number of prints left is not updated")
#

def test_Template_Management_TestcaseID_45910():
    pass


# prev_designs = template_management.get_all_designs_in_recently_printed_labels()
# template_management.turn_off_wifi()
#
# template_management.refresh_the_home_page_till_you_see_error()
# template_management.check_the_error_msg_of_turning_off_wifi()
# template_management.click_on_continue()
# try:
#     template_management.click_on_continue()
# except:
#     pass
#
# curr_designs = template_management.get_all_designs_in_recently_printed_labels()
# if len(curr_designs)>0:
#     raise Exception("designs are displayed after turning off the wifi  ")

# template_management.turn_on_wifi()
#
# template_management.refresh_the_home_page_()
#
# common_method.wait_for_element_appearance("Recently Printed Labels")
#
# after_designs = template_management.get_all_designs_in_recently_printed_labels()
#
# if prev_designs!=after_designs:
#     raise Exception("designs are not matching before and after turning on wifi")

def test_Template_Management_TestcaseID_45909():
    pass


"""Print a design before staring this test case"""


# start_app("com.google.android.googlequicksearchbox")
#
# others.click_google_search_bar()
# others.enter_the_text_in_goole("https://zsbportal.zebra.com/")
# others.click_enter()
# others.wait_for_element_appearance("Continue with Google",10)
# login_page.click_Loginwith_Google()
# sleep(2)
# email = "zebratest850@gmail.com"
# login_page.choose_a_google_account(email)
#
# others.wait_for_element_appearance_text("Home",20)

# others.scroll_down()
# curr_date = template_management.get_current_date_in_mm_dd_yy_format()
#
# print_date = template_management.get_printer_date_in_google()
#
# if curr_date != print_date:
#     print(curr_date)
#     print(print_date)
#     raise Exception("dates are not matching")

def test_Template_Management_TestcaseID_45911():
    pass


#
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# full_name = template_management.select_design_in_my_design_by_name_and_return("4-elements")
#
# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")
#
# name="4-elements"
#
# try:
#     common_method.wait_for_element_appearance_namematches("4-elements")
# except:
#     raise Exception("name does not match")
#
# if not template_management.check_element_exists("Label 1 of 1"):
#     raise Exception("Label 1 of 1 not displayed")

# try:
#     template_management.check_element_exists("android.widget.EditText",1)
# except:
#     pass
#
# if not template_management.check_print_button_clickable:
#     raise Exception("print option is not clickable")


# template_management.click_print_button()

# prev_copies=template_management.get_no_of_copies()
#
# if not template_management.check_element_exists_name_or_text_matches("labels left"):
#     raise Exception("labels left not displayed")
#
# curr_copies = template_management.get_no_of_copies()
#
# if prev_copies!=curr_copies:
#     raise Exception("prev and curr copies are not same")
#
# template_management.check_element_exists("Total of 1 label")
#
# prev_count = template_management.get_no_of_labels_left_in_print_page()
# if not template_management.check_print_button_clickable:
#     raise Exception("print option is not clickable")
#
# template_management.click_print_button()
# common_method.wait_for_element_appearance_enabled("Print")
#
# curr_count = template_management.get_no_of_labels_left_in_print_page()
#
# if not int(prev_count) == int(curr_count)+1:
#     raise Exception("no of labels not updated")
#
# sleep(3)
# template_management.click_left_arrow()
# if not template_management.check_element_exists("My Designs"):
#     template_management.click_left_arrow()

# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# sleep(2)

# template_management.check_element_exists("My Designs")
#
# full_name = template_management.select_design_in_my_design_by_name_and_return("4-elements",0)
#
# pd,pm,py=template_management.get_design_last_print_date(full_name)
#
# cd,cm,cy=template_management.get_current_date()
# if pd != cd or pm != cm or py != cy:
#     raise Exception("dates are not matching")
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# sleep(1)
#
# labels_left = template_management.get_no_of_left_cartridge()
# if str(labels_left) != str(curr_count):
#     raise Exception("labels left not updated")

def test_Template_Management_TestcaseID_45912():
    pass


# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# full_name = template_management.select_design_in_my_design_by_name_and_return("variable_elements")
#
# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")
#
# initial_text = "Sample123"
#
# curr_text = template_management.get_text_from_element("android.widget.EditText",0)
# if initial_text!=curr_text:
#     raise Exception("initial text not matching")

# template_management.input_text_in_element_by_name("android.widget.EditText","",0)
# curr_text = template_management.get_text_from_element("android.widget.EditText",0)
# if curr_text != "":
#     raise Exception("text did not change")

# template_management.click_element_by_name_or_text("android.widget.EditText",0)
# new_text="new text"
# template_management.input_text_in_element_by_name("android.widget.EditText",new_text,0)
# curr_text = template_management.get_text_from_element("android.widget.EditText",0)
# if curr_text != new_text:
#     raise Exception("text did not change")

# new_text="new 123@gmai\n.com"
#
# template_management.input_text_in_element_by_name("android.widget.EditText",new_text,0)

# keyevent("back")

# curr_date = template_management.get_the_date_from_print_page()
# if curr_date!="11/11/2021":
#     raise Exception("initial date is not matching")
#
# template_management.set_new_date_in_print_page(15)

# curr_date = template_management.get_the_date_from_print_page()
# changing_date="02/15/2024"
# if curr_date!=changing_date:
#     raise Exception("initial date is not matching")


# prev_count = template_management.get_no_of_labels_left_in_print_page()
# if not template_management.check_print_button_clickable:
#     raise Exception("print option is not clickable")
#
# template_management.click_print_button()
# common_method.wait_for_element_appearance_enabled("Print")
#
#
# curr_count = template_management.get_no_of_labels_left_in_print_page()
#
# if not int(prev_count) == int(curr_count)+1:
#     raise Exception("no of labels not updated")
#
# sleep(5)
# template_management.click_left_arrow()
# if not template_management.check_element_exists("My Designs"):
#     template_management.click_left_arrow()
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# sleep(2)
#
# template_management.check_element_exists("My Designs")
#
# full_name = template_management.select_design_in_my_design_by_name_and_return("4-elements",0)
#
# pd,pm,py=template_management.get_design_last_print_date(full_name)
#
# cd,cm,cy=template_management.get_current_date()
# if pd != cd or pm != cm or py != cy:
#     raise Exception("dates are not matching")
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# sleep(1)
#
# labels_left = template_management.get_no_of_left_cartridge()
# curr_count = 102
# if str(labels_left) != str(curr_count):
#     raise Exception("labels left not updated")

def test_Template_Management_TestcaseID_45913():
    pass


# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# full_name = template_management.select_design_in_my_design_by_name_and_return("variable_image")
#
# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")

# template_management.check_element_exists("android.widget.EditText",0)
# template_management.check_element_exists("android.widget.EditText",1)
# template_management.check_element_exists("Picture\nicon\nChoose an option",0)
#
# initial_text = template_management.get_text_from_element("android.widget.EditText",1)
# if initial_text!="123":
#     raise Exception("initial_text not matching")
# template_management.click_element_by_name_or_text("android.widget.EditText",1)
# template_management.input_text_in_element_by_name("android.widget.EditText","",1)
# curr_text = template_management.get_text_from_element("android.widget.EditText",1)
# if curr_text:
#     raise Exception("blank value not accepted")
# new_text="4567890"
# template_management.input_text_in_element_by_name("android.widget.EditText",new_text,1)
# curr_text = template_management.get_text_from_element("android.widget.EditText",1)
# if curr_text!=new_text:
#     raise Exception("new text not updated")
# keyevent("back")


# initial_text = template_management.get_text_from_element("android.widget.EditText",0)
# if initial_text!="123456789012":
#     raise Exception("initial_text not matching")
# template_management.click_element_by_name_or_text("android.widget.EditText",0)
# template_management.input_text_in_element_by_name("android.widget.EditText","",0)
# curr_text = template_management.get_text_from_element("android.widget.EditText",0)
# if curr_text:
#     raise Exception("blank value not accepted")
# new_text="1234567890"
# template_management.input_text_in_element_by_name("android.widget.EditText",new_text,0)
# curr_text = template_management.get_text_from_element("android.widget.EditText",0)
# if curr_text!=new_text:
#     raise Exception("new text not updated")
# keyevent("back")

# template_management.click_on_image_input_in_print_page()
# template_management.upload_image_in_print_page()
# template_management.wait_for_image_upload_in_print_page()
# sleep(5)

# prev_count = template_management.get_no_of_labels_left_in_print_page()
#
# if not template_management.check_print_button_clickable:
#     raise Exception("print option is not clickable")
#
# template_management.click_print_button_enabled()
# common_method.wait_for_element_appearance_enabled("Print",20)
#
#
# curr_count = template_management.get_no_of_labels_left_in_print_page()
#
# if not int(prev_count) == int(curr_count)+1:
#     raise Exception("no of labels not updated")
#
# sleep(5)
# template_management.click_left_arrow()
# if not template_management.check_element_exists("My Designs"):
#     template_management.click_left_arrow()
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# sleep(2)
#
# template_management.check_element_exists("My Designs")
#
# full_name = template_management.select_design_in_my_design_by_name_and_return("vaiable_image",0)
#
# pd,pm,py=template_management.get_design_last_print_date(full_name)
#
# cd,cm,cy=template_management.get_current_date()
# if pd != cd or pm != cm or py != cy:
#     raise Exception("dates are not matching")

def test_Template_Management_TestcaseID_45914():
    pass


# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# full_name = template_management.select_design_in_my_design_by_name_and_return("45914")

# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")
#
# """Cannot check the numeric keypad display since it is different for different phones"""

# prev_copies=template_management.get_no_of_copies()
# prev_labels = template_management.get_no_of_labels_left_in_print_page()
#
# template_management.click_element_by_name_or_text("android.widget.EditText",0)
#
# template_management.input_text_in_element_by_name("android.widget.EditText","2",0)
# others.go_back()
#
# curr_copies=template_management.get_no_of_copies()
# if curr_copies!='2':
#     raise Exception("curr copies not updated")

# template_management.click_print_button_enabled()
# common_method.wait_for_element_appearance_enabled("Print")
# curr_labels = template_management.get_no_of_labels_left_in_print_page()
# temp=curr_labels
# if int(prev_labels)!=int(curr_labels)+2:
#     raise Exception("no of labels left not updated")
# sleep(5)
# template_management.click_left_arrow()
# if not template_management.check_element_exists("My Designs"):
#     template_management.click_left_arrow()
#
# template_management.check_element_exists("My Designs")
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# sleep(2)
# full_name = template_management.select_design_in_my_design_by_name_and_return("45914",0)
#
# pd,pm,py=template_management.get_design_last_print_date(full_name)
#
# cd,cm,cy=template_management.get_current_date()
# if pd != cd or pm != cm or py != cy:
#     raise Exception("dates are not matching")
#
# template_management.select_design_in_my_design_by_name_and_return("45914")
# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")
# curr_labels=template_management.get_no_of_labels_left_in_print_page()

# if curr_labels!=temp:
#     raise Exception("count not same after reselecting the design")

# template_management.click_left_arrow()
# if not template_management.check_element_exists("My Designs"):
#     login_page.click_Menu_HamburgerICN()
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# sleep(1)
#
# labels_left = template_management.get_no_of_left_cartridge()
#
# if str(labels_left) != str(curr_labels):
#     raise Exception("labels left not updated")

def test_Template_Management_TestcaseID_45915():
    pass


# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# full_name = template_management.select_design_in_my_design_by_name_and_return("variable_image")
#
# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")


# template_management.click_element_by_name_or_text("android.widget.EditText",1)
#
# new_text="4567890"
# template_management.input_text_in_element_by_name("android.widget.EditText",new_text,1)
#
# keyevent("back")
#
#
# template_management.click_element_by_name_or_text("android.widget.EditText",0)
#
# new_text="1234567890"
# template_management.input_text_in_element_by_name("android.widget.EditText",new_text,0)
#
# keyevent("back")

# template_management.click_on_image_input_in_print_page()
# template_management.upload_image_in_print_page()
# template_management.wait_for_image_upload_in_print_page()
# sleep(5)

# prev_labels = template_management.get_no_of_labels_left_in_print_page()
#
# template_management.click_on_copies()
# if not template_management.check_copies_focused():
#     raise Exception("cursor is not in copies")
# template_management.enter_no_of_copies(3)
# others.go_back()

# curr_copies=template_management.get_no_of_copies()
#
#
# if curr_copies!='3':
#     raise Exception("curr copies not updated")

# template_management.click_print_button_enabled()
# common_method.wait_for_element_appearance_enabled("Print")
# curr_labels = template_management.get_no_of_labels_left_in_print_page()
# temp=curr_labels
# if int(prev_labels)!=int(curr_labels)+3:
#     raise Exception("no of labels left not updated")
# sleep(5)

# template_management.click_left_arrow()
# if not template_management.check_element_exists("My Designs"):
#     template_management.click_left_arrow()
#
# template_management.check_element_exists("My Designs")
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# sleep(2)
# full_name = template_management.select_design_in_my_design_by_name_and_return("variable_image",0)
#
# pd,pm,py=template_management.get_design_last_print_date(full_name)
#
# cd,cm,cy=template_management.get_current_date()
# if pd != cd or pm != cm or py != cy:
#     raise Exception("dates are not matching")
#
# template_management.select_design_in_my_design_by_name_and_return("variable_image")
# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")
# curr_labels=template_management.get_no_of_labels_left_in_print_page()
# if curr_labels!=temp:
#     raise Exception("count not same after reselecting the design")
#
# template_management.click_left_arrow()
# if not template_management.check_element_exists("My Designs"):
#     login_page.click_Menu_HamburgerICN()
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# sleep(1)
#
# labels_left = template_management.get_no_of_left_cartridge()
#
# if str(labels_left) != str(curr_labels):
#     raise Exception("labels left not updated")

def test_Template_Management_TestcaseID_45916():
    pass


#
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# full_name = template_management.select_design_in_my_design_by_name_and_return("BOGO copy")
#
# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")
#
# if not template_management.check_prompt_for_smaller_label_than_current():
#     raise Exception("Prompt for smaller page is not displayed or may have wrong words")

# prev_labels = template_management.get_no_of_labels_left_in_print_page()
#
# template_management.click_on_copies()
#
# template_management.enter_no_of_copies(1)
# others.go_back()
# template_management.click_print_button_enabled()
#
# curr_copies=template_management.get_no_of_copies()
# if curr_copies!='1':
#     raise Exception("current copies are not one")

# common_method.wait_for_element_appearance_enabled("Print")
# curr_labels = template_management.get_no_of_labels_left_in_print_page()
# temp=curr_labels
# if int(prev_labels)!=int(curr_labels)+1:
#     raise Exception("no of labels left not updated")
# sleep(5)

# template_management.click_left_arrow()
# if not template_management.check_element_exists("My Designs"):
#     template_management.click_left_arrow()
#
# template_management.check_element_exists("My Designs")

# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# sleep(2)
# full_name = template_management.select_design_in_my_design_by_name_and_return("variable_image",0)
#
# pd,pm,py=template_management.get_design_last_print_date(full_name)
#
# cd,cm,cy=template_management.get_current_date()
# if pd != cd or pm != cm or py != cy:
#     raise Exception("dates are not matching")

# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# sleep(1)
#
# labels_left = template_management.get_no_of_left_cartridge()
#
# if str(labels_left) != str(curr_labels):
#     raise Exception("labels left not updated")

# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# full_name = template_management.select_design_in_my_design_by_name_and_return("45914")
#
# try:
#     common_method.wait_for_element_appearance_enabled("45914",15)
# except:
#     raise Exception("print page not displayed")
#
# if template_management.check_prompt_for_smaller_label_than_current():
#     raise Exception("Prompt for smaller page is  displayed or may have wrong words")
#
# template_management.click_print_button()
# common_method.wait_for_element_appearance_enabled("Print")
# template_management.click_print_button_enabled()

def test_Template_Management_TestcaseID_45917():
    pass


# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# sleep(2)
# full_name = template_management.select_design_in_my_design_by_name_and_return("Caution Heavy Package Label - Light - Vertical 4x6 copy")
#
# template_management.click_print_button()
#
#
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")
#
# if not template_management.check_prompt_for_smaller_label_than_current():
#     raise Exception("Prompt for smaller page is not displayed or may have wrong words")
#
# prev_labels = template_management.get_no_of_labels_left_in_print_page()
#
# template_management.click_on_copies()
#
# template_management.enter_no_of_copies(1)
# others.go_back()
# template_management.click_print_button_enabled()
#
# curr_copies=template_management.get_no_of_copies()
# if curr_copies!='1':
#     raise Exception("current copies are not one")
#
# common_method.wait_for_element_appearance_enabled("Print")
# curr_labels = template_management.get_no_of_labels_left_in_print_page()
# temp=curr_labels
# if int(prev_labels)!=int(curr_labels)+1:
#     raise Exception("no of labels left not updated")
# sleep(5)
#
# template_management.click_left_arrow()
# if not template_management.check_element_exists("My Designs"):
#     template_management.click_left_arrow()
#
# template_management.check_element_exists("My Designs")
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# sleep(2)
# full_name = template_management.select_design_in_my_design_by_name_and_return("variable_image",0)
#
# pd,pm,py=template_management.get_design_last_print_date(full_name)
#
# cd,cm,cy=template_management.get_current_date()
# if pd != cd or pm != cm or py != cy:
#     raise Exception("dates are not matching")
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# sleep(1)
#
# labels_left = template_management.get_no_of_left_cartridge()
#
# if str(labels_left) != str(curr_labels):
#     raise Exception("labels left not updated")
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# full_name = template_management.select_design_in_my_design_by_name_and_return("45914")
#
# try:
#     common_method.wait_for_element_appearance_enabled("45914",15)
# except:
#     raise Exception("print page not displayed")
#
# if template_management.check_prompt_for_smaller_label_than_current():
#     raise Exception("Prompt for smaller page is  displayed or may have wrong words")
#
# template_management.click_print_button()
# common_method.wait_for_element_appearance_enabled("Print")
# template_management.click_print_button_enabled()

def test_Template_Management_TestcaseID_45919():
    pass


# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# common_method.wait_for_element_appearance_namematches("Showing")
# original_name = "Decorative Gift Label copy"
# full_name = template_management.select_design_in_my_design_by_name_and_return(original_name)
#
# duplicate_name = template_management.duplicate_the_design_and_get_the_name()
# if original_name+" copy"!=duplicate_name:
#     raise Exception("default duplicate name is not changing")

# duplicate_name="Decorative Gift Label copy copy"
# full_name = template_management.select_design_in_my_design_by_name_and_return(duplicate_name)
#
# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")
#
# try:
#     common_method.wait_for_element_appearance_namematches(duplicate_name)
# except:
#     raise Exception("name does not match")
#
# if not template_management.check_element_exists("Label 1 of 1"):
#     raise Exception("Label 1 of 1 not displayed")
#
# try:
#     template_management.check_element_exists("android.widget.EditText",1)
# except:
#     pass
#
# if not template_management.check_print_button_clickable:
#     raise Exception("print option is not clickable")
#
#
# template_management.click_print_button()
#
# prev_copies=template_management.get_no_of_copies()
#
# if not template_management.check_element_exists_name_or_text_matches("labels left"):
#     raise Exception("labels left not displayed")
#
# curr_copies = template_management.get_no_of_copies()
#
# if prev_copies!=curr_copies:
#     raise Exception("prev and curr copies are not same")
#
# template_management.check_element_exists("Total of 1 label")
#
# prev_count = template_management.get_no_of_labels_left_in_print_page()
# if not template_management.check_print_button_clickable:
#     raise Exception("print option is not clickable")
#
# template_management.click_print_button()
# common_method.wait_for_element_appearance_enabled("Print")
#
# curr_count = template_management.get_no_of_labels_left_in_print_page()
#
# if not int(prev_count) == int(curr_count)+1:
#     raise Exception("no of labels not updated")

# sleep(5)
# template_management.click_left_arrow()
# if not template_management.check_element_exists("My Designs"):
#     template_management.click_left_arrow()


# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# sleep(2)
#
# template_management.check_element_exists("My Designs")

# full_name = template_management.select_design_in_my_design_by_name_and_return(duplicate_name,0)
#
# pd,pm,py=template_management.get_design_last_print_date(full_name)
#
# cd,cm,cy=template_management.get_current_date()
# if pd != cd or pm != cm or py != cy:
#     raise Exception("dates are not matching")

# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# sleep(1)
#
# labels_left = template_management.get_no_of_left_cartridge()
# print(labels_left,curr_count)
# if str(labels_left) != str(curr_count):
#     raise Exception("labels left not updated")

def test_Template_Management_TestcaseID_45920():
    pass


# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# common_method.wait_for_element_appearance_namematches("Showing")


# name="EnterText copy"
# template_management.select_design_in_my_design_by_name_and_return(name)

# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")

# template_management.click_element_by_name_or_text("android.widget.EditText",0)
# template_management.enter_the_special_characters_in_print_page("C31:C43'<>,.?£€)")
# a=template_management.get_text_from_element("android.widget.EditText",0)
# if a!="C31:C43'<>,.?£€)":
#     raise Exception("special characters are not entered proper")
#
# try:
#     template_management.click_element_by_name_or_text("Cancel")
# except:
#     pass
# others.go_back()
# template_management.click_print_button()
#
#
# if not template_management.check_element_exists_name_or_text_matches("labels left"):
#     raise Exception("labels left not displayed")
#
# template_management.check_element_exists("Total of 1 label")
#
# prev_count = template_management.get_no_of_labels_left_in_print_page()
#
# template_management.click_print_button()
# common_method.wait_for_element_appearance_enabled("Print")
#
# curr_count = template_management.get_no_of_labels_left_in_print_page()
#
# if not int(prev_count) == int(curr_count)+1:
#     raise Exception("no of labels not updated")
#
# sleep(5)
# template_management.click_left_arrow()
# if not template_management.check_element_exists("My Designs"):
#     template_management.click_left_arrow()
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# sleep(2)
#
# template_management.check_element_exists("My Designs")
#
# full_name = template_management.select_design_in_my_design_by_name_and_return(name,0)
#
# pd,pm,py=template_management.get_design_last_print_date(full_name)
#
# cd,cm,cy=template_management.get_current_date()
# if pd != cd or pm != cm or py != cy:
#     raise Exception("dates are not matching")
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# sleep(1)
#
# labels_left = template_management.get_no_of_left_cartridge()
# print(labels_left,curr_count)
# if str(labels_left) != str(curr_count):
#     raise Exception("labels left not updated")

def test_Template_Management_TestcaseID_45923():
    pass


# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# common_method.wait_for_element_appearance_namematches("Showing")
#
#
# name="Asset copy"
# template_management.select_design_in_my_design_by_name_and_return(name)
#
# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")
#
# prev_count = template_management.get_no_of_labels_left_in_print_page()
# template_management.click_left_arrow()
# if not template_management.check_element_exists("My Designs"):
#     template_management.click_left_arrow()
#
# template_management.check_element_exists("My Designs")
#
# full_name = template_management.select_design_in_my_design_by_name_and_return(name,0)
#
# try:
#     template_management.get_design_last_print_date(full_name)
#     raise Exception("last print updated")
# except:
#     pass
#
# template_management.select_design_in_my_design_by_name_and_return(name)
#
# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")
#
# curr_count=template_management.get_no_of_labels_left_in_print_page()
# if prev_count!=curr_count:
#     raise Exception("print label updated without printing")
#
# template_management.click_print_button_enabled()
# common_method.wait_for_element_appearance_enabled("Print")
#
# curr_count=template_management.get_no_of_labels_left_in_print_page()
#
# sleep(5)

# template_management.click_left_arrow()
# if not template_management.check_element_exists("My Designs"):
#     template_management.click_left_arrow()
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
# sleep(1)
#
# labels_left = template_management.get_no_of_left_cartridge()
# print(labels_left,curr_count)
# if str(labels_left) != str(curr_count):
#     raise Exception("labels left not updated")

def test_Template_Management_TestcaseID_45924():
    pass


# name="Asset copy"
# template_management.select_design_in_recetly_printed_design_by_name_and_return(name)
#
# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")
#
# prev_count = template_management.get_no_of_labels_left_in_print_page()
# template_management.click_left_arrow()
# if not template_management.check_element_exists("Home"):
#     template_management.click_left_arrow()
#
# template_management.check_element_exists("Home")
#
# full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name,0)
#
# try:
#     template_management.get_design_last_print_date(full_name)
#     raise Exception("last print updated")
# except:
#     pass
#
# template_management.select_design_in_recetly_printed_design_by_name_and_return(name)
#
# template_management.click_print_button()
# try:
#     common_method.wait_for_element_appearance_enabled("Print",15)
# except:
#     raise Exception("print page not displayed")
#
# curr_count=template_management.get_no_of_labels_left_in_print_page()
# if prev_count!=curr_count:
#     raise Exception("print label updated without printing")
#
# template_management.click_print_button_enabled()
# common_method.wait_for_element_appearance_enabled("Print")
#
# sleep(5)

# curr_count=template_management.get_no_of_labels_left_in_print_page()
#
# template_management.click_left_arrow()
# if not template_management.check_element_exists("Home"):
#     template_management.click_left_arrow()
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# login_page.click_Menu_HamburgerICN()
# template_management.click_home_button()
#
# labels_left = template_management.get_no_of_left_cartridge()
# print(labels_left,curr_count)
# if str(labels_left) != str(curr_count):
#     raise Exception("labels left not updated")

def test_Template_Management_TestcaseID_45926():
    pass


# """a. Verify "Edit name" window is displayed not in mobile app"""
# """Save" button is NOT clickable (is clickable in mobile)"""
#
# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# common_method.wait_for_element_appearance_namematches("Showing")
# """Give the name of existing design here"""
# name="assets (1)"
# full_name = template_management.select_design_in_my_design_by_name_and_return(name,1)
# prev_size,prev_date= template_management.get_the_size_and_lastprint_of_design(full_name)
#
# template_management.click_on_rename_button()
#
# default_value= template_management.get_the_default_rename_text()
# if default_value!=name:
#     raise Exception("default value not matches the design's name")
#
# if not template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("cancel button is not clickable")

# if template_management.check_save_button_clickable_in_rename_popup():
#     raise Exception("save button is clickable")

# template_management.enter_text_in_rename_design("\/")
# if not template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error not displayed for invalid characters")
#
# new_name = "somenamemyown"
#
# template_management.enter_text_in_rename_design(new_name)
# if template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error displayed for valid characters")
#
# template_management.click_on_save_button_in_rename_design()
#
# try:
#     common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
#
# except:
#     raise Exception("design has been successfully renamed. is not displayed")
#
# if template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("rename popup not closed")
#
# try:
#     full_name = template_management.select_design_in_my_design_by_name_and_return(new_name, 0)
# except:
#     raise Exception("design not found after updating")
#
# curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)
#
# if curr_size!=prev_size or curr_date!=prev_date:
#     raise Exception("size or date is not matching after renaming the design")
#
def test_Template_Management_TestcaseID_45927():
    pass


# name="somenamemyown"
# full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name,1)
# prev_size,prev_date= template_management.get_the_size_and_lastprint_of_design(full_name)
#
# template_management.click_on_rename_button()
#
# default_value= template_management.get_the_default_rename_text()
# if default_value!=name:
#     raise Exception("default value not matches the design's name")
#
# if not template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("cancel button is not clickable")

# if template_management.check_save_button_clickable_in_rename_popup():
#     raise Exception("save button is clickable")

# new_name = "ownname"
#
# template_management.enter_text_in_rename_design(new_name)
# if template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error displayed for valid characters")
#
# template_management.click_on_save_button_in_rename_design()
# try:
#     common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
#
# except:
#     raise Exception("design has been successfully renamed. is not displayed")
#
# if template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("rename popup not closed")
#
# try:
#     full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(new_name, 0)
# except:
#     raise Exception("design not found after updating")
#
# curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)
#
# if curr_size!=prev_size or curr_date!=prev_date:
#     raise Exception("size or date is not matching after renaming the design")

def test_Template_Management_TestcaseID_45928():
    pass


# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# common_method.wait_for_element_appearance_namematches("Showing")
# """Give the name of existing design here"""
# name="ownname"
# full_name = template_management.select_design_in_my_design_by_name_and_return(name,1)
#
# template_management.click_on_rename_button()
#
# new_name = "Address"
#
# template_management.enter_text_in_rename_design(new_name)
# if template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error displayed for valid characters")
#
# template_management.click_on_save_button_in_rename_design()
#
# try:
#     common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
# except:
#     raise Exception("design has been successfully renamed. is not displayed")
#
# if template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("rename popup not closed")
# try:
#     full_name = template_management.select_design_in_my_design_by_name_and_return(new_name+" (1)", 0)
# except:
#     raise Exception("design not found after updating")
#
# template_management.select_design_in_my_design_by_name_and_return(new_name+" (1)",1)
# template_management.click_on_rename_button()
#
# default_value= template_management.get_the_default_rename_text()
# if default_value!=new_name+" (1)":
#     raise Exception("default value not updated to new value")
#
# if not template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("cancel button is not clickable")

# if not template_management.check_save_button_clickable_in_rename_popup():
#     raise Exception("save button is not clickable")
# template_management.click_on_cancel_button_in_rename_popup()

def test_Template_Management_TestcaseID_45929():
    pass


# """Give the name of existing design here"""
# name="ownname"
# full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name,1)
# template_management.click_on_rename_button()
# new_name = "Address"
#
# template_management.enter_text_in_rename_design(new_name)
# if template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error displayed for valid characters")
#
# template_management.click_on_save_button_in_rename_design()
#
# try:
#     common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
# except:
#     raise Exception("design has been successfully renamed. is not displayed")
#
# if template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("rename popup not closed")
# try:
#     full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(new_name+" (1)", 0)
# except:
#     raise Exception("design not found after updating")
#
# template_management.select_design_in_recetly_printed_design_by_name_and_return(new_name+" (1)",1)
# template_management.click_on_rename_button()
#
# default_value= template_management.get_the_default_rename_text()
# if default_value!=new_name+" (1)":
#     raise Exception("default value not updated to new value")
#
# if not template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("cancel button is not clickable")
#
# if not template_management.check_save_button_clickable_in_rename_popup():
#     raise Exception("save button is not clickable")
# template_management.click_on_cancel_button_in_rename_popup()

def test_Template_Management_TestcaseID_45930():
    pass


# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# common_method.wait_for_element_appearance_namematches("Showing")
# """Give the name of existing design here"""
# name="Address copy"
# full_name = template_management.select_design_in_my_design_by_name_and_return(name,1)
# template_management.click_on_rename_button()
# template_management.click_on_save_button_in_rename_design()
# try:
#     common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
# except:
#     raise Exception("design has been successfully renamed. is not displayed")
#
# if template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("rename popup not closed")
# try:
#     full_name = template_management.select_design_in_my_design_by_name_and_return(name+" (1)", 0)
# except:
#     raise Exception("design not found after updating")
#
# template_management.select_design_in_my_design_by_name_and_return(name+" (1)",1)
# template_management.click_on_rename_button()
#
# default_value= template_management.get_the_default_rename_text()
# if default_value!=name+" (1)":
#     raise Exception("default value not updated to new value")
#
# if not template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("cancel button is not clickable")
#
# if not template_management.check_save_button_clickable_in_rename_popup():
#     raise Exception("save button is not clickable")
# template_management.click_on_cancel_button_in_rename_popup()

def test_Template_Management_TestcaseID_45931():
    pass


# """Give the name of existing design here"""
# name="Address copy"
# full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name,1)
# template_management.click_on_rename_button()
# template_management.click_on_save_button_in_rename_design()
# try:
#     common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
# except:
#     raise Exception("design has been successfully renamed. is not displayed")
#
# if template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("rename popup not closed")
# try:
#     full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name+" (1)", 0)
# except:
#     raise Exception("design not found after updating")
#
# template_management.select_design_in_recetly_printed_design_by_name_and_return(name+" (1)",1)
# template_management.click_on_rename_button()
#
# default_value = template_management.get_the_default_rename_text()
# if default_value != name+" (1)":
#     raise Exception("default value not updated to new value")
#
# if not template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("cancel button is not clickable")
#
# if not template_management.check_save_button_clickable_in_rename_popup():
#     raise Exception("save button is not clickable")
# template_management.click_on_cancel_button_in_rename_popup()

def test_Template_Management_TestcaseID_45934():
    pass

# name = "Address copy"
# full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name, 1)
# prev_size,prev_date= template_management.get_the_size_and_lastprint_of_design(full_name)
#
# template_management.click_on_rename_button()
#
# template_management.enter_text_in_rename_design("")
# if not template_management.check_error_for_blank_value_in_rename_design():
#     raise Exception("error not displayed for blank field")
#
# template_management.click_on_cancel_button_in_rename_popup()
# sleep(1)
# if template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("rename popup not closed")
#
# try:
#     template_management.select_design_in_recetly_printed_design_by_name_and_return(name, 1)
#     template_management.click_on_rename_button()
# except:
#     raise Exception("design name not found after blank value cancellation")
#
# default_value = template_management.get_the_default_rename_text()
# if default_value != name:
#     raise Exception("default value not matches with original name")
#
# if not template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("cancel button is not clickable")
#
# if not template_management.check_save_button_clickable_in_rename_popup():
#     raise Exception("save button is not clickable")
#
# new_name="A_1"
# template_management.enter_text_in_rename_design(new_name)
# if template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error  displayed for valid characters")
#
# template_management.click_on_save_button_in_rename_design()
#
# try:
#     common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
# except:
#     raise Exception("design has been successfully renamed. is not displayed")
#
# if template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("rename popup not closed")
#
# full_name=template_management.select_design_in_recetly_printed_design_by_name_and_return(new_name, 1)
# curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)
#
# if curr_size!=prev_size or curr_date!=prev_date:
#     raise Exception("size or date is not matching after renaming the design")
#
# template_management.click_on_rename_button()
#
# template_management.enter_text_in_rename_design("&*%")
# if not template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error not displayed for invalid characters")
#
# if template_management.check_save_button_clickable_in_rename_popup():
#     raise Exception("save button is enabled for invalid characters")
#
# """. Input only one or several spaces
# Check spaces should be auto cleared and provide the message "Name must be at least 1 character…”  fails"""
# template_management.enter_text_in_rename_design("   ")
# if not template_management.check_error_for_blank_value_in_rename_design():
#     raise Exception("error not displayed for blank field")

def test_Template_Management_TestcaseID_45935():
    pass

# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# common_method.wait_for_element_appearance_namematches("Showing")
# """Give the name of existing design here"""
# name="Address copy"
# full_name = template_management.select_design_in_my_design_by_name_and_return(name,1)
# template_management.click_on_rename_button()
# new_name="A_1"
# template_management.enter_text_in_rename_design(new_name)
# if template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error  displayed for valid characters")
#
# template_management.click_on_cancel_button_in_rename_popup()
# sleep(2)
# if template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("rename popup not closed")
#
# try:
#     full_name = template_management.select_design_in_my_design_by_name_and_return(name, 1)
# except:
#     raise Exception("design not found after cancelling")
# template_management.click_on_rename_button()
#
# default_value= template_management.get_the_default_rename_text()
# if default_value!=name:
#     raise Exception("original name changed even after cancellation")
#
# if not template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("cancel button is not clickable")
#
# if not template_management.check_save_button_clickable_in_rename_popup():
#     raise Exception("save button is not clickable")

def test_Template_Management_TestcaseID_45936():
    pass

# name="Address copy"
# full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name,1)
# template_management.click_on_rename_button()
#
# new_name="A_1"
# template_management.enter_text_in_rename_design(new_name)
# if template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error  displayed for valid characters")
#
# template_management.click_on_cancel_button_in_rename_popup()
# sleep(2)
# if template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("rename popup not closed")
#
# try:
#     full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name, 1)
# except:
#     raise Exception("design not found after cancelling")
# template_management.click_on_rename_button()
#
# default_value= template_management.get_the_default_rename_text()
# if default_value!=name:
#     raise Exception("original name changed even after cancellation")
#
# if not template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("cancel button is not clickable")
#
# if not template_management.check_save_button_clickable_in_rename_popup():
#     raise Exception("save button is not clickable")

def test_Template_Management_TestcaseID_45938():
    pass

# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# common_method.wait_for_element_appearance_namematches("Showing")
# """Give the name of existing design here"""
# name = "Address copy"
# full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name, 1)
# prev_size,prev_date= template_management.get_the_size_and_lastprint_of_design(full_name)
# template_management.click_on_rename_button()
#
# default_value = template_management.get_the_default_rename_text()
# if default_value != name:
#     raise Exception("default value not matches with original name")
#
# template_management.enter_text_in_rename_design("Abc123+")
# if not template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error not displayed for invalid characters")
#
# if template_management.check_save_button_clickable_in_rename_popup():
#     raise Exception("save button is enabled for invalid characters")
#
# template_management.enter_text_in_rename_design("! @ $ ^ - ~ ( ) _  ` = { } | [ ] ; '")
# if template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error not displayed for allowed special characters ")
#
# new_name="new@_name"
# template_management.enter_text_in_rename_design(new_name)
# if template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error not displayed for allowed special characters ")
#
# if not template_management.check_save_button_clickable_in_rename_popup():
#     raise Exception("save button is disabled for valid special characters")
#
# template_management.click_on_save_button_in_rename_design()
#
# try:
#     common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
# except:
#     raise Exception("design has been successfully renamed. is not displayed")
#
# if template_management.check_cancel_button_clickable_in_rename_popup():
#     raise Exception("rename popup not closed")
#
# try:
#     full_name=template_management.select_design_in_recetly_printed_design_by_name_and_return(new_name, 0)
# except:
#     raise Exception("updated name not found")
# curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)
#
# if curr_size!=prev_size or curr_date!=prev_date:
#     raise Exception("size or date is not matching after renaming the design")

def test_Template_Management_TestcaseID_45940():
    pass

# login_page.click_Menu_HamburgerICN()
# template_management.click_my_designs_button()
# common_method.wait_for_element_appearance_namematches("Showing")
# """Give the name of existing design here"""
# name = "Address copy"
# full_name = template_management.select_design_in_my_design_by_name_and_return(name, 1)
# prev_size,prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)
# template_management.click_on_rename_button()
#
# new_name="new@_name"
# template_management.enter_text_in_rename_design(new_name)
# if template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error not displayed for allowed special characters ")
#
# template_management.turn_off_wifi()
# sleep(2)
# template_management.click_on_save_button_in_rename_design()
# """Verify connection lost alert "Error communicating with server" with "Cancel" and "Save" buttons is displayed this step has error"""
# template_management.turn_on_wifi()
# sleep(5)
# template_management.click_on_save_button_in_rename_design()
#
# try:
#     common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
# except:
#     raise Exception("design has been successfully renamed. is not displayed")
#
# try:
#     full_name=template_management.select_design_in_my_design_by_name_and_return(new_name, 0)
# except:
#     raise Exception("updated name not found")
# curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)
#
# if curr_size!=prev_size or curr_date!=prev_date:
#     raise Exception("size or date is not matching after renaming the design")

def test_Template_Management_TestcaseID_45941():
    pass

# """Give the name of existing design here"""
# name = "Address copy"
# full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name, 1)
# prev_size,prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)
# template_management.click_on_rename_button()
#
# new_name="new@_name"
# template_management.enter_text_in_rename_design(new_name)
# if template_management.check_error_for_invalid_characters_in_rename_design():
#     raise Exception("error not displayed for allowed special characters ")
#
# template_management.turn_off_wifi()
# sleep(2)
# template_management.click_on_save_button_in_rename_design()
# """Verify connection lost alert "Error communicating with server" with "Cancel" and "Save" buttons is displayed this step has error"""
# template_management.turn_on_wifi()
# sleep(5)
# template_management.click_on_save_button_in_rename_design()
#
# try:
#     common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
# except:
#     raise Exception("design has been successfully renamed. is not displayed")
#
# try:
#     full_name=template_management.select_design_in_recetly_printed_design_by_name_and_return(new_name, 0)
# except:
#     raise Exception("updated name not found")
# curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)
#
# if curr_size!=prev_size or curr_date!=prev_date:
#     raise Exception("size or date is not matching after renaming the design")

def test_Template_Management_TestcaseID_45976():
    pass

login_page.click_Menu_HamburgerICN()
template_management.click_my_designs_button()
"""Search your designs" (for this search designs is prompt text) prompt text and Search icon are displayed"""
template_management.check_search_icon()
template_management.check_search_designs_text()
template_management.click_on_search_design()
"""input value that does not match with our current designs"""
not_exists_design="noexists"
template_management.search_designs(not_exists_design)

"""3. Type in text that does not have a match any of the user's designs
a. Verify Suggestions dropdown is displayed
b. Verify "No results for "searched text"" text is displayed (this step has error id SMBUI-1305)
c. Verify "Search tips: try typing exactly what you’re looking for. It may help to simply type 1 word, and search for results then."""

template_management.search_designs("")













