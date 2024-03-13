import requests
import self
from airtest.core.api import *
from airtest.core.api import sleep
from urllib3.util import url

# from setuptools.config._validate_pyproject.formats import url

from ZSB_Mobile.Common_Method import Common_Method
from poco.exceptions import PocoNoSuchNodeException
from pocoui_lib.android.kotoComponent import poco
import os


class APS_Notification:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Files_Folder = "Files"
        self.Three_Dot_Icon_Next_To_PDF = "More options"
        self.PDF_Share_Option = "com.google.android.apps.docs:id/title"
        self.Print_Option = "Print"
        self.Notification_Is_Not_Displaying = "android:id/text"
        self.Notification_To_Login = "android:id/text"
        self.Available_Printer_To_Print = ""
        self.Downloads_Tab = "com.google.android.apps.nbu.files:id/search_suggestion_text"
        self.Mobile_SearchBar = "com.google.android.apps.nexuslauncher:id/hotseat"
        self.Drive_SearchBar = "com.google.android.apps.nbu.files:id/open_search_bar_text_view"
        self.Searchbar2 = "com.google.android.apps.nexuslauncher:id/input"
        self.Drive_SearchBar2 = "com.google.android.apps.nbu.files:id/search_box"
        self.Settings = "Settings"
        self.Connected_Devices = "android:id/title[1]"
        self.ZSB_Series = "android:id/title"
        self.Turn_ON_ZSB_Series_Printer = "android:id/switch_widget"
        self.Mobile_back_icon = "Navigate up"
        self.Mobile_Footer_Back_Icon = "com.android.systemui:id/back"
        self.Suggestion_PDF_File = "com.google.android.apps.nbu.files:id/search_suggestion_text"
        self.PDF_ON_Result = "com.google.android.apps.nbu.files:id/title"
        self.Print_Review_Page = "com.android.printspooler:id/preview_page"
        self.Save_AS_PDF = "com.android.printspooler:id/title"
        self.All_Printers = "All printers…"
        self.Share_Option = "com.google.android.apps.nbu.files:id/share_action"

    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def click_Device_Files_Folder(self):
        start_app("com.android.documentsui")
        wait(Template("files_app.png"), timeout=10)
        touch(Template("downloads_folder.png"))

    def click_Files_Folder(self):
        sleep(3)
        Files_Folder = self.poco(self.Files_Folder)
        if Files_Folder.exists():
            Files_Folder.click()
            sleep(2)
        else:
            print("Searchbar is not there")
        sleep(3)

    # def click_PDF_File_From_The_List(self):
    #     sleep(2)
    #     poco.scroll(self.PDF_File_From_The_List).exists()
    #     sleep(1)
    #     touch(self.PDF_File_From_The_List)
    #     sleep(3)

    # def click_PDF_File_From_The_List(self):
    #     sleep(2)  # Add a sleep for 2 seconds before scrolling
    #     if poco.scroll(self.PDF_File_From_The_List, direction='up').exists():  # Scroll vertically
    #     sleep(4)  # Adjusted sleep time if necessary
    #     touch(self.PDF_File_From_The_List)
    #     sleep(3)  # Add a sleep for 3 seconds after clicking the file
    #     else:
    #          print("PDF file not found in the list")

    def click_PDF_File_From_The_List(self):
        sleep(2)
        SearchBar2 = self.poco(self.Drive_SearchBar2)
        SearchBar2.set_text(" ")
        sleep(3)
        SearchBar2.set_text("pdf")
        sleep(3)

    def click_JPG_Image_File_From_The_List(self):
        sleep(2)
        SearchBar2 = self.poco(self.Drive_SearchBar2)
        SearchBar2.set_text(" ")
        sleep(3)
        SearchBar2.set_text("jpg")
        sleep(3)

    def click_ON_Three_Dot(self):
        sleep(2)
        three_dot = self.poco(self.Three_Dot_Icon_Next_To_PDF)
        three_dot.click()
        sleep(2)

    def click_On_Share_Option(self):
        sleep(2)
        Share_Option = self.poco(self.Share_Option)
        Share_Option.click()
        sleep(2)

    def click_Suggestion_PDF_File(self):
        Suggestion_PDF_File = self.poco(self.Suggestion_PDF_File)
        Suggestion_PDF_File.click()
        sleep(3)

    def click_PDF_ON_Result(self):
        PDF_ON_Result = self.poco(self.PDF_ON_Result)
        PDF_ON_Result.click()
        sleep(3)

    def click_PDF_Share_Option(self):
        PDF_Share_Option = self.poco(text="Share")
        PDF_Share_Option.click()
        sleep(3)

    def click_Print_Option(self):
        Print_Option = self.poco(text="Print")
        Print_Option.click()
        sleep(3)

    def Verify_Notification_Is_Not_Displaying(self):
        sleep(2)
        if not self.Notification_Is_Not_Displaying:
            return "Notification Is not Displaying"
        return "Notification Is  Displaying"

    def Verify_Notification_To_Login(self):
        # assert_exists(self.Notification_To_Login, "Notification To Login is displaying")
        Notification_To_Login = self.poco(self.Notification_To_Login)
        Notification_To_Login.get_text()
        print(" Please Login pop up is displaying:", Notification_To_Login)
        return Notification_To_Login

    def click_Available_Printer_To_Print(self):
        Available_Printer = self.poco(text="ZSB-DP12")
        if Available_Printer.exists():
            Available_Printer.click()
            sleep(3)
        else:
            print(" Printer is not displaying:")

    def click_Downloads(self):
        Downloads = self.poco(self.Downloads_Tab)
        Downloads.click()
        sleep(3)

    def click_Mobile_SearchBar(self):
        Mobile_SearchBar = self.poco(self.Mobile_SearchBar)
        Mobile_SearchBar.click()
        sleep(3)

    def click_On_Searchbar2(self):
        sleep(2)
        SearchBar2 = self.poco(self.Searchbar2)
        SearchBar2.click()
        sleep(3)

    def Enter_Files_Text_On_SearchBar(self):
        SearchBar2 = self.poco(self.Searchbar2)
        SearchBar2.set_text(" ")
        sleep(2)
        SearchBar2.set_text("Files")
        sleep(2)
        self.poco(self.Files_Folder).click()
        sleep(3)

    def click_Drive_Searchbar(self):
        sleep(3)
        SearchBar = self.poco(self.Drive_SearchBar)
        if SearchBar.exists():
            SearchBar.click()
            sleep(3)
        else:
            self.poco(self.Drive_SearchBar2).click()

    def click_Drive_Searchbar2(self):
        sleep(2)
        SearchBar2 = self.poco(self.Drive_SearchBar2)
        if SearchBar2.exists():
            SearchBar2.click()
        else:
            print("Searchbar is not there")

    def Enter_Download_Text_On_SearchBar(self):
        sleep(2)
        SearchBar2 = self.poco(self.Drive_SearchBar2)
        SearchBar2.set_text("Download")
        sleep(3)

    def Verify_Print_job_sent_successfully_Message(self):
        pass

    def Clear_The_Error_Status_On_The_Printer(self):
        pass

    def click_Settings_Tab(self):
        SearchBar2 = self.poco(self.Searchbar2)
        SearchBar2.set_text("Settings")
        sleep(3)

    def click_Settings(self):
        sleep(2)
        Settings = self.poco(self.Settings)
        if Settings.exists():
            Settings.click()
            sleep(2)
        else:
            print("Settings text is not there")

    # def click_Connected_Devices(self):
    #     sleep(2)
    #     Connected_Devices = \
    #         self.poco("android.widget.FrameLayout").offspring("com.android.settings:id/recycler_view").child(
    #             "android.widget.LinearLayout")[1].offspring("android:id/title")
    #     if Connected_Devices.exists():
    #         Connected_Devices.click()
    #         sleep(3)
    #     else:
    #         print("Connected Devices element not found")

    def click_Connected_Devices(self):
        sleep(2)
        Connected_Devices = self.poco(text="Connected devices")
        if Connected_Devices.exists():
            Connected_Devices.click()
            sleep(3)
        else:
            print("Connected Devices element not found")

    def click_Connection_Preferences(self):
        sleep(2)
        Connection_Preferences = \
            self.poco("android.widget.FrameLayout").offspring("com.android.settings:id/content_frame").offspring(
                "com.android.settings:id/recycler_view").child("android.widget.LinearLayout")[7].offspring(
                "android:id/title")
        if Connection_Preferences.exists():
            Connection_Preferences.click()
            sleep(3)
        else:
            print("Connection Preferences element not found")

    def click_Printing_Tab(self):
        printing_tab = \
            self.poco("android.widget.FrameLayout").offspring("com.android.settings:id/content_frame").offspring(
                "com.android.settings:id/recycler_view").child("android.widget.LinearLayout")[3].offspring(
                "android:id/title")
        if printing_tab.exists():
            printing_tab.click()
            sleep(3)
        else:
            print("Printing Tab element not found")

    def click_ZSB_Series(self):
        sleep(2)
        ZSB_Series = \
            self.poco("android.widget.FrameLayout").offspring("com.android.settings:id/content_frame").offspring(
                "com.android.settings:id/recycler_view").child("android.widget.LinearLayout")[1].offspring(
                "android:id/title")
        if ZSB_Series.exists():
            ZSB_Series.click()
            sleep(3)
        else:
            print("ZSB_Series element not found")

    def get_all_designs_in_recently_printed_labels(self, index=6):
        try:
            self.check_element_exists_name_or_text_matches("Recently")
            arr = self.get_all_designs_in_my_designs()
            temp = []
            for i in arr:
                if "prints left" not in i:
                    temp.append(i)
            return temp

        except:
            return []

    def click_Turn_ON_ZSB_Series_Printer(self):
        sleep(2)
        ZSB_Series = self.poco(self.Turn_ON_ZSB_Series_Printer)
        ZSB_Series.click()

    def click_Mobile_back_icon(self):
        sleep(2)
        Mobile_back_icon = self.poco(self.Mobile_back_icon)
        if Mobile_back_icon.exists():
            Mobile_back_icon.click()
            sleep(1)
        else:
            print("Back icon is not there")
            sleep(3)

    def click_Mobile_Footer_Back_Icon(self):
        sleep(2)
        mobile_footer_back_icon = self.poco(self.Mobile_Footer_Back_Icon)
        mobile_footer_back_icon.click()
        sleep(1)
        mobile_footer_back_icon.click()
        sleep(1)
        mobile_footer_back_icon.click()
        sleep(1)
        mobile_footer_back_icon.click()
        sleep(2)

    def Enter_Settings_Text_On_SearchBar(self):
        sleep(2)
        SearchBar2 = self.poco(self.Searchbar2)
        SearchBar2.set_text(" ")
        sleep(2)
        SearchBar2.set_text("Settings")
        sleep(3)
        self.poco(self.Settings).click()

    def Stop_Android_App(self):
        sleep(4)
        keyevent("HOME")
        sleep(4)

    def Verify_Print_Review_Page(self):
        print_preview = self.poco(self.Print_Review_Page)
        if print_preview.exists():
            print_preview.get_text()
            print(" Print Review page is displaying correctly:", print_preview)
            return print_preview
        else:
            print(" Print Review page is not displaying correctly")

    def click_Save_AS_PDF(self):
        sleep(5)
        save_as_pdf = self.poco(self.Save_AS_PDF)
        save_as_pdf.click()
        sleep(2)

    def click_All_Printers(self):
        sleep(1)
        All_Printers = self.poco(text="All printers…")
        if All_Printers.exists():
            All_Printers.click()
            sleep(8)
        else:
            print("All_Printers element not found")

    def click_PrinterAll(self):
        save_as_pdf = self.poco(self.All_Printers)
        save_as_pdf.click()
        sleep(2)

    def Verify_Printer_Status_AS_Offline(self):
        Printer_Status_AS_Offline = self.poco(textMatches=".*ZSB Series - Offline*")
        if Printer_Status_AS_Offline:
            return "Printer status Is Displaying as Offline"
        return "Printer status Is not Displaying as Offline"