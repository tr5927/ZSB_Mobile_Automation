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
wake()
start_app("com.zebra.soho_app")
sleep(2.0)
common_method = Common_Method()
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)


def test_DataSources_TestcaseID_45729():
    """""""""test"""""


#
#
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(2)
# """Select file with special characters"""
# special_char_file = data_sources_page.selectExistingFile()
# data_sources_page.searchName(special_char_file)
# data_sources_page.verify_File_Data()
# data_sources_page.searchName("")
# """Select long file name"""
# long_file = data_sources_page.selectExistingFile()
# data_sources_page.searchName(long_file)
# data_sources_page.verify_File_Data()
# data_sources_page.searchName("")
# """Remove both files"""
# data_sources_page.searchName(special_char_file)
# data_sources_page.remove_File()
# data_sources_page.searchName("")
# data_sources_page.searchName(long_file)
# data_sources_page.remove_File()
# data_sources_page.searchName("")
# """Check if files removed successfully"""
# data_sources_page.searchName(special_char_file)
# data_sources_page.checkIfListIsEmpty()
# data_sources_page.searchName(long_file)
# data_sources_page.checkIfListIsEmpty()
# """"""""""""""""""""""""""""""""""""""
# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# """Select file with special characters"""
# special_char_file = data_sources_page.selectExistingFile()
# data_sources_page.searchName(special_char_file)
# data_sources_page.verify_File_Data()
# data_sources_page.searchName("")
# """Select long file name"""
# long_file = data_sources_page.selectExistingFile()
# data_sources_page.searchName(long_file)
# data_sources_page.verify_File_Data()
# data_sources_page.searchName("")
# """Remove both files"""
# data_sources_page.searchName(special_char_file)
# data_sources_page.remove_File()
# data_sources_page.searchName("")
# data_sources_page.searchName(long_file)
# data_sources_page.remove_File()
# data_sources_page.searchName("")
# """Check if files removed successfully"""
# data_sources_page.searchName(special_char_file)
# data_sources_page.checkIfListIsEmpty()
# data_sources_page.searchName(long_file)
# data_sources_page.checkIfListIsEmpty()


def test_DataSources_TestcaseID_45730():
    """""""""test"""""


# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# initial_file_count = data_sources_page.fileListDisplayed()
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(2)
# """Click back arrow"""
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(2)
# data_sources_page.checkFilesShownAreSupported()
# data_sources_page.searchFilesInLinkFiles("png_file.png")
# png_file = data_sources_page.selectExistingFile()
# data_sources_page.clickSelect()
# data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(2)
# data_sources_page.checkFilesShownAreSupported()
# data_sources_page.searchFilesInLinkFiles("jpg_file.png")
# jpg_file = data_sources_page.selectExistingFile()
# data_sources_page.clickSelect()
# data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(2)
# data_sources_page.checkFilesShownAreSupported()
# data_sources_page.searchFilesInLinkFiles("csv_file.png")
# csv_file = data_sources_page.selectExistingFile()
# data_sources_page.clickSelect()
# data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)


def test_DataSources_TestcaseID_45731():
    """""""""test"""""


# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# initial_file_count = data_sources_page.fileListDisplayed()
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(2)
# """Click back arrow"""
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(2)
# data_sources_page.checkFilesShownAreSupported()
# data_sources_page.searchFilesInLinkFiles("png_file.png")
# png_file = data_sources_page.selectExistingFile()
# data_sources_page.clickSelect()
# data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(2)
# data_sources_page.checkFilesShownAreSupported()
# data_sources_page.searchFilesInLinkFiles("jpg_file.png")
# jpg_file = data_sources_page.selectExistingFile()
# data_sources_page.clickSelect()
# data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(2)
# data_sources_page.checkFilesShownAreSupported()
# data_sources_page.searchFilesInLinkFiles("csv_file.png")
# csv_file = data_sources_page.selectExistingFile()
# data_sources_page.clickSelect()
# data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)


def test_DataSources_TestcaseID_45732():
    """""""""test"""""


# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# initial_file_count = data_sources_page.fileListDisplayed()
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# """Click back arrow"""
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# data_sources_page.checkFilesShownAreSupported()
# data_sources_page.searchFilesInLinkFiles("png_file.png")
# png_file = data_sources_page.selectExistingFile()
# data_sources_page.clickSelect()
# data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# data_sources_page.checkFilesShownAreSupported()
# data_sources_page.searchFilesInLinkFiles("jpg_file.png")
# jpg_file = data_sources_page.selectExistingFile()
# data_sources_page.clickSelect()
# data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# data_sources_page.checkFilesShownAreSupported()
# data_sources_page.searchFilesInLinkFiles("csv_file.png")
# csv_file = data_sources_page.selectExistingFile()
# data_sources_page.clickSelect()
# data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)

def test_DataSources_TestcaseID_45744():
    """""""""test"""""


# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(5)
# """Click Upload file"""
# data_sources_page.click_Upload_File()
# sleep(5)
# """Select File to upload"""
# file_name = data_sources_page.select_File_To_Upload(True)
# sleep(5)
# """Upload the same file again"""
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(5)
# """Click Upload file"""
# data_sources_page.click_Upload_File()
# sleep(5)
# data_sources_page.select_File_To_Upload()
# sleep(5)
# if file_name[-4:] == "xlsx":
#     search_name = file_name[:-5]
#     data_sources_page.searchName(file_name[:-5])
# else:
#     search_name = file_name[:-4]
#     data_sources_page.searchName(file_name[:-4])
# file_list = data_sources_page.fileListDisplayed()
# try:
#     if (search_name in file_list) and (search_name + "(1)" in file_list):
#         pass
# except:
#     raise Exception("Re-uploading not appended '(1)' to file name")
#
# file_name_drive = data_sources_page.selectFile()
# """Unable to automate uploading local file with the same name as a cloud file"""


def test_DataSources_TestcaseID_45742():
    """""""""test"""""


#
#
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# data_sources_page.searchName("ferry.jpg")
# data_sources_page.remove_File_Based_On_DataSource("Google Drive", "ferry.jpg", True)
# file_list = data_sources_page.fileListDisplayed()
# if len(file_list) >= 1:
#     pass
# else:
#     raise Exception("File list empty")
# data_sources_page.remove_File_Based_On_DataSource("Google Drive", "ferry.jpg")
# data_sources_page.searchName("")
# sleep(3)
# data_sources_page.searchName("ferry.jpg")
# data_sources_page.verifyFilePresentInList("ferry.jpg", "Google Drive", True)


def test_DataSources_TestcaseID_45746():
    """""""""test"""""


#
#
#
# # """""""""click on the login button"""""""""""
# # login_page.click_loginBtn()
# # sleep(2)
# # """""""select the login with google option"""""""""
# # login_page.click_Loginwith_Google()
# # sleep(2)
# # login_page.click_GooglemailId()
# # sleep(5)
# # login_page.add_Account()
# # sleep(2)
# # login_page.Enter_Google_UserID()
# # sleep(2)
# # login_page.click_Emailid_Nextbtn()
# # sleep(4)
# # """"To enter password need to use the 2nd method """
# # login_page.Enter_Google_Password()
# # # poco(text("Swdvt@#123"))
# # # sleep(2)
# # login_page.click_Password_Nextbtn()
# # sleep(7)
# # help_page.chooseAcc()
# """Click hamburger icon to expand menu"""
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(5)
# """Click Upload file"""
# data_sources_page.click_Upload_File()
# sleep(5)
# """Select File to upload"""
# data_sources_page.select_File_To_Upload()
# sleep(5)
# """Verify Filename date and datasource"""
# common_method.swipe_screen([0.9, 0.3482905982905983], [0.22037037037037038, 0.3482905982905983], 3)
# data_sources_page.verify_File_Data()
#
#
# def test_DataSources_TestcaseID_47936():
#     """""""""test"""""
#
#
# """Click hamburger icon to expand menu"""
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(5)
# """Click Upload file"""
# data_sources_page.click_Upload_File()
# sleep(5)
# """Select File to upload"""
# data_sources_page.select_File_To_Upload()
# sleep(5)
# """Notification on file upload"""
# """Unable to verify due to BUG SMBM-712"""
# common_method.swipe_screen([0.9, 0.3482905982905983], [0.22037037037037038, 0.3482905982905983], 3)
# sleep(2)
# """Click Three Dots on My Data Page"""
# data_sources_page.clickThreeDotsMyData()
# sleep(2)
# """Click Remove"""
# data_sources_page.clickRemove()
# sleep(2)
# data_sources_page.clickRemove()
# """Verify if File is removed"""
# data_sources_page.verifyRemovedSuccessfully()
# """Notification on file removal"""
# """Unable to verify due to BUG SMBM-712"""
#
#
def test_DataSources_TestcaseID_45757():
    """""""""test"""""


