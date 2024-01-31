# LoginFunction.py
from platform import platform
from airtest.core.api import *
import pytest
from airtest.core.android import Android
from airtest.core.api import exists, sleep
from poco import poco
from ZSB_Mobile.Common_Method import Common_Method
from poco.exceptions import PocoNoSuchNodeException
from pocoui_lib.android.kotoComponent import poco


class Add_A_Printer_Screen_iOS:
    pass

    def __init__(self, poco):
        self.poco = poco

        self.Add_A_Printer_Btn = "Add A Printer"
        self.Start_Btn = "Start"
        self.Searching_For_Your_Printer_Text = "Searching for your printer"
        self.Printer_LED_Not_Flashing_Text = "My Printer’s LED is Not Flashing Blue What Does The LED Light Indicator Mean"
        self.To_Find_Your_Printer_Text = "To find your printer, please ensure your printer’s LED is flashing blue like the example below."

        """"need to replace the image path  & details"""
        self.Printer_LED_Image = (Template(r"tpl1705903757611.png", record_pos=(-0.007, 0.041), resolution=(1080, 2400)))

    def enable_bluetooth(self):
        os.system('adb shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE')
        shell_element = poco(text="Allow")
        try:
            shell_element.exists()
            shell_element.click()
            sleep(1)
        except Exception as e:
            print(f"An error occurred: {e}. Skipping.")

    def disable_bluetooth(self):
        os.system('adb shell am start -a android.bluetooth.adapter.action.REQUEST_DISABLE')
        shell_element = poco(text="Allow")
        try:
            shell_element.exists()
            shell_element.click()
            sleep(1)
        except Exception as e:
            print(f"An error occurred: {e}. Skipping.")

    def click_Add_A_Printer(self):
        add_a_printer_btn = self.poco(self.Add_A_Printer_Btn)
        add_a_printer_btn.click()

    def click_Start_Button(self):
        sleep(2)
        start_btn = self.poco(self.Start_Btn)
        start_btn.click()

    def Verify_Searching_for_your_printer_Text(self):
        searching_for_printer_text = self.poco(self.Searching_For_Your_Printer_Text)
        searching_for_printer_text.get_text()
        print(" Searching for your printer text is displaying:", searching_for_printer_text)
        return searching_for_printer_text

    def Verify_Printer_LED_Not_Flashing_Text(self):
        printer_led_not_flashing_text = self.poco(self.Printer_LED_Not_Flashing_Text)
        printer_led_not_flashing_text.get_text()
        print(" Printer led not flashing text is displaying:", printer_led_not_flashing_text)
        return printer_led_not_flashing_text

    def Verify_To_Find_Your_Printer_Text(self):
        To_Find_Your_Printer_text = self.poco(self.To_Find_Your_Printer_Text)
        To_Find_Your_Printer_text.get_text()
        print(" To Find Your Printer text is displaying:", To_Find_Your_Printer_text)
        return To_Find_Your_Printer_text

    def Verify_Printer_LED_Image(self):
        assert_exists(self.Printer_LED_Image, "Printer LED Image is present")
