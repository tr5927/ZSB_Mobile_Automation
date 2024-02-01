#from poco import poco
import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ZSB_Mobile.PageObject.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Social_Login import Social_Login
from ZSB_Mobile.Common_Method import *
import os

class test_Others():
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# start_app("com.zebra.soho_app")
# sleep(3.0)

login_page = Login_Screen(poco)
social_login = Social_Login(poco)

def test_Social_Login_TestcaseID_48464():
    pass

# login_page.click_loginBtn()
# sleep(5)
# res = social_login.check_zebra_logo()
# if not res:
#     raise Exception("Zebra logo not present")
#
# res = social_login.check_login_with_google()
# if not res:
#     raise Exception("Login with google not present")
#
# res = social_login.check_login_with_apple()
# if not res:
#     raise Exception("Login with Apple not present")
#
# res = social_login.check_login_with_facebook()
# if not res:
#     raise Exception("Login with Facebook not present")
#
# res = social_login.check_sign_in_with_email()
# if not res:
#     raise Exception("Sign in with email not present")
#
# res = social_login.check_text_of_free_benifits()
# if not res:
#     raise Exception(" Check under the Sign in with your email option, there is a Learn more about the Benefits of Creating a Free ZSB Account, and the Benefits of Creating a Free Account is highlighted in blue")
#
# social_login.scroll_down(1)
#
# social_login.check_the_cookie_text()
#
# res = social_login.check_options_under_cookie_text()
# if not res:
#     raise Exception("options are not proper or missing")


def test_Social_Login_TestcaseID_48465():
    pass

# login_page.click_loginBtn()
# sleep(5)
# social_login.click_on_benefits_of_zebra_account()
# res = social_login.check_the_text_of_benefits_of_free_account_page()
# if not res:
#     raise Exception("the page text dint match")
# social_login.scroll_up(1)
# social_login.check_both_images_in_benefits_of_free_account_page()
# social_login.scroll_up(1)
# res = social_login.check_the_back_button()
# if not res:
#     raise Exception("No back button")
# social_login.click_on_the_back_button()
# res = social_login.check_login_with_google()
# if not res:
#     raise Exception("Home page dint show up")


def test_Social_Login_TestcaseID_48466():
    pass

"""Need to complete"""
#
# login_page.click_loginBtn()
# sleep(5)
# social_login.open_in_chrome()
# social_login.scroll_down(1)
# social_login.click_on_zebra_link()
# if not social_login.verify_the_url("zebra.com."):
#     raise Exception("zebra.com url not present")
# social_login.go_back()
# social_login.swith_back_the_app()
# social_login.click_on_legal_notice_link()
# if not social_login.verify_the_url("zebra.com/us/en/about-zebra/company-information/legal/terms-of-use.html"):
#     raise Exception("zebra.com url not present")
# social_login.go_back()
# social_login.swith_back_the_app()
# sleep(1)
# social_login.click_on_privacy_statement_link()
# if not social_login.verify_the_url("zebra.com/us/en/about-zebra/company-information/legal/privacy-statement.html"):
#     raise Exception("zebra.com url not present")


def test_Social_Login_TestcaseID_48475():
    pass

# login_page.click_loginBtn()
# social_login.click_on_sign_in_with_email()
# keyevent("back")
# social_login.swipe_down(1)
#
# """Reset The password"""
# social_login.click_on_reset_password()
# social_login.wait_for_element_appearance_text("Password Recovery",10)
# social_login.enter_user_name_to_change_password()
# social_login.click_on_submit_button()
# social_login.wait_for_element_appearance("android.widget.EditText",10)
#
# """Enter the temp_pass was temporary password which is got through Mail and enter new password"""
# temp_pass = ""
# new_pass = ""
# social_login.enter_the_new_password_with_temporary_password(temp_pass,new_pass)
#
# social_login.click_on_submit_button()
#
# try:
#     social_login.wait_for_element_appearance_text("Password changed successfully.",10)
# except:
#     raise Exception("password changed confirmation dint receive")
#
# social_login.return_to_login_page()
# social_login.wait_for_element_appearance("Login",10)

