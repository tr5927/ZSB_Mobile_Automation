# LoginFunction.py
from platform import platform

import pytest
from airtest.core.android import Android
from airtest.core.api import exists, sleep
from poco import poco
from ZSB_Mobile.Common_Method import Common_Method


class Login_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.LoginAllow_Popup = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
        self.loginBtn = "Login"
        self.Bluetooth_Allow = "android:id/button1"
        self.Google_Login = "Continue with Google"
        self.Enter_GoogleID_Field = "SWDVT IDC test account"
        self.Google_UserID = "identifierId"
        self.Emailid_Nextbtn = "identifierNext"
        self.Google_Password = "android.widget.TextView"
        self.Next_LoginBtn = "Next"
        self.Google_MailID = "Use another account"
        self.Password_Nextbtn = "passwordNext "
        self.Menu_Hamburger_Icn = "Open navigation menu"
        self.swdvt_test_account = "SWDVT IDC test account soho.swdvt.01@gmail.com"
        self.zebra_test_account_text = "zebratest850@gmail.com"



    def click_LoginAllow_Popup(self):
        loginallow = self.poco(self.LoginAllow_Popup)
        loginallow.click()

    def click_Bluetooth_Allow(self):
        bluetooth_allow = self.poco(self.Bluetooth_Allow)
        bluetooth_allow.click()

    def click_loginBtn(self):
        login_btn = self.poco(self.loginBtn)
        login_btn.click()

    def click_Loginwith_Google(self):
        google_login = self.poco(self.Google_Login)
        google_login.click()

    def click_GoogleID_Field(self):
        enter_googleID_field = self.poco(self.Enter_GoogleID_Field)
        enter_googleID_field.click()

    def Enter_Google_UserID(self):
        enter_googleid = self.poco(self.Google_UserID)
        enter_googleid.set_text("soho.swdvt.01@gmail.com")

    def click_GooglemailId(self):
        google_mailid = self.poco(self.Google_MailID)
        google_mailid.click()

    def Enter_Google_Password(self):
        enter_google_password = self.poco(self.Google_Password)
        sleep(2)
        enter_google_password.set_text("Swdvt@#123")

    def click_Next_LoginBtn(self):
        next_login_btn = self.poco(self.Next_LoginBtn)
        next_login_btn.click()

    def click_Emailid_Nextbtn(self):
        emailid_nextbtn = self.poco(self.Emailid_Nextbtn)
        emailid_nextbtn.click()

    def click_Password_Nextbtn(self):
        password_nextbtn = self.poco(self.Password_Nextbtn)
        password_nextbtn.click()

    def click_Menu_HamburgerICN(self):
        hamburgerIcn = self.poco(self.Menu_Hamburger_Icn)
        hamburgerIcn.click()

    def click_swdvt_account(self):
        swdvt_account = self.poco(self.swdvt_test_account)
        swdvt_account.click()

    def click_zebra_test_850_account(self):
        zt_account = self.poco(text = self.zebra_test_account_text)
        zt_account.click()

