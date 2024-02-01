from turtle import up

import self
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import connect_device, device
import unittest
from ZSB_Mobile.Common_Method import Common_Method

from ZSB_Mobile.PageObject.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Add_A_Printer_Screen import Add_A_Printer_Screen


class iOS_App_Settings:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def test_AppSettings_TestcaseID_45688():
    """""""Install the latest production app on the phone"""""""
