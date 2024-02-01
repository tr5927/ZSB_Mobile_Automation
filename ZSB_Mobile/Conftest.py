# conftest.py
import os.path
import shutil
from datetime import time
from platform import platform
from urllib import request

import pytest
from airtest.core.android.adb import ADB
from airtest.core.api import auto_setup, sleep, start_app
from jinja2 import Environment, FileSystemLoader
import logging


from platform import platform

import pytest
from airtest.core.android import Android
from airtest.core.api import connect_device, device
from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# if platform= "Android"
# device_info = {
#     "platform": "Android",  # or "iOS"
#     "device": "2A051JEGR15175",  # specify the device ID or name
#     # Add other device-specific information as needed
# }
#
# # Connect to the device
# connect_device("Android:///" + device_info["device"])
# start_app("com.zebra.soho_app")
# sleep(2.0)

@pytest.fixture(autouse=True)
def tc_setup():
    print("Launch app")
    print("Login")
    yield
    print("Logoff")
    print("close browser")

"""---------------------------------------------------------------------------------------------------------------------"""

#file_path = 'path to text file.txt'
#
# udid_array = []
#
# # Open the file and read lines
# with open(file_path, 'r') as file:
#     for line in file:
#         # Append each line to the list, removing newline characters
#         udid_array.append(line.strip())

import openpyxl

excel_file_path = 'Book1.xlsx'
udid_list = []

workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook.active

for udid in sheet.iter_rows(min_col=1, max_col=1, values_only=True):
    udid_list.append(udid[0])

for i in udid_list:
    connect_device(f"iOS:///{i}")
    poco = iosPoco

"""---------------------------------------------------------------------------------------------------------------------"""

def pytest_addoption(parser):
    parser.addoption("--Android", action="store", default="default_value", help="Specify the Android option.")

    if platform == "Android":
        connect_device("Android:///")
        poco = AndroidUiautomationPoco()
    elif platform == "iOS":
        connect_device("iOS:///00008101-00051D400144001E")
        poco = iosPoco()
    else:
        raise ValueError(f"Unsupported platform: {platform}")

    # Setup
    yield poco

    # Teardown
    device().stop_app()


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default=None, help="Specify the platform (android/ios)")


