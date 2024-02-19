from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

from ZSB_Mobile.PageObject.Login_Screen import *

from ZSB_Mobile.PageObject.Help_Screen.Help_Screen import Help_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen


class Android_App_Help:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
start_app("com.zebra.soho_app")
sleep(2.0)

common_method = Common_Method()
login_page = Login_Screen(poco)
help_page = Help_Screen(poco)


def test_Help_TestcaseID_45789():
    """""""""test"""""


# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# sleep(2)
# login_page.click_GooglemailId()
# sleep(5)
# # login_page.add_Account()
# # sleep(2)
# # login_page.Enter_Google_UserID()
# # sleep(2)
# # login_page.click_Emailid_Nextbtn()
# # sleep(4)
# # """"To enter password need to use the 2nd method """
# # login_page.Enter_Google_Password()
# # # poco(text("Swdvt@#123"))
# # # sleep(2)
# # login_page.click_Password_Nextbtn()
# sleep(7)
# help_page.chooseAcc()
# sleep(10)
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Swipe up"""
# poco.scroll()
# sleep(2)
# """Check Help icon with '?' is present"""
# help_page.checkIfHelpIconIsPresent()
# """Click Help dropdown to expand Help options"""
# help_page.click_Help_dropdown_option()
# sleep(2)
# """Check Help has Support, FAQs, Contact Us and Live Chat Options"""
# # help_page.verify_text("Live Chat", help_page.Chat_btn)
# help_page.Test_Support_faq_Contactus__Livechat_is_present()
# """Click Support to open support page"""
# help_page.click_Support()
# sleep(5)
# """Check if we are redirected to support page"""
# help_page.checkIfLandedOnSupportPage()
# sleep(5)
# help_page.verify_url("https://zsbsupport.zebra.com/s/")
# sleep(5)
# common_method.swipe_screen([1, 0.3482905982905983], [0.22037037037037038, 0.3482905982905983], 1)
# """Click FAQs to see FAQ on the web"""
# sleep(5)
# help_page.click_FAQs()
# sleep(5)
# """Check if we are redirected to FAQs page"""
# help_page.checkIfLandedOnFAQsPage()
# sleep(5)
# help_page.verify_url("https://zsbsupport.zebra.com/s/faqs")
# sleep(5)
# common_method.swipe_screen([1, 0.3482905982905983], [0.22037037037037038, 0.3482905982905983], 1)
# sleep(2)
# """Click Contact US to view contact options"""
# help_page.click_ContactUs()
# sleep(5)
# """Check if we are redirected to Contact Us page"""
# help_page.checkIfLandedOnContactUsPage()
# sleep(5)
# help_page.verify_url("https://zsbsupport.zebra.com/s/contactsupport")
# sleep(5)
# common_method.swipe_screen([1, 0.3482905982905983], [0.22037037037037038, 0.3482905982905983], 1)
# sleep(2)
# """Click chat to """
# help_page.click_Chat()
# sleep(5)
# """Verify Chat Page Title"""
# help_page.verifyLiveChatWindowTitle()
# sleep(2)
# """Verify if Begin Chat button is present"""
# help_page.verifyBeginChatBtn()
# sleep(2)
# stop_app("com.zebra.soho_app")

#
# def test_Help_TestcaseID_47788():
#     """""""""test"""""
#
#
# start_app("com.zebra.soho_app")
# """Click hamburger icon to expand menu"""
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Swipe up"""
# poco.scroll()
# sleep(2)
# """Click Help dropdown to expand Help options"""
# help_page.click_Help_dropdown_option()
# # poco(name="Help").click()
# sleep(2)
# """Click Live Chat"""
# help_page.click_Chat()
# sleep(2)
# """Check if it displays Available 7am to 7pm ET"""
# try:
#     help_page.verifyChatHours()
# except ZeroDivisionError:
#     pass
#
# sleep(2)
# """Begin Chat"""
# help_page.clickBeginChat()
# sleep(2)
# """Click Back Arrow"""
# help_page.clickBackArrow()
# sleep(2)
# """Check if it displays Available 7am to 7pm ET"""
# """Unable to verify due to BUG"""
# help_page.verifyChatHours()
# sleep(2)
# stop_app("com.zebra.soho_app")

# def test_Help_TestcaseID_47919():
#     """""""""test"""""
#
# start_app("com.zebra.soho_app")
# sleep(5)
# # """""""""click on the login button"""""""""""
# # login_page.click_loginBtn()
# # sleep(2)
# # """""""select the login with google option"""""""""
# # login_page.click_Loginwith_Google()
# # sleep(2)
# # login_page.click_GooglemailId()
# # sleep(5)
# # login_page.add_Account()
# # sleep(2)
# # login_page.Enter_Google_UserID()
# # sleep(2)
# # login_page.click_Emailid_Nextbtn()
# # sleep(4)
# # """"To enter password need to use the 2nd method """
# # login_page.Enter_Google_Password()
# # # poco(text("Swdvt@#123"))
# # # sleep(2)
# # login_page.click_Password_Nextbtn()
# # sleep(7)
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Swipe up"""
# poco.scroll()
# sleep(2)
# """Check Help icon with '?' is present"""
# help_page.checkIfHelpIconIsPresent()
# """Click Help dropdown to expand Help options"""
# help_page.click_Help_dropdown_option()
# sleep(2)
# """Click Live Chat"""
# help_page.click_Chat()
# sleep(2)
# """Begin Chat"""
# help_page.clickBeginChat()
# sleep(2)
# """Select Subject from dropdown"""
# help_page.selectDropDownForSubject()
# sleep(2)
# help_page.selectSubjectFromDropDown()
# sleep(2)
# """Enter Problem Description"""
# help_page.fillDescription()
# sleep(2)
# """Select affected printer"""
# help_page.selectDropDownForAffectedPrinter()
# sleep(2)
# help_page.selectAffectedPrinterFromDropDown()
# sleep(2)
# """Start chat"""
# help_page.startChat()
# """Click Go to chat"""
# help_page.goToChat()
# """Check if chat bubble does not appear"""
# """Cannot check since chat bubble does not appear"""
