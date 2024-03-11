import requests
import self
from airtest.core.api import *
from airtest.core.api import sleep
from urllib3.util import url

# from setuptools.config._validate_pyproject.formats import url

from ZSB_Mobile.Common_Method import Common_Method
from poco.exceptions import PocoNoSuchNodeException
from pocoui_lib.android.kotoComponent import poco


class APS_Notification:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Files_Folder = "Files"
        self.PDF_File_From_The_List = Template(os.path.join(os.path.expanduser('~'),
                              "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                              "tpl1709717652228.png"), record_pos=(-0.035, 0.831), resolution=(1080, 2400))

        # directory = os.path.join(os.path.expanduser('~'), "Pictures", "Automation_Backup", "ZSB_Automation", "ZSB_Mobile", "PageObject", "Images")
        #
        # # Define the filename of the image file
        # filename = "tpl1707817586300.png"
        #
        # # Join the directory and filename to create the full path
        # image_path = os.path.join(directory, filename)
        #
        # # Define the template with the full path
        # self.Apple_UserName = Template(image_path, record_pos=(-0.191, -0.867), resolution=(1170, 2532))

        self.Three_Dot_Icon_Next_To_PDF = "More options"
        self.PDF_Share_Option = "com.google.android.apps.docs:id/title"
        self.Print_Option = "Print"
        self.Notification_Is_Not_Displaying = (Template(r"tpl1709794655332.png", record_pos=(0.007, -0.85), resolution=(1080, 2400)))
        self.Notification_To_Login = self.poco(text="Please login to search for ZSB Printers")
        self.Available_Printer_To_Print = ""
        self.Downloads_Tab = "com.google.android.apps.nbu.files:id/search_suggestion_text"
        self.Mobile_SearchBar = "com.google.android.apps.nexuslauncher:id/hotseat"
        self.Drive_SearchBar = "com.google.android.apps.nbu.files:id/open_search_bar_text_view"
        self.Searchbar2 = "com.google.android.apps.nexuslauncher:id/input"
        self.Drive_SearchBar2 = "com.google.android.apps.nbu.files:id/search_box"

    #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def click_Device_Files_Folder(self):
        start_app("com.android.documentsui")
        wait(Template("files_app.png"), timeout=10)
        touch(Template("downloads_folder.png"))



    def click_Files_Folder(self):
        sleep(2)
        Files_Folder = self.poco(self.Files_Folder)
        Files_Folder.click()
        sleep(7)

    # def click_PDF_File_From_The_List(self):
    #     sleep(2)
    #     poco.scroll(self.PDF_File_From_The_List).exists()
    #     sleep(1)
    #     touch(self.PDF_File_From_The_List)
    #     sleep(3)

    # def click_PDF_File_From_The_List(self):
        # sleep(2)  # Add a sleep for 2 seconds before scrolling
        # if poco.scroll(self.PDF_File_From_The_List, direction='up').exists():  # Scroll vertically
        #     sleep(4)  # Adjusted sleep time if necessary
        #     touch(self.PDF_File_From_The_List)
        #     sleep(3)  # Add a sleep for 3 seconds after clicking the file
        # else:
        #     print("PDF file not found in the list")
    def click_PDF_File_From_The_List(self):
        sleep(3)  # Add a sleep for 10 seconds before scrolling (if needed)
        poco.scroll()
        max_swipes = 6
        for _ in range(max_swipes):

            if poco.scroll(self.PDF_File_From_The_List).exists():
                touch(self.PDF_File_From_The_List)
            else:
                poco.scroll()





    def click_Three_Dot_Icon_Next_To_PDF(self):
        Three_Dot_Icon = self.poco(self.Three_Dot_Icon_Next_To_PDF)
        Three_Dot_Icon.click()
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
        sleep(3)
        assert_not_exists(self.Notification_Is_Not_Displaying, "Notification Is Not Displaying")

    def Verify_Notification_To_Login(self):
        sleep(3)
        assert_exists(self.Notification_To_Login, "Notification To Login is displaying")

    def click_Available_Printer_To_Print(self):
        Available_Printer = self.poco(self.Available_Printer_To_Print)
        Available_Printer.click()
        sleep(3)

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
        SearchBar2.set_text("Files")
        sleep(3)

    def click_Drive_Searchbar(self):
        SearchBar = self.poco(self.Drive_SearchBar)
        SearchBar.click()
        sleep(3)

    def click_Drive_Searchbar2(self):
        sleep(2)
        SearchBar2 = self.poco(self.Drive_SearchBar2)
        SearchBar2.click()
        sleep(3)
        SearchBar2.set_text("Download")
        sleep(3)












