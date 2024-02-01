from turtle import up

import self
from poco import poco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

import ZSB_Mobile.TestExecution.test_Help
import ZSB_Mobile.TestExecution.test_App_Settings
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Data_Sources_Screen import Data_Sources_Screen
from ZSB_Mobile.PageObject.Login_Screen import *

from ZSB_Mobile.PageObject.Add_A_Printer_Screen import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.APP_Settings_Screen import App_Settings_Screen
from ZSB_Mobile.PageObject.Help_Screen import Help_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Printer_Management_Screen import Printer_Management_Screen


class Android_App_Help:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
start_app("com.zebra.soho_app")
sleep(2.0)