#
#
# # """""""""click on the login button"""""""""""
# # login_page.click_loginBtn()
# # sleep(2)
# # """""""select the login with google option"""""""""
# # login_page.click_Loginwith_Google()
# # sleep(2)
# # login_page.click_GooglemailId()
# # sleep(5)
# # login_page.add_Account()
# # sleep(2)
# # login_page.Enter_Google_UserID()
# # sleep(2)
# # login_page.click_Emailid_Nextbtn()
# # sleep(4)
# # """"To enter password need to use the 2nd method """
# # login_page.Enter_Google_Password()
# # # poco(text("Swdvt@#123"))
# # # sleep(2)
# # login_page.click_Password_Nextbtn()
# # sleep(7)
# # help_page.chooseAcc()
# sleep(5)
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Designs in menu"""
# data_sources_page.clickMyDesigns()
# sleep(2)
# """Choose the design created at setup"""
# data_sources_page.selectDesignCreatedAtSetUp()
# sleep(5)
# """Click the print option"""
# data_sources_page.clickPrint()
# sleep(5)
# """Verify if there is option to choose picture"""
# data_sources_page.verifyPhotoOptions()
# poco.scroll()
# """Expand to see different options to choose picture"""
# data_sources_page.expandPhotoOptions()
# sleep(5)
# """Choose camera option"""
# data_sources_page.chooseCameraToClickPhoto()
# sleep(5)
# """click the photo"""
# data_sources_page.Camera_Shutter()
# """Part of step 4 is to check the preview is correct
#     unable to verify preview has to be done manually"""
# """Print the photo"""
# data_sources_page.clickPrint()


def test_DataSources_TestcaseID_45758():
    """""""""test"""""


# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.signInWithGoogle("zebratest850@gmail.com", "Zebra#123456789")
# sleep(2)
# data_sources_page.checkDriveEmpty()
# data_sources_page.clickBackArrow()

# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ One drive """
# # data_sources_page.signInWithMicrosoft("zebratest850@gmail.com", "Zebra#123456789")
# sleep(3)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# data_sources_page.checkDriveEmpty()
# data_sources_page.clickBackArrow()


def test_DataSources_TestcaseID_47942():
    """""""""test"""""


#
#
#
# """Click hamburger icon to expand menu"""
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(5)
# """Click Upload file"""
# data_sources_page.click_Upload_File()
# sleep(5)
# """Select File to upload"""
# data_sources_page.select_File_To_Upload()
# sleep(5)
#
# def test_DataSources_TestcaseID_47942():
#     """""""""test"""""
#
#
#
# """Click hamburger icon to expand menu"""
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(5)
# """Click Upload file"""
# data_sources_page.click_Upload_File()
# sleep(5)
# """Select File to upload"""
# data_sources_page.select_File_To_Upload()
# sleep(5)
# """Verify Progress Indicator"""
# data_sources_page.verifyProgressIndicator()
# sleep(10)
# """Verify if file uploaded succesfully"""
# common_method.swipe_screen([0.9, 0.3482905982905983], [0.22037037037037038, 0.3482905982905983], 3)
# data_sources_page.verify_File_Data()


def test_DataSources_TestcaseID_47830():
    """""""""test"""""


