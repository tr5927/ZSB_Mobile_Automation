import datetime
import os
import time
import random
import string

from airtest.core.api import *
# import pytest
# from pipes import Template
from poco import poco
from poco.exceptions import PocoNoSuchNodeException

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen

common_method = Common_Method(poco)


class Registration_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Register_Email = " Register Your Email Now"
        self.log_out_button = "Log Out"
        self.Google_Icon = Template(r"Google_Icon.png", record_pos=(-0.319, -0.173), resolution=(1080, 2340))
        self.Facebook_Icon = Template(r"Facebook_Icon.png", record_pos=(-0.316, 0.094), resolution=(1080, 2340))
        self.Apple_Icon = Template(r"Apple_Icon.png", record_pos=(-0.317, -0.043), resolution=(1080, 2340))
        self.Buy_More_Labels = "Buy More Labels"
        self.Connect = "Connect"
        self.Join_Network_Password_TextBox = Template(r"Join_Network_Password_TextBox.png", record_pos=(-0.127, 0.118),
                                                      resolution=(1080, 2340))
        self.submit = "Submit"
        self.Finish_Setup = "Finish Setup"
        self.Try_Again = "Try Again"
        self.Login = "Login"

    def clickSignIn(self):
        signInBtn = self.poco("Sign In")
        signInBtn.click()


    def registerEmail(self):
        self.poco(self.Register_Email).wait_for_appearance(timeout=10)
        self.poco(self.Register_Email).click()

    def click_on_reset_password(self):
        self.poco(" Reset Password").focus([0.2, 0.3]).click()

    def check_if_in_password_recovery_page(self):
        self.wait_for_element_appearance_text("Password Recovery", 20)

    def Enter_Username_password_recovery_page(self, email):
        self.poco("android.widget.EditText").set_text(email)

    def click_SUBMIT(self):
        self.poco(text="SUBMIT").click()

    def check_submit_is_clickable(self):
        return self.poco(text="SUBMIT", enabled=True).exists()

    def check_if_in_login_page(self):
        return self.poco(self.Login).exists()

    def check_zebra_mail_registration_error(self):
        try:
            self.wait_for_element_appearance_text("This site is for external users only. Please contact your local system administrator for application access request.")
        except:
            raise Exception("NO error when trying to register with zebra mail id.")

    def wait_for_element_appearance_text(self, element, time_out=15):
        self.poco(text=element).wait_for_appearance(timeout=time_out)

    def enter_user_email_for_registering(self, email):
        if self.poco(text="Cookie use").exists():
            self.poco(text="Reject All").click()
        self.poco("android.widget.EditText").set_text(email)

    def wait_for_element_appearance(self, element, time_out=10):
        self.poco(element).wait_for_appearance(timeout=time_out)

    def enter_the_verification_code(self, code):
        self.poco("android.widget.EditText").set_text(code)

    def fill_first_name_field(self, name):
        self.poco("android.widget.EditText")[0].click()
        self.poco("android.widget.EditText")[0].set_text(name)
        self.poco(text="First Name: *").click()

    def fill_last_name_field(self, name):
        self.poco("android.widget.EditText")[1].click()
        self.poco("android.widget.EditText")[1].set_text(name)
        self.poco(text="Last Name: *").click()

    def verify_if_all_fields_present(self):

        self.poco(text="First Name: *").exists()
        self.poco.scroll()
        self.poco(text="Last Name: *").exists()
        self.poco(text="Password: *").exists()
        self.poco(text="Confirm Password: *").exists()
        self.poco(text="Select Country *").exists()

    def verify_if_checkboxes_are_present_registration(self):
        self.poco(text="I'd like to receive marketing emails").exists()
        self.poco(text=" I have read and agree to the ").exists()

    def special_character_error_name_field(self, field_name, value):
        if field_name == "First Name":
            self.poco("android.widget.EditText")[0].click()
            self.poco("android.widget.EditText")[0].set_text(value)
            self.poco(text="First Name: *").click()
        elif field_name == "Last Name":
            self.poco("android.widget.EditText")[1].click()
            self.poco("android.widget.EditText")[1].set_text(value)
            self.poco(text="Last Name: *").click()
        sleep(2)
        return self.poco(text="Please do not use any special characters or numerical digits.").exists()

    def check_error_password_field(self, value, swipe=False):
        if swipe:
            temp2 = self.poco("android.widget.EditText")[0]
            temp1 = self.poco(text="signup.zebra.com")
            temp2.drag_to(temp1)
        sleep(3)
        self.poco("android.widget.EditText")[2].click()
        sleep(2)
        self.poco("android.widget.EditText")[2].set_text(value)
        self.poco(text="Password: *").click()
        sleep(2)
        return self.poco(
            text="Password MUST be at least 12 characters. Password MUST contain one lowercase, one uppercase letter, one number and a special character. Password MUST NOT contain spaces or tabs.").exists()

    def fill_password_field(self, value):
        self.poco("android.widget.EditText")[2].click()
        self.poco("android.widget.EditText")[2].set_text(value)
        self.poco(text="Confirm Password: *").click()

    def fill_confirm_password_field(self, value):
        self.poco("android.widget.EditText")[3].click()
        self.poco("android.widget.EditText")[3].set_text(value)
        self.poco(text="Confirm Password: *").click()

    def check_password_unmatch_error(self):
        return self.poco("Password and Confirm Password must match.").exists()

    def enter_the_fields(self, firstname, lastname, password):
        scroll_view = self.poco("android.webkit.WebView")
        while self.poco(text="Enter User Information ").exists():
            scroll_view.swipe("up")

        self.poco("android.widget.EditText")[0].set_text(firstname)

        self.poco("android.widget.EditText")[1].set_text(lastname)

        self.poco("android.widget.EditText")[2].set_text(password)

        self.poco("android.widget.EditText")[3].set_text(password)

    def select_the_country(self, country):
        self.poco(text="-- Select --").click()
        scroll_view = self.poco("android.widget.ListView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 26
        for _ in range(max_swipes):
            # Swipe up on the ScrollView
            scroll_view.scroll()

            # Check if the "Accept" element is present and enabled
            search = self.poco(text=country)
            if search.exists():
                self.poco(text=country).click()
                # Accept button is visible and enabled, break out of the loop
                break

    def select_the_check_boxes(self):

        self.poco("android.widget.CheckBox")[0].click()

        self.poco("android.widget.CheckBox")[1].click()

    def click_clear(self):
        self.poco("android.widget.Button").click()

    def check_error_message_after_clear(self):
        return self.poco("This field is required.").exists()

    def click_submit_and_continue(self):
        start_point = [0.5, 0.7]
        end_point = [0.5, 0.4]
        for i in range(1):
            self.poco.swipe(start_point, end_point, duration=0.1)
        self.poco(text="SUBMIT AND CONTINUE").click()

    def check_sign_up_successful(self):
        self.poco("CONTINUE").wait_for_appearance(timeout=30)
        self.poco("CONTINUE").wait_for_appearance(timeout=30)
        self.poco(text="ZSB Printer registration completed.").exists()
        self.poco(text="Success! Click \"continue\" to log into your account.").exists()

    def click_continue_registration_page(self):
        self.poco("CONTINUE").click()

    def check_email_already_exists_page_title(self):
        try:
            self.wait_for_element_appearance_text("ZSB Printer Account Already Exist.")
        except:
            raise Exception("Email already exists message did not appear.")

    def check_email_already_Exists_page_message(self):
        try:
            self.wait_for_element_appearance_text("You already have an account with us, Please click the below \"Continue\" button to redirect to the application.")
        except:
            raise Exception(
                "\"You already have an account with us, Please click the below \"Continue\" button to redirect to the application.\" did not appear.")

    def check_email_verification_page_message(self):
        try:
            self.wait_for_element_appearance_text("Your request has been received. We have sent a verification code through your email to verify your account. Please enter your verification code below to finish registration. Can't find your email? Please check your junk mail or click this link: ")
        except:
            raise Exception(
                "\"Your request has been received. We have sent a verification code through your email to verify your account. Please enter your verification code below to finish registration. Can't find your email? Please check your junk mail or click this link: \" did not appear.")

    def check_email_verified_successfully_message(self):
        return self.poco(text="Email verified successfully!").exists()

    def verify_resend_verification_code_btn_exists(self):
        return self.poco("Resend Verification Code.").exists()

    def click_resend_verification_code_btn(self):
        self.poco("Resend Verification Code.").focus([0.99, 0.01]).click()

    def verify_user_information_and_account_security_page(self):
        try:
            self.wait_for_element_appearance_text("ZSB Printer User Information and Account Security")
        except:
            raise Exception("Did not navigate to 'ZSB Printer User Information and Account Security' page.")

    def verify_verification_code_expired_error(self):
        return self.poco(textMatches=".*Token has expired. Please use 'Resend Verification Code' link to regenerate token.").exists()

    def click_on_sign_in_with_email(self):
        sign_in_with_email = self.poco("android.widget.Button")
        sign_in_with_email.click()

    def complete_sign_in_with_email(self, user_name, password, click_on_sign_in=1, click_back=1, wrong_password=False,
                                    enter_only_password=False):

        if click_back:
            keyevent("back")
        if not enter_only_password:
            if self.poco("com.android.chrome:id/coordinator"):
                self.poco("com.android.chrome:id/coordinator").click()
            keyevent("Enter")
            self.poco("android.widget.EditText")[0].wait_for_appearance(timeout=10)
            self.poco("android.widget.EditText")[0].set_text(user_name)
            keyevent("Enter")
        self.poco("android.widget.EditText")[1].wait_for_appearance(timeout=10)
        self.poco("android.widget.EditText")[1].set_text(password)
        # self.poco(text="Sign In").click()
        if click_on_sign_in:
            self.poco("android.widget.Button")[1].click()
        if wrong_password:
            try:
                self.poco("We didn't recognize the username or password you entered. Please try again.")
            except:
                raise Exception("Error message not displayed for wrong password.")

    def click_on_profile_edit(self):
        self.poco("android.widget.Button").click()

    def verify_if_on_EULA_page(self):
        try:
            self.wait_for_element_appearance("Click ‘Accept’ to indicate that you have read and agree to the ", 20)
        except:
            raise Exception("Did not reach EULA page")

    def check_user_does_not_exist_error(self):
        return self.poco(text="User does not exist.").exists()

    def click_accept(self):
        self.poco("Accept").click()

    def click_decline(self):
        self.poco("Decline").click()

    def click_log_out_button(self):
        log_out_btn = self.poco(self.log_out_button)
        log_out_btn.click()

    def click_Google_Icon(self):
        touch(self.Google_Icon)

    def click_Facebook_Icon(self):
        touch(self.Facebook_Icon)

    def click_Apple_Icon(self):
        touch(self.Apple_Icon)

    def click_on_next(self):
        self.poco(text="Next").click()

    def addAccountToDevice(self):
        add_acc = self.poco(text="Add account to device")
        add_acc.click()

    def sign_In_With_Google(self, password, username=None, wrong_password=False):
        if username is not None:
            try:
                self.poco("android.widget.EditText").wait_for_appearance(timeout=10)
                self.poco("android.widget.EditText").set_text(username)
            except:
                self.poco("identifierId").wait_for_appearance(timeout=10)
                self.poco("identifierId").set_text(username)
            keyevent("enter")
            self.poco("android.widget.Button")[-1].click()
        self.poco("android.widget.EditText").wait_for_appearance(timeout=10)
        self.poco("android.widget.EditText").set_text(password)
        keyevent("enter")
        if wrong_password:
            try:
                self.wait_for_element_appearance_text(
                    "Wrong password. Try again or click Forgot password to reset it.")
            except:
                raise Exception(
                    "Error message: \"Wrong password. Try again or click Forgot password to reset it.\" not displayed.")
        else:
            self.poco("android.widget.Button")[-1].click()
            try:
                scrolls = 5
                while scrolls!=0:
                    poco.scroll()
                if self.poco(text="Skip").exists():
                    self.poco(text="Skip").click()
            except:
                pass
            while not self.poco(text="I agree").exists():
                self.poco.scroll()
            self.poco(text="I agree").click()

    def get_login_name_from_menu(self):
        name = self.poco("android.view.View")[4].child().child().child().get_name().split("\n")[1]
        return name

    def login_Facebook(self, password, username=None, wrong_password=False):
        if username is not None:
            self.poco("android.widget.EditText").wait_for_appearance(timeout=10)
            self.poco("android.widget.EditText").set_text(username)
        self.poco("android.widget.EditText")[1].wait_for_appearance(timeout=10)
        self.poco("android.widget.EditText")[1].set_text(password)
        keyevent("Enter")
        self.poco("android.widget.Button").click()
        if wrong_password:
            try:
                self.wait_for_element_appearance_text("Incorrect password. ")
                self.wait_for_element_appearance_text("Did you forget your password?")
            except:
                raise Exception("Error message \"Incorrect password. Did you forget your password?\"not displayed for wrong password.")
        sleep(3)
        if self.poco(text="Continue as Zsb").exists():
            self.poco(text="Continue as Zsb").click()

    def login_Apple(self, password, username=False, wrong_password=False):
        if username:
            self.poco("android.widget.EditText").wait_for_appearance(timeout=10)
            self.poco("android.widget.EditText").set_text(username)
            self.poco("android.widget.Button")[1].click()
            if self.poco("com.android.chrome:id/coordinator").exists():
                self.poco("com.android.chrome:id/coordinator").click()
        self.poco("android.widget.EditText")[1].wait_for_appearance(timeout=10)
        self.poco("android.widget.EditText")[1].set_text(password)
        self.poco(text="Sign In").click()#changed during datasources test id- 45731
        if wrong_password:
            self.poco("android.widget.TextView")[7].click()
            error_message = [self.poco("android.widget.TextView")[11].get_text()][0]
            print(error_message)
            if error_message == "Your Apple\xa0ID or password was incorrect.":
                print("Successfully displayed Error message for wrong password")
                return
            else:
                print("Error message not displayed for wrong password.")
                raise Exception("Error message not displayed for wrong password.")

    def home_page_overview(self, firstname):
        self.poco(f"Hey {firstname}\nAdd a printer to get started. We’ll help you set things up.")

    def check_add_a_printer_exists(self):
        self.poco("Add A Printer").exists()

    def check_buy_more_labels_exists(self):
        return self.poco(self.Buy_More_Labels).exists()

    def click_Buy_More_Labels(self):
        self.poco(self.Buy_More_Labels).wait_for_appearance(timeout=25)
        self.poco(self.Buy_More_Labels).click()

    def clickRadioButton(self):
        self.poco("android.widget.RadioButton").wait_for_appearance(timeout=15)

    def clickConnect(self):
        self.poco(self.Connect).wait_for_appearance(timeout=20)
        self.poco(self.Connect).click()

    def Enter_Password_Join_Network(self):
        touch(self.Join_Network_Password_TextBox)

    def clickSubmit(self):
        self.poco(self.submit).click()

    def selectPrinter(self, printername):
        no_of_devices_displayed = len(self.poco("android.view.View")[5].child())
        last_device_displayed = self.poco("android.view.View")[5].child()[no_of_devices_displayed - 1].get_name()
        while True:
            for i in range(no_of_devices_displayed):
                displayed_printer_name = self.poco("android.view.View")[5].child()[i]
                if displayed_printer_name.get_name() == printername:
                    displayed_printer_name.child().click()
                    return
            common_method.swipe_screen([0.5, 0.8141025641025641], [0.5, 0.191], 1)
            new_last_device_displayed = self.poco("android.view.View")[5].child()[
                no_of_devices_displayed - 1].get_name()
            if new_last_device_displayed == last_device_displayed:
                raise Exception("Printer not found")
            last_device_displayed = new_last_device_displayed

    def clickFinishSetup(self):
        self.poco(self.Finish_Setup).wait_for_appearance(timeout=100)
        self.poco(self.Finish_Setup).click()

    def checkWiFiGreen(self):
        if self.poco("Need the Printer Driver?").exists():
            return True
        else:
            return False

    def timeTillWiFiGreen(self):
        start_time = time.time()
        while not self.checkWiFiGreen():
            pass
        end_time = time.time()
        time_taken = end_time - start_time
        return time_taken

    def verifyTurnOnBluetoothPopUp(self):
        if self.poco("Turn on Bluetooth to Allow “ZSB Printer App” to Connect.").exists():
            return
        else:
            raise Exception("Bluetooth is already on")

    def verifyUnableToPairPrinterError(self):
        # sleep(30)
        if self.poco("Unable to pair your printer").exists():
            pass
        else:
            raise Exception("Connection Error did not appear")

    def checkIfBluetoothConnectedSuccessfully(self):
        sleep(30)
        self.poco("Searching for Wi-Fi Networks").exists()

    def clickTryAgain(self):
        self.poco(self.Try_Again).click()

    def check_if_on_success_page(self):
        return self.poco(text="Success!").exists()

    def check_message_on_success_page(self):
        return_message = False
        if self.poco(text="An email with a Password Reset Code has been sent to your email address.").exists():
            if self.poco(text="The OTP will expire in 10 minutes").exists():
                return_message = True
        return return_message

    def click_on_Click_here(self):
        self.poco("Click here ").click()

    def click_on_click_here(self):
        self.poco("click here").click()

    def check_if_on_Reset_Password_page(self):
        self.wait_for_element_appearance_text("Reset Password")

    def check_fields_on_Reset_Password_page(self):
        self.poco(text="Password Reset Code*").exists()
        self.poco(text="New Password*").exists()
        self.poco(text="Confirm Password*").exists()

    def check_error_message_on_fields_on_Reset_Password_page(self):
        return_message = False
        if self.poco("android.widget.TextView")[1].get_text() == "This field is required.":
            if self.poco("android.widget.TextView")[2].get_text() == "This field is required.":
                if self.poco("android.widget.TextView")[3].get_text() == "This field is required.":
                    return_message = True
        return return_message

    def fillPasswordResetCode(self, resetCode):
        self.poco("android.widget.EditText").set_text(resetCode)

    def fillNewPassword(self, password):
        self.poco("android.widget.EditText")[1].set_text(password)

    def fillConfirmPassword(self, password):
        self.poco("android.widget.EditText")[2].set_text(password)

    def checkWrongConfirmPasswordErrorMessage(self):
        return self.poco("android.widget.TextView")[1].get_text() == "Fields do not match."

    def check_OTExpiredMessage(self):
        return_message = False
        if self.poco(text="The OTP was invalid or expired. Please ").exists():
            if self.poco("click here").exists():
                if self.poco(text=" to regenerate OTP.").exists():
                    return_message = True
        return return_message

    def check_successful_password_reset_page_message(self):
        self.poco(text="Password changed successfully.").exists()
        self.poco("Click here").exists()
        self.poco(text="to login with your new password.").exists()

    def check_if_in_zebra_network_account_password_reset_page(self):
        title = self.poco("android.widget.TextView")[3].get_text().split('\n')
        return title[0] == "Reset your Zebra network account (Active Directory) password."

    def check_fields_in_zebra_network_account_password_reset_page(self):
        self.poco(text="User name").exists()
        self.poco(text="CAPTCHA").exists()
        self.poco("android.widget.CheckBox").exists()

    def fill_username_in_zebra_network_account_password_reset_page(self, username):
        self.poco("android.widget.EditText").set_text(username)

    def enableCaptcha(self):
        self.poco("android.widget.CheckBox").click()

    def checkSkipExists(self):
        return self.poco(text="SKIP").exists()

    def clickSkip(self):
        self.poco(text="SKIP").click()

    def checkVerifyExists(self):
        return self.poco(text="VERIFY").exists()

    def clickVerify(self):
        self.poco(text="VERIFY").click()

    def generate_random_word(self, word_length):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(word_length))

    def check_Message_in_Password_Reset_Error_Page(self):
        self.poco(text="This user cannot use the configured Password Reset process. Possible reasons:").exists()
        self.poco(text="User does not exist or is not enrolled.").exists()
        self.poco(text="User is not part of the configured password reset process.").exists()
        self.poco(text="User account is locked.").exists()
        self.poco(text="Try again later. For immediate assistance, call the service desk.").exists()

    def create_google_account(self):
        os.system("adb shell am start -a android.settings.SYNC_SETTINGS")
        while not self.poco(text="Add account").exists():
            self.poco.scroll()
        self.poco(text="Add account").click()
        self.poco(text="Google").wait_for_appearance(timeout=20)
        self.poco(text="Google").click()
        self.poco(text="Create account", enabled=True).wait_for_appearance(timeout=30)
        sleep(3)
        self.poco(text="Create account").click()
        self.poco(text="For my personal use").click()
        name = self.generate_random_word(10)
        self.poco("firstName").wait_for_appearance(timeout=20)
        sleep(2)
        self.poco("firstName").click()
        self.poco("firstName").set_text(name)
        keyevent("Enter")
        self.poco(text="Next").click()
        self.poco(text="Month").wait_for_appearance(timeout=20)
        self.poco(text="Month").click()
        self.poco("android.widget.ListView").wait_for_appearance(timeout=20)
        month_length = len(self.poco("android.widget.ListView").child())
        i = random.randint(0, month_length - 1)
        self.poco("android.widget.ListView").child()[i].click()
        day = random.randint(1, 28)
        try:
            self.poco("day").set_text(day)
        except:
            self.poco("android.widget.EditText").set_text(day)
        year = random.randint(1990, 2007)
        try:
            self.poco("year").set_text(year)
        except:
            self.poco("android.widget.EditText")[1].set_text(year)
        self.poco(text="Gender").click()
        gender_length = len(self.poco("android.widget.ListView").child())
        i = random.randint(0, gender_length-2)
        self.poco("android.widget.ListView").child()[i].click()
        self.poco(text="Next").click()
        self.poco(text="Create your own Gmail address").wait_for_appearance(timeout=20)
        self.poco(text="Create your own Gmail address").click()
        self.poco("android.widget.EditText").set_text(name)
        keyevent("Enter")
        password = self.generate_random_word(10) + '@1234'
        self.poco("android.widget.EditText").wait_for_appearance(timeout=20)
        sleep(2)
        self.poco("android.widget.EditText").set_text(password)
        keyevent("Enter")
        self.poco(text="Next").click()
        sleep(3)
        self.poco(text="Next").click()
        if self.poco(text="Skip").exists():
            self.poco(text="Skip").click()
            self.poco(text="Next").click()
        username = name + '@gmail.com'
        print(username)
        while not self.poco(text="I agree").exists():
            self.poco.scroll()
        self.poco(text="I agree").click()
        self.wait_for_element_appearance_text("Add account", 20)
        return username, password

    def verifyLinksInSignInPage(self):
        while not self.poco("Legal Notice").exists():
            self.poco.scroll()
        link_1 = self.poco("Zebra.com", enabled=True).exists()
        link_2 = self.poco("Legal Notice", enabled=True).exists()
        link_3 = self.poco("Privacy Statement", enabled=True).exists()
        return link_1 and link_2 and link_3

    def add_contacts_google_account(self, email, password):
        os.system("adb shell am start -a android.settings.SYNC_SETTINGS")
        self.poco(text=email).click()
        self.poco(text="Google Account").click()
        self.wait_for_element_appearance_text("Home")
        self.poco.swipe(self.poco(text="Data and privacy").get_position(), self.poco(text="Home").get_position())
        self.poco.swipe(self.poco(text="Security").get_position(), self.poco(text="Data and privacy").get_position())
        self.poco(text="People and sharing").click()
        self.poco(text="Contacts")[1].click()
        self.poco("android.widget.EditText").set_text(email)
        self.poco("android.widget.EditText").set_text(password)
        keyevent("Enter")
        if self.poco(text="Stay on web").exists():
            self.poco(text="Stay on web").click()
        self.poco(text="Add new contact").click()

    def clickClose(self):
        self.poco("android.widget.Button").click()

    def clickExit(self):
        self.poco("Exit").click()

