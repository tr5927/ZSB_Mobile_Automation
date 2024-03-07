# LoginFunction.py
from platform import platform

import pytest
from _pytest.outcomes import skip
from airtest.core.android import Android
from airtest.core.api import exists, sleep
from poco import poco
from ZSB_Mobile.Common_Method import Common_Method
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from pocoui_lib.android.kotoComponent import poco


class Smoke_Test_Android:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.LoginAllow_Popup =""