#
#
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Designs in menu"""
# data_sources_page.clickMyDesigns()
# sleep(2)
# start_app("com.microsoft.emmx")
# sleep(2)
# poco(text="Ask me anything…").click()
# sleep(2)
# poco(text="Ask me anything…").set_text("https://zsbportal.zebra.com/")
# sleep(2)
# data_sources_page.clickEnter()
# """adb shell input keyevent 26"""
# wake()
# # common_method.swipe_screen([0.5, 0.1576923076923077], [0.5, 0.3927350427350427], 1)
# # login_page.click_Loginwith_Google()
# # sleep(2)
# # login_page.click_GooglemailId()
# # sleep(5)
# # help_page.chooseAcc()
# # sleep(5)
# data_sources_page.click_Menu_HamburgerICNWeb()
# sleep(5)
# data_sources_page.clickMyDesigns()
# sleep(5)
# data_sources_page.click_Menu_HamburgerICNWeb()
# sleep(5)
# data_sources_page.clickCreateDesignBtn()
# sleep(5)
#
# sleep(2)
# # wake()
# common_method.swipe_screen([0.9, 0.25427350427350426], [0.08055555555555556, 0.25427350427350426], 1)
# sleep(5)
# data_sources_page.clickAddBarcode()
# sleep(5)
# data_sources_page.placeBarcode()
# sleep(5)
# common_method.swipe_screen([0.08055555555555556, 0.25427350427350426], [0.9, 0.25427350427350426], 1)
# sleep(5)
# label_name = "1A"
# data_sources_page.setLabelName(label_name)
# sleep(5)
# data_sources_page.exitDesigner()
# sleep(5)
# # common_method.swipe_screen([0.5, 0.1576923076923077], [0.5, 0.3927350427350427], 1)
# data_sources_page.click_Menu_HamburgerICNWeb()
# data_sources_page.click_My_Data()
# sleep(5)
# data_sources_page.click_Menu_HamburgerICNWeb()
# data_sources_page.click_Upload_File_Web()
# data_sources_page.selectFileToUploadWeb()
# start_app("com.zebra.soho_app")
# data_sources_page.searchName(label_name)
# data_sources_page.verifyDesign(label_name)
# data_sources_page.click_Menu_HamburgerICNWeb()
# data_sources_page.click_Upload_File_Web()
# data_sources_page.checkWebUploadedFileOnApp()


# def test_DataSources_TestcaseID_47830():
#     """test"""
#
# """Click hamburger icon to expand menu"""
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(5)
# """Click Upload file"""
# data_sources_page.click_Upload_File()
# sleep(5)
# """Select File to upload"""
# data_sources_page.select_File_To_Upload()
# sleep(5)


def test_DataSources_TestcaseID_45748():
    """test"""


# """Click hamburger icon to expand menu"""
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# """"""
# initial_file_count = data_sources_page.countNumberOfFiles()
# data_sources_page.searchExistingName()
# final_file_count = data_sources_page.countNumberOfFiles()
# data_sources_page.checkIfResultsAreFiltered(initial_file_count, final_file_count)
# data_sources_page.searchRandomWord()
# data_sources_page.enterSpecialCharactersInsearchField()
# data_sources_page.clearTextAndVerifyFileCount(initial_file_count)
# count_after_clearing_text = data_sources_page.countNumberOfFiles()


def test_DataSources_TestcaseID_45756():
    """test"""


#
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Designs in menu"""
# data_sources_page.clickMyDesigns()
# sleep(2)
# """Choose the design created at setup"""
# data_sources_page.selectDesignCreatedAtSetUp()
# sleep(2)
# """Click print"""
# data_sources_page.clickPrint()
# """Choose Use Local Contacts in Update Data Connections page"""
# data_sources_page.updateDataConnections()
# """Click 'Allow ZSB Series to access your contacts?'"""
# data_sources_page.clickAllow()
# """Click Continue"""
# data_sources_page.clickContinue()
# """Choose inputs in Relink Data Source Columns page"""
# data_sources_page.chooseAnOption2()
# data_sources_page.chooseAnOption1()
# data_sources_page.chooseAnOption3()
# """Verify if preview is present"""
# data_sources_page.verifyIfPreviewIsPresent()
# poco.scroll()
# """Set the label range accordingly"""
# data_sources_page.selectLabelRange(2)
# """Choose the printer to print the labels"""
# data_sources_page.selectPrinter()
# common_method.swipe_screen([0.5, 0.1987179487179487], [0.6268518518518519, 0.8478632478632478],1)
# """Verify if preview label range is according to the label range set"""
# data_sources_page.previewLabelRange()
# poco.scroll()
# """Click print to print the labels"""
# data_sources_page.clickPrint()