# login_page.click_loginBtn()
# social_login.click_on_sign_in_with_email()
# social_login.complete_sign_in_with_email("zebra850@gmail.com","Zebra#@09876")

# try:
#     social_login.wait_for_element_appearance("Home",20)
# except:
#     raise Exception("dint sign in properly")

def test_Social_Login_TestcaseID_48473():
    pass


# login_page.click_loginBtn()
# social_login.click_on_sign_in_with_email()
# keyevent("back")
#
# if not social_login.check_zebra_logo():
#     raise Exception("Zebra Logo not present")
#
# if not social_login.check_username_and_password_feilds():
#     raise Exception("user name or password feilds nor present ")
#
# if not social_login.check_sign_in_button():
#     raise Exception("sign in button not present")
#
# social_login.swipe_down_half(1)
#
# if not social_login.check_close_button():
#     raise Exception("close button not present")

# if not social_login.check_text_of_register_your_email():
#     raise Exception("text not matching for register your email now")
#
# if not social_login.check_reset_password_text():
#     raise Exception("text not matching for reset password feild")
#
# social_login.click_on_close_button()
#
# if social_login.check_close_button():
#     raise Exception("page dint close")


def test_Social_Login_TestcaseID_48474():
    pass
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_on_sign_in_with_email()
# social_login.click_register_your_email()
# sleep(2)
# a=social_login.check_registration_of_email()
# if not a:
#     raise Exception("register user page dint show")
#
# """Enter the User Email"""
# email="zebra852@gmail.com"
# social_login.enter_user_email_for_registering(email)
# social_login.click_on_next()
#
# try:
#     social_login.wait_for_element_appearance("Resend Verification Code.",10)
# except:
#     raise Exception("Second step dint work")
#
# verification_code = "SLS9820000"
# social_login.enter_the_verification_code(verification_code)
# social_login.click_on_next()
# sleep(2)
# """Enter the first Name last name and the password"""
# first_n = "Zebra"
# last_n = "Z"
# password = "Zebra#123456789"
# social_login.enter_the_fields(first_n, last_n, password)
# social_login.select_the_country("India")
# social_login.select_the_check_boxes()
# social_login.click_submit_and_continue()
# sleep(2)
# social_login.check_sign_up_successful()
# social_login.click_on_continue()
#
#
#
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# social_login.click_on_sign_in_with_email()
#
# """Provide the email and password"""
# email = "zebra852@gmail.com"
# password = "Zebra#123456789"
# social_login.complete_sign_in_with_email(email,password)
#
# try:
#     social_login.wait_for_element_appearance("Home",20)
# except:
#     raise Exception("home page dint show up")
#
# login_page.click_loginBtn()
# social_login.click_on_profile_edit()
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Login",5)
# except:
#     raise Exception("Did not redirect to the login page")


def test_Social_Login_TestcaseID_48482():
    pass
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# social_login.click_on_sign_in_with_email()
#
# """Provide new_user name and password which is registered"""
# email = "zebratest852@gmail.com"
# password = "Zebra#123456789"
# social_login.complete_sign_in_with_email(email,password)
# if not social_login.check_EULA():
#     raise Exception("Eula is not dispayed")
#
# social_login.accept_EULA_agreement()
# social_login.wait_for_element_appearance("Home",10)
#
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# """Pass the first name last name and email to be expected"""
# first_name = "Zebra"
# last_name = "Zebra"
# social_login.validate_the_details_of_account(first_name, last_name, email)
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Login",5)
# except:
#     raise Exception("Did not redirect to the login page")

# email = "zebratest852@gmail.com"
# password = "Zebra#123456789"
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# social_login.click_on_sign_in_with_email()
# sleep(2)
# social_login.complete_sign_in_with_email(email,password)
# sleep(5)
# if social_login.check_EULA():
#     raise Exception("Eula is dispayed")


def test_Social_Login_TestcaseID_50646():
    pass

# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# social_login.click_on_sign_in_with_email()
#
# if not social_login.check_focused_of_user_name():
#     raise Exception("user name is not focused")
# if not social_login.check_key_board():
#     raise Exception("No key board displayed")

def test_Social_Login_TestcaseID_48467():
    pass

# login_page.click_loginBtn()
# login_page.click_Loginwith_Google()
#
# """Enter the email"""
# email = "zebratest850@gmail.com"
# social_login.choose_a_google_account(email)
# social_login.wait_for_element_appearance("Home",10)
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# if not social_login.check_the_email_in_profile_page(email):
#     raise Exception("the email is not matching")
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Login",10)
# except:
#     raise Exception("Did not redirect to the login page")

def test_Social_Login_TestcaseID_50643():
    pass

# login_page.click_loginBtn()
# login_page.click_Loginwith_Google()
#
# """Enter the email"""
# email = "zebratest850@gmail.com"
# social_login.choose_a_google_account(email)
# social_login.wait_for_element_appearance("Home",10)
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
#
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Login",10)
# except:
#     raise Exception("Did not redirect to the login page")
#
#
# login_page.click_loginBtn()
#
# login_page.click_Loginwith_Google()
#
# if not social_login.verify_choose_an_account_text():
#     raise Exception("did not redirect to the choose an acoount page")


def test_Social_Login_TestcaseID_50612():
    pass

# login_page.click_loginBtn()
#
# """Enter the email and password"""
# email = "zebratest850@gmail.com"
# password = 'Zebra#123456789'
#
# social_login.click_on_sign_in_with_email()
# social_login.complete_sign_in_with_email(email,password,0)
# social_login.show_the_password()
# sleep(4)
# res = social_login.get_the_password()
# if not res == password:
#     raise Exception("password is not matching")


def test_Social_Login_TestcaseID_48486():
    pass

# login_page.click_loginBtn()
#
# """Enter the email and password"""
# email = ""
# password = ''
#
# # social_login.click_on_sign_in_with_email()
# social_login.complete_sign_in_with_email(email,password,1)
# if not social_login.check_for_blank_value_error_of_both():
#     raise Exception("Error not displayed for blank values")
#
# email = "zebratest852@gmail.com"
# social_login.complete_sign_in_with_email(email,password,1,0)
# if not social_login.check_for_blank_value_error_of_password():
#     raise Exception("Error not displayed for blank values")
#
# password = "Zebra#123456789"
# social_login.complete_sign_in_with_email(email,password,1,0)
# if not social_login.wait_for_element_appearance("Home",10):
#     raise Exception('did not sign in properly')


def test_Social_Login_TestcaseID_48483():
    pass

# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# social_login.click_on_sign_in_with_email()
#
# """Provide new_user name and password which is registered"""
# email = "zebratest852@gmail.com"
# password = "Zebra#123456789"
# social_login.complete_sign_in_with_email(email,password)
# if social_login.check_EULA():
#     social_login.accept_EULA_agreement()
#
# social_login.wait_for_element_appearance("Home", 20)
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# """Pass the first name last name and email to be expected"""
# first_name = "Zebra"
# last_name = "Zebra"
# social_login.validate_the_details_of_account(first_name, last_name, email)
# if not social_login.check_the_email_in_profile_page(email):
#     raise Exception("Email are not matching")
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Login",5)
# except:
#     raise Exception("Did not redirect to the login page")



def test_Social_Login_TestcaseID_48485():
    pass

login_page.click_loginBtn()

"""Enter the email and password"""
email = ""
password = ''

# social_login.click_on_sign_in_with_email()
social_login.complete_sign_in_with_email(email,password,1)
if not social_login.check_for_blank_value_error_of_both():
    raise Exception("Error not displayed for blank values")

email = "zebratest852@gmail.com"
social_login.complete_sign_in_with_email(email,password,1,0)
if not social_login.check_for_blank_value_error_of_password():
    raise Exception("Error not displayed for blank values")

password = "Zebra#123456789"
social_login.complete_sign_in_with_email(email,password,1,0)
if not social_login.wait_for_element_appearance("Home",10):
    raise Exception('did not sign in properly')






