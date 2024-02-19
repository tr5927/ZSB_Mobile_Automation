from time import sleep
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from poco import poco

class Smoke_Test_iOS:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.SignIn_With_Text = "Sign In With"
        self.Continue_With_Facebook_Option = "Continue with Facebook"
        self.Continue_With_Apple_Option = "Continue with Apple"
        self.home_Text_IS_Present = "Home"
        self.Facebook_UserName = Template(os.path.join(os.path.expanduser('~'),
                                                       "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\PageObject\Images",
                                                       "tpl1707806465367.png"), record_pos=(-0.169, -0.869),
                                          resolution=(1170, 2532))
        self.Continue_With_Password_ForApple_Login = "Continue with Password"
        self.click_On_Password_Text_field = "SecureTextField"
        self.Sign_In_Option = "Sign In"
        self.Apple_UserName = Template(os.path.join(os.path.expanduser('~'),
                                                       "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\PageObject\Images",
                                                     "tpl1707817586300.png"), record_pos=(-0.191, -0.867), resolution=(1170, 2532))

        self.Google_UserName = Template(os.path.join(os.path.expanduser('~'),
                                                       "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\PageObject\Images",
                                                     "tpl1707818376117.png"), record_pos=(-0.174, -0.867), resolution=(1170, 2532))


    def Verify_SignIn_With_Text_Is_Present(self):
        sleep(10)
        SignIn_With_Text = self.poco(self.SignIn_With_Text)
        SignIn_With_Text.get_text()
        return SignIn_With_Text

    def click_Continue_With_Facebook_Option(self):
        sleep(2)
        Continue_With_Facebook_Option = self.poco(self.Continue_With_Facebook_Option)
        Continue_With_Facebook_Option.click()
        sleep(20)

    def Verify_Facebook_UserName_Is_Displaying(self):
        sleep(3)
        assert_exists(self.Facebook_UserName, "Facebook UserName is displaying")

    def click_Continue_With_Apple_Option(self):
        sleep(2)
        Continue_With_Apple_Option = self.poco(self.Continue_With_Apple_Option)
        Continue_With_Apple_Option.click()
        sleep(20)

    def click_Continue_With_Password_ForApple_Login(self):
        sleep(2)
        Continue_With_Password_ForApple_Login = self.poco(self.Continue_With_Password_ForApple_Login)
        Continue_With_Password_ForApple_Login.click()

    def click_On_Password_Textfield(self):
        enter_apple_id_password = self.poco(self.click_On_Password_Text_field)
        enter_apple_id_password.click()
        sleep(2)

    def Enter_Apple_ID_Password(self):
        self.poco(text("Testing@123"))

    def click_On_Sign_In_Option(self):
        sleep(2)
        Sign_In_Option = self.poco(self.Sign_In_Option)
        Sign_In_Option.click()
        sleep(9)

    def Verify_Apple_UserName_Is_Displaying(self):
        sleep(3)
        assert_exists(self.Apple_UserName, "Apple UserName is displaying")

    def Verify_Google_UserName_Is_Displaying(self):
        sleep(3)
        assert_exists(self.Google_UserName, "Google UserName is displaying")


