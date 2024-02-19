from time import sleep


class Login_Screen_iOS:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.loginBtn = "Login"
        self.Continue_popup_to_login = "Continue"
        self.Enter_GoogleID_Field = "SWDVT IDC test account"
        self.Google_Login = "Continue with Google"
        self.Bluetooth_Allow = " "
        self.Google_MailID = "Use another account"
        self.Password_Nextbtn = "Next "
        self.Menu_Hamburger_Icn = "Open navigation menu"
        self.Google_UserID = "identifierId"
        self.Emailid_Nextbtn = "identifierNext"
        self.Google_Password = "Enter your password"
        self.Next_LoginBtn = "Next"
        self.LoginAllow_Popup = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
    def clcik_Login_Btn(self):
        login_btn = self.poco(self.loginBtn)
        login_btn.click()

    def click_Continue_Btn(self):
        Continue_btn = self.poco(self.Continue_popup_to_login)
        Continue_btn.click()

    def click_GoogleID_Field(self):
        enter_googleID_field = self.poco(self.Enter_GoogleID_Field)
        enter_googleID_field.click()

    def click_Loginwith_Google(self):
        google_login = self.poco(self.Google_Login)
        google_login.click()

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
        hamburgerIcn = self.poco(self.Menu_Hamburger_Icn)
        hamburgerIcn.click()

    def click_LoginAllow_Popup(self):
        loginallow = self.poco(self.LoginAllow_Popup)
        loginallow.click()

    def click_Enter_Password_Field(self):
        enter_google_password = self.poco(self.Google_Password)
        enter_google_password.click()
