from time import sleep
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException

class Login_Screen_iOS:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.loginBtn = "Login"
        self.Continue_popup_to_login = "Continue"
        self.Enter_GoogleID_Field = "SWDVT IDC test account"
        self.Google_Login = "Continue with Google"
        self.Bluetooth_Allow = "android:id/button1"
        self.Google_MailID = "Use another account"
        self.Password_Nextbtn = "Next "
        self.Menu_Hamburger_Icn = "Open navigation menu"
        self.Google_UserID = "identifierId"
        self.Emailid_Nextbtn = "identifierNext"
        self.Google_Password = "Enter your password"
        self.Next_LoginBtn = "Next"
        self.LoginAllow_Popup = "Continue"
        self.Allow_ZSB_Series_Popup = ""
        self.Use_Another_Account = "Use another account"
        self.Google_MailID = "Use another account"
        self.Password_Nextbtn = "passwordNext "
        self.UserName = "TextField"
        self.Password_Field = "SecureTextField"
        self.SignIn_Button = "Sign In"
        self.Login_With_ZebraEmail = "Sign In with your email"



    def clcik_Login_Btn(self):
        login_btn = self.poco(self.loginBtn)
        login_btn.click()

    def click_Continue_Btn_To_Login(self):
        sleep(2)
        Continue_btn = self.poco(self.Continue_popup_to_login)
        Continue_btn.click()

    def click_loginBtn(self):
        sleep(3)
        login_btn = self.poco(self.loginBtn)
        login_btn.click()
        login_btn.click()


    def click_GoogleID_Field(self):
        enter_googleID_field = self.poco(self.Enter_GoogleID_Field)
        enter_googleID_field.click()

    def click_Loginwith_Google(self):
        google_login = self.poco(self.Google_Login)
        google_login.click()
        sleep(10)

    def click_Bluetooth_Allow(self):
        bluetooth_allow = self.poco(self.Bluetooth_Allow)
        bluetooth_allow.click()

    def click_GooglemailId(self):
        google_mailid = self.poco(self.Google_MailID)
        google_mailid.click()

    def Enter_Google_UserID(self):
        enter_googleid = self.poco(self.Google_UserID)
        enter_googleid.set_text("soho.swdvt.01@gmail.com")

    def click_Emailid_Nextbtn(self):
        emailid_nextbtn = self.poco(self.Emailid_Nextbtn)
        emailid_nextbtn.click()

    def Enter_Google_Password(self):
        enter_google_password = self.poco(self.Google_Password)
        sleep(2)
        enter_google_password.set_text("Swdvt@#123")

    def click_Password_Nextbtn(self):
        password_nextbtn = self.poco(self.Password_Nextbtn)
        password_nextbtn.click()

    def click_Menu_HamburgerICN(self):
        sleep(4)
        hamburgerIcn = self.poco(self.Menu_Hamburger_Icn)
        hamburgerIcn.click()

    def click_LoginAllow_Popup(self):
        loginallow = self.poco(self.LoginAllow_Popup)
        loginallow.click()

    def click_Next_LoginBtn(self):
        next_login_btn = self.poco(self.Next_LoginBtn)
        next_login_btn.click()

    def click_Enter_Password_Field(self):
        enter_google_password = self.poco(self.Google_Password)
        enter_google_password.click()

    def click_Allow_ZSB_Series_Popup(self):
        sleep(3)
        Allow_ZSB_Series_Popup = self.poco(self.Allow_ZSB_Series_Popup)
        if Allow_ZSB_Series_Popup.exists():
            Allow_ZSB_Series_Popup.click()
        else:
            # pytest.skip("Allow ZSB Series Popup does not exist, skipping test.")
            print("Element not found, proceeding with the next part of the code.")

    # def Verify_LoginAllow_Popup_IS_Not_Displaying(self):
    #     if assert_not_exists(self.poco(self.LoginAllow_Popup), "Login Allow pop up is not there"):
    #         print("Pass")
    #     else:
    #         print("Fail")

    def Verify_LoginAllow_Popup_IS_Not_Displaying(self):
        sleep(2)
        if self.poco(self.LoginAllow_Popup).exists():
            print("Fail")
        else:
            print("Pass")

    def click_Login_With_Email_Tab(self):
        sleep(7)
        touch(self.Login_With_ZebraEmail)
        # login_with_email = self.poco(self.Login_With_Email)
        # # login_with_email.click()
        # if login_with_email.exists():
        # login_with_email.click()
        # else:
        #     print("Login with email element not found.")

    def click_UserName_TextField(self):
        username = self.poco(self.UserName)
        username.click()

    def Enter_UserName(self):
        username = self.poco(self.UserName)
        username.set_text("soho.swdvt.01@gmail.com")

    def click_Password_TextField(self):
        password = self.poco(self.Password_Field)
        password.click()

    def Enter_Password(self):
        password = self.poco(self.Password_Field)
        sleep(2)
        password.set_text("Swdvt@#123")

    def click_SignIn_Button(self):
        signin = self.poco(self.SignIn_Button)
        signin.click()
        sleep(7)

    def Check_loginBtn_IS_Present(self):
        sleep(5)
        login_btn = self.poco(self.loginBtn)
        if login_btn.exists():
            # Click on the "OK" or "Allow" button
            login_btn.click()
            print("Login Button is enabled.")
            return True
        else:
            print("Login Button is not enabled.")
            return False

    def Enter_Zebra_UserName(self):
        sleep(2)
        username = self.poco(self.UserName)
        username.set_text("Zebra01.swdvt@icloud.com")

    def Enter_Zebra_Password(self):
        password = self.poco(self.Password_Field)
        password.set_text("Testing@1234")