def test_DataSources_TestcaseID_45733():
    """test"""


#
# """Click hamburger icon to expand menu"""
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(5)
# """Click Upload file"""
# data_sources_page.click_Link_File()
# sleep(5)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
"""searchTest re check"""


# data_sources_page.searchTest("test")
# data_sources_page.searchTest("test_i", 1)
# data_sources_page.searchTest("test_i", 2)
# data_sources_page.searchTest("test_i", 3)
# data_sources_page.searchTest(".jpg")
# data_sources_page.searchTest(".png")
# data_sources_page.searchTest(".bmp")
# random_word = data_sources_page.generateRandomWord(24)
# data_sources_page.searchTest(random_word)


def test_DataSources_TestcaseID_45752():
    """Test"""


#
#
# """Click hamburger icon to expand menu"""
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# init_file_count = data_sources_page.fileListDisplayed()
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(5)
# """Click Upload file"""
# data_sources_page.click_Link_File()
# sleep(5)
# data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
# data_sources_page.clickMicrosoftOneDrive()
# data_sources_page.clickBackArrow()
# data_sources_page.checkNoChangeInFileCount(init_file_count)
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(5)
# """Click Upload file"""
# data_sources_page.click_Link_File()
# sleep(5)
# data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
# data_sources_page.clickMicrosoftOneDrive()

def test_DataSources_TestcaseID_47944():
    """test"""


"""Click hamburger icon to expand menu"""


# sleep(5)
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# data_sources_page.click_Add_File()
# sleep(2)
# # data_sources_page.click_Link_File()
# # sleep(2)
# # data_sources_page.clickGoogleDrive()
# # data_sources_page.chooseAccToLinkFile()
# data_sources_page.click_Upload_File()
# poco("android.widget.LinearLayout")[7].click()
# """Search not working in link files"""
# """For now manually select 4-BMP.BMP"""
# # data_sources_page.clickSelect()
# data_sources_page.searchName("4-BMP.BMP")
# poco("Connect files, so you can leverage them within your designs.").click()
# data_sources_page.checkIfListIsEmpty()

def test_DataSources_TestcaseID_45734():
    """test"""


# login_page.click_Menu_HamburgerICN()
# sleep(5)
"""Click My Data"""


# data_sources_page.click_My_Data()
# sleep(2)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Link_File()
# sleep(2)
# """Test for Google Drive"""
# data_sources_page.clickGoogleDrive()
# sleep(2)
# data_sources_page.checkFilesShownAreSupported()
# sleep(2)
# large_file = data_sources_page.selectLargeFile()
# sleep(2)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickGoogleDrive()
# """Upload a file"""
# existing_file =  data_sources_page.selectExistingFile()
# sleep(5)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickGoogleDrive()
# """Re upload the same file"""
# sleep(2)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Link_File()
# sleep(2)
# existing_file = data_sources_page.selectExistingFile()
# sleep(5)
# data_sources_page.checkIsAlreadyLinkedPopUp()
# """Test for One Drive"""
# sleep(2)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# # data_sources_page.checkFilesShownAreSupported()
# large_file = data_sources_page.selectLargeFile()
# sleep(7)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# """Upload a file"""
# existing_file = data_sources_page.selectExistingFile()
# sleep(5)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# """Re upload the same file"""
# existing_file =  data_sources_page.selectExistingFile()
# sleep(5)
# data_sources_page.checkIsAlreadyLinkedPopUp()

def test_DataSources_TestcaseID_45735():
    """test"""


"""Click hamburger icon to expand menu"""


# login_page.click_loginBtn()
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# # data_sources_page.countNumberOfFiles()
# sleep(2)
# data_sources_page.clickBackArrow()
# sleep(2)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# data_sources_page.checkFilesShownAreSupported()
# data_sources_page.selectExistingFile()

def test_DataSources_TestcaseID_45755():
    """""""""test"""""


"""Click hamburger icon to expand menu"""


# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
# sleep(5)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# data_sources_page.checkFilesShownAreSupported()
# sleep(10)
# existing_file = data_sources_page.selectExistingFile()
# sleep(5)
# data_sources_page.searchName(existing_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(existing_file, "OneDrive", True)

def test_DataSources_TestcaseID_45741():
    """""""""test"""""


#
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# data_sources_page.remove_File_Based_On_DataSource("OneDrive")
# sleep(2)


def test_DataSources_TestcaseID_45759():
    """""""""test"""""


# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# # data_sources_page.signInWithGoogle()
# data_sources_page.clickGoogleDrive()
# sleep(2)
# existing_file = data_sources_page.selectExistingFile()
# sleep(2)
# data_sources_page.searchName(existing_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(existing_file, "Google Drive", True)
# """Re upload same file"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """CLick Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickGoogleDrive()
# sleep(2)
# data_sources_page.selectExistingFile()
# sleep(2)
# """Verify if 'filename' is already linked pop up appears"""
# data_sources_page.checkIsAlreadyLinkedPopUp()
# """ One Drive """
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
# sleep(2)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# existing_file = data_sources_page.selectExistingFile()
# sleep(2)
# data_sources_page.searchName(existing_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(existing_file, "Google Drive", True)
# """Re upload same file"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """CLick Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# data_sources_page.selectExistingFile()
# sleep(2)
# """Verify if 'filename' is already linked pop up appears"""
# data_sources_page.checkIsAlreadyLinkedPopUp()

def test_DataSources_TestcaseID_45738():
    """""""""test"""""


# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.clickMyDesigns()
# sleep(2)
# data_sources_page.searchMyDesigns("LDA")
# sleep(3)
# data_sources_page.selectDesignCreatedAtSetUp()
# sleep(2)
# data_sources_page.clickPrint()
# sleep(2)
# data_sources_page.verifyPreviewShownIsCorrect()
# sleep(2)
# data_sources_page.clickBackArrow()
# sleep(2)
# poco("canada.xlsx").click()
# sleep(2)
# poco("android.view.View")[6].child()[5].click()
# sleep(2)
# data_sources_page.clickContinue()
# sleep(2)
# data_sources_page.chooseAnOption1()
# sleep(2)
# poco("android.view.View")[6].child().click()
# sleep(2)
# data_sources_page.clickContinue()
# sleep(2)
# poco.scroll()
# data_sources_page.labelRangeSelection(4)
# data_sources_page.clickPrint()

def test_DataSources_TestcaseID_45737():
    """""""""test"""""


#
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.click_My_Data()
# sleep(2)
# data_sources_page.searchName("canada.xlsx")
# sleep(2)
# data_sources_page.remove_File_Based_On_DataSource("Google Drive", "canada.xlsx", False, True)
# sleep(2)
# data_sources_page.searchName("")
# sleep(10)
# data_sources_page.searchName("canada.xlsx")
# sleep(2)
# common_method.swipe_screen([0.22037037037037038, 0.3482905982905983], [0.9, 0.3482905982905983], 3)
# try:
#     data_sources_page.verifyFilePresentInList("canada.xlsx", "Google Drive")
# except:
#     pass
# sleep(2)
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.clickMyDesigns()
# sleep(2)
# data_sources_page.searchMyDesigns("LDA")
# sleep(3)
# data_sources_page.selectDesignCreatedAtSetUp()
# sleep(2)
# data_sources_page.clickPrint()
# sleep(4)
# data_sources_page.clickBackArrow()
# sleep(2)
# poco("canada.xlsx").click()
# sleep(2)
# poco("android.view.View")[6].child()[5].click()
# sleep(2)
# data_sources_page.clickContinue()
# sleep(2)
# data_sources_page.chooseAnOption1()
# sleep(2)
# poco("android.view.View")[6].child().click()
# sleep(2)
# data_sources_page.clickContinue()
# sleep(2)
# poco.scroll()
# data_sources_page.labelRangeSelection(4)
# data_sources_page.clickPrint()

def test_DataSources_TestcaseID_45739():
    """""""""test"""""

sleep(3)
data_sources_page.searchFileInLocalStorage("large")
