import datetime
import time
import random
import string
import fnmatch

from airtest.core.api import *
# import pytest
# from pipes import Template
from poco import poco
from poco.exceptions import PocoNoSuchNodeException

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
import subprocess

common_method = Common_Method(poco)
data_sources_page = Data_Sources_Screen(poco)


class Template_Management_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Search_place_holder = Template(r"search_design_placeholder.png", record_pos=(-0.192, -0.609),
                                            resolution=(1080, 2280))
        self.Search_icon = Template(r"search_Icon.png", record_pos=(-0.398, -0.605), resolution=(1080, 2280))
        self.Search_files_place_holder = Template(r"search_files_place_holder.png", record_pos=(-0.203, -0.584), resolution=(1080, 2340))


    def turn_on_wifi(self):
        cmd = "adb shell svc wifi enable"
        common_method.run_the_command(cmd)

    def get_showing_n_designs_number(self):
        self.poco(nameMatches=".*Showing.*").wait_for_appearance(timeout=10)
        a = self.poco(nameMatches=".*Showing.*").get_name()
        a = a.split(" ")
        return a[1]

    def turn_off_wifi(self):
        command = "adb shell svc wifi disable"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("Command output:")
        print(result.stdout)

    def verify_default_sort_my_designs(self):
        return self.poco("Name (A to Z)").exists()

    def click_sort_my_designs(self):
        self.poco("android.view.View")[4].child()[4].click()

    def verify_sort_options_my_designs(self):
        if len(self.poco("android.view.View")[6].child()) == 2:
            if self.poco("android.view.View")[6].child()[0].get_name() == "Name (A to Z)":
                if self.poco("android.view.View")[6].child()[1].get_name() == "Name (Z to A)":
                    pass
                else:
                    raise Exception("\"Name (Z to A)\" is not present.")
            else:
                raise Exception("\"Name (A to Z)\" is not present.")
        else:
            raise Exception(f"There are {len(self.poco("android.view.View")[6].child())} options present.")

    def verify_default_filter_my_designs(self):
        return self.poco("All sizes").exists()

    def verify_sort_order_my_designs(self, sort_order):
        if sort_order == "A-Z":
            return self.poco("Name (A to Z)").exists()
        elif sort_order == "Z-A":
            return self.poco("Name (Z to A)").exists()

    def click_filter_my_designs(self, name=None):
        if name is not None:
            if name == "All sizes":
                self.poco("All sizes").click()
        else:
            self.poco("android.view.View")[4].child()[3].click()

    def selectFilter(self, filterOptionNumber):
        selected_option = self.poco("android.view.View")[6].child()[filterOptionNumber].get_name()
        self.poco("android.view.View")[6].child()[filterOptionNumber].click()
        return selected_option

    def click_sort_common_designs(self):
        self.poco("android.widget.EditText").parent().child()[3].click()

    def click_filter_common_designs(self):
        self.poco("android.view.View")[5].child()[2].click()

    def get_filter_value(self):
        return self.poco("android.view.View")[5].child()[2].get_name()

    def verify_connection_error_app(self):
        return self.poco("An error occurred when loading your designs. Please tap to try again").exists()

    def wait_for_appearance_designs_in_a_particular_category(self):
        self.poco("android.view.View").child(type="android.widget.ImageView").wait_for_appearance(timeout=10)

    def get_all_designs_in_my_designs(self, name=False):
        first_design = self.poco("android.view.View").child(type="android.widget.ImageView").get_name()
        total = []
        prev = []
        while 1:
            if name:
                curr = [child.get_name().split("\n")[0] for child in
                        self.poco("android.view.View").child(type="android.widget.ImageView")]
            else:
                curr = [child.get_name() for child in
                        self.poco("android.view.View").child(type="android.widget.ImageView")]
            if curr != prev:
                for i in curr:
                    if i not in total:
                        total.append(i)
            if curr == prev:
                break
            self.poco.swipe([0.5, 0.9], [0.5, 0.5])
            prev = curr
        while not self.poco(first_design).exists():
            self.poco.swipe([0.5, 0.5], [0.5, 0.9])
        return total

    def get_all_designs_size_in_my_designs(self):
        first_design = self.poco("android.view.View").child(type="android.widget.ImageView").get_name()
        total = []
        prev = []
        label_sizes = set()
        while 1:
            curr = [child.get_name() for child in self.poco("android.view.View").child(type="android.widget.ImageView")]
            if curr != prev:
                for i in curr:
                    if i not in total:
                        total.append(i)

            if curr == prev:
                break

            self.poco.swipe([0.5, 0.9], [0.5, 0.5])
            prev = curr
        for i in total:
            label_sizes.add(i.split("\n")[1])
        while not self.poco(first_design).exists():
            self.poco.swipe([0.5, 0.5], [0.5, 0.9])
        return label_sizes

    def filter_options(self, length=False):

        filter_option_list = []
        if length:
            return len(self.poco("android.view.View")[6].child())
        else:
            for i in range(1, len(self.poco("android.view.View")[6].child())):
                filter_option_list.append(self.poco("android.view.View")[6].child()[i].get_name())
            return filter_option_list

    def verify_design_names_follow_order(self, design_names, sort_order="A-Z"):
        start_with_special_character = False
        start_with_number = False
        start_with_alphabet = False
        previous_design_name = None
        previous_design_num = None
        if sort_order == "A-Z":
            for name in design_names:
                if name[0].isalpha():
                    if not start_with_number and not start_with_special_character:
                        raise Exception(
                            "Design name starting with alphabets found before design names starting with number and special characters... ")
                    start_with_alphabet = True
                    if previous_design_name is not None and name <= previous_design_name:
                        raise Exception(f"Design {name} not following sort order:{sort_order}.")
                    previous_design_name = name
                elif name[0].isdigit():
                    if start_with_alphabet:
                        raise Exception(
                            "Design name starting with number found after design names starting with alphabets... ")
                    start_with_number = True
                    if previous_design_num is not None and name <= previous_design_num:
                        raise Exception(f"Design {name} not following order 0-9 for designs starting with numbers..")
                    previous_design_num = name
                else:
                    if start_with_number or start_with_alphabet:
                        raise Exception(
                            "Design name starting with special characters found after design names starting with number or alphabets...")
                    start_with_special_character = True
        elif sort_order == "Z-A":
            for name in design_names:
                if name[0].isalpha():
                    if start_with_number or start_with_special_character:
                        raise Exception(
                            "Design name starting with alphabets found after design names starting with number or special characters... ")
                    start_with_alphabet = True
                    if previous_design_name is not None and name >= previous_design_name:
                        raise Exception(f"Design {name} not following sort order:{sort_order}.")
                    previous_design_name = name
                elif name[0].isdigit():
                    if start_with_special_character:
                        raise Exception(
                            "Design name starting with number found after design names starting with special characters... ")
                    start_with_number = True
                    if previous_design_num is not None and name >= previous_design_num:
                        raise Exception(f"Design {name} not following order 9-0 for designs starting with numbers..")
                else:
                    if not start_with_number and not start_with_alphabet:
                        raise Exception(
                            "Design name starting with special characters found before design names starting with number and alphabets...")
                    start_with_special_character = True

    def check_design_count_title(self, length):
        return self.poco(f"Showing {length} Designs").exists()

    def clickCommonDesigns(self):
        self.poco("Common Designs").click()

    def checkIfAccPresent(self, account):
        start = 0
        end = 1
        while True:
            for i in range(start, len(self.poco("android.widget.ListView").child()) - end):
                if self.poco("android.widget.ListView").child()[i].child().child()[0].get_text() == "Use another account":
                    return False
                elif self.poco("android.widget.ListView").child()[i].child().child()[1].get_text() == account:
                    return True
            start = 1
            end = 0
            self.poco.scroll()

    def search_design_common_designs(self, design_name):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(design_name)

    def select_design_common_designs(self):
        self.poco("android.view.View")[7].child()[1].child().click()

    def select_design_common_designs_Web(self):
        if self.poco("android.widget.Image")[1].exists():
            self.poco("android.widget.Image")[1].click()

    def select_label_common_designs_Web(self):
        if self.poco("android.widget.Image")[2].exists():
            self.poco("android.widget.Image")[2].click()

    def select_label_common_designs(self):
        self.poco("android.view.View").child(type="android.widget.ImageView").wait_for_appearance(timeout=10)
        label_name = self.poco("android.view.View").child(type="android.widget.ImageView").get_name().split("\n")[0]
        self.poco("android.view.View").child(type="android.widget.ImageView").click()
        return label_name

    def get_name_of_selected_design(self):
        design_name = self.poco(textMatches="Edit").parent().parent().parent().parent().child()[0].child()[1].get_text()
        return design_name

    def click_copy_to_My_Designs(self):
        try:
            self.poco("Copy to My Designs").click()
        except:
            self.poco(text="Copy to My Designs").click()

    def get_first_design_name_my_designs(self):
        return self.poco("android.view.View")[8].child().child().get_name().split("\n")[0]

    def check_for_suggestion_drop_down_in_search_designs(self):
        a = self.poco(nameMatches="(?s).*result.*")[0].exists()
        return a

    def checkNumberOfDesignsMatchingDropDown(self):
        drop_down_results = len(self.poco("android.view.View")[3].child())
        for i in range(drop_down_results):
            print(self.poco("android.view.View")[3].child()[i].get_name().split("\n")[1])
            if fnmatch.fnmatch(self.poco("android.view.View")[3].child()[i].get_name().split("\n")[1], "? result"):
                pass
            else:
                raise Exception("Number of design that matches the list in the suggestion dropdown is not displayed on the right side of each.")

    def check_dropdown_options_Are_clickable(self):
        drop_down_result_1 = self.poco("android.view.View")[3].child().get_name()
        return self.poco(name=drop_down_result_1, enabled=True).exists()

    def click_drop_down_result_1(self, returnName=None):
        if self.poco(nameMatches="(?s).*DESIGNS.*").exists():
            return_value = self.poco(nameMatches="(?s).*DESIGNS.*").get_name().split("\n")[1]
            self.poco(nameMatches="(?s).*DESIGNS.*").click()
        elif self.poco(nameMatches="(?s).*result.*").exists():
            return_value = self.poco(nameMatches="(?s).*result.*").get_name().split("\n")[0]
            self.poco(nameMatches="(?s).*result.*").click()
        elif self.poco(nameMatches="(?s).*CATEGORIES.*").exists():
            return_value = self.poco(nameMatches="(?s).*CATEGORIES.*").get_name().split("\n")[1]
            self.poco(nameMatches="(?s).*CATEGORIES.*").click()
        if returnName is not None:
            return return_value

    def select_sort_order(self, sort_order):
        if sort_order == "A-Z":
            self.poco("Name (A to Z)").click()
        elif sort_order == "Z-A":
            self.poco("Name (Z to A)").click()

    def verify_designs_are_according_to_sort_order(self, design_list):
        if self.poco("android.view.View")[6].child()[0].get_name() == "Name (A to Z)":
            for i in range(len(design_list) - 1):
                if design_list[i] > design_list[i + 1]:
                    return False
            return True
        elif self.poco("android.view.View")[6].child()[0].get_name() == "Name (Z to A)":
            for i in range(1, len(design_list)):
                if design_list[i - 1] < design_list[i]:
                    return False
            return True

    def select_label_size(self):
        size = self.poco("android.view.View")[6].child()[1].get_name()
        self.poco("android.view.View")[6].child()[1].click()
        return size

    def verify_search_placeholder(self):
        return assert_exists(self.Search_place_holder, "Search design place holder present.")

    def verify_search_drop_down_results(self, search_text):
        for i in range(len(self.poco("android.view.View")[3].child())):
            result = self.poco("android.view.View")[3].child()[i].get_name().split("\n")[0]
            if search_text.lower() in result.lower():
                pass
            else:
                raise Exception("search text not present in one of the dropdown result.")

    def wait_for_suggestions_to_appear(self):
        self.poco(nameMatches="(?s).*result.*").wait_for_appearance(timeout=10)

    def click_Connect_Data_File(self):
        self.poco(text="Connect Data File").wait_for_appearance(timeout=10)
        self.poco(text="Connect Data File").focus([0.1, 0.5]).click()

    def select_file_from_Connect_Data_File(self, name=None):
        if name is not None:
            self.poco(textMatches="columnWithUnequalRows.xlsx.*").click()
        else:
            self.poco("android.widget.TextView")[3].click()
            return self.poco("android.widget.TextView")[3].get_text().split(" ")[0]

    def click_from_data_file(self):
        self.poco(text="   From Data File").focus([0.0, 0.5]).click()

    def clickAddText(self):
        self.poco(text="Add text").click()

    def placeText(self):
        touch(Template(r"tpl1708429167702.png", record_pos=(-0.109, 0.382), resolution=(1080, 2340)))

    def checkManualInput_checkbox(self):
        if self.poco("android.widget.CheckBox", checked=True):
            pass
        else:
            self.poco("android.widget.CheckBox").click()

    def verify_print_preview(self, preview_name):
        assert_exists(Template(rf"{preview_name}.png", record_pos=(-0.001, -0.045), resolution=(1080, 2340)),
                      "Preview is present.")

    def verify_label_range_navigation_unavailable(self):
        return self.poco("Label 1 of 1").exists()

    def fillOrganizationId(self, Id):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(Id)

    def fillIndex(self, index):
        self.poco("android.widget.EditText")[1].click()
        self.poco("android.widget.EditText")[1].set_text(index)

    def verify_if_on_relink_data_source_page(self):
        return self.poco(nameMatches=".*Relink.*").exists()

    def verify_if_on_update_connections_page(self):
        return self.poco(nameMatches="Update Data Connections").exists()

    def verify_duplicate_previous_next_button(self):
        if self.poco("Previous")[1].exists():
            return True
        if self.poco("Next")[1].exists():
            return True
        return False

    def select_second_colum_from_data_file(self):
        self.poco("android.widget.TextView")[7].focus([0.1, 0.5]).click()
        self.poco("android.widget.TextView")[9].focus([0.1, 0.5]).click()

    def selectChooseAnOption(self, option_count=1, option_name=None, click=True):
        try:
            self.poco(nameMatches="(?s).*Choose an option.*").wait_for_appearance(timeout=20)
        except:
            sleep(3)
        for i in range(1, option_count + 1):
            try:
                self.poco(nameMatches="(?s).*Choose an option.*").click()
            except:
                self.poco(nameMatches="(?s).*Continue.*").parent().child()[2].click()
            if click:
                if option_name is None:
                    self.poco("android.view.View")[6].child()[option_count - i].click()
                else:
                    self.poco(option_name).click()

    def verify_label_range_is_All(self):
        if self.poco("All").exists():
            return
        raise Exception("Label Range is not 'All'")

    def verify_label_navigation(self):
        initial = self.poco(nameMatches="Label.*").get_name()
        self.poco("Next").click()
        navigated_next = self.poco(nameMatches="Label.*").get_name()
        self.poco("Previous").click()
        navigated_previous = self.poco(nameMatches="Label.*").get_name()
        if navigated_next != initial:
            if navigated_previous == initial:
                return
        raise Exception("'Previous' and 'Next' navigation buttons are not functioning.")

    def check_total_label_for_print_count(self, n):
        return self.poco(f"Total of {n} labels").exists()

    def get_total_labels_printing(self):
        return self.poco(nameMatches=".*Total.*").get_name().split(" ")[2]

    def choose_label_print_range(self):
        self.poco("android.widget.ScrollView").child()[6].click()

    def rename_Design(self):
        self.poco("Rename").click()

    def new_design_name(self, name):
        self.poco("android.widget.EditText").focus([0.5, 0.45]).click()
        self.poco("android.widget.EditText").set_text(name)

    def clickDuplicateDesign(self):
        self.poco("Duplicate").click()

    def clickDeleteDesign(self):
        self.poco("Delete").click()

    def verifyLabelsShown(self):
        try:
            self.poco("android.view.View").child(type="android.widget.ImageView").wait_for_appearance(timeout=20)
        except:
            raise Exception("Error in displaying round labels.")

    def change_print_value(self, value):
        self.poco("android.widget.EditText").set_value(value)

    def click_print_value(self):
        self.poco("android.widget.EditText").click()

    def get_print_value(self):
        return self.poco("android.widget.EditText").get_text()

    def compare_element_text(self, element, expected_text):
        element_text = element.get_text()
        print(f"Text from the element: {element_text}")
        if element_text == expected_text:
            print("Text matches the expected value.")
            assert False

    def verifySearchCommonDesignPlaceHolder(self):
        return assert_exists(self.Search_place_holder, "Search placeholder is present")

    def verifySearchIcon(self):
        return assert_exists(self.Search_icon, "Search icon is present")

    def checkIfElementIsPresent(self, element):
        try:
            a = self.poco(element).exists()
            return a
        except:
            a = self.poco(text=element).exists()
            return a

    def verifySearchFiles(self):
        return assert_exists(self.Search_files_place_holder, "Search placeholder is present")

    def clickSearchIconTextBox(self):
        touch(Template(r"search_icon.png", record_pos=(-0.218, -0.723), resolution=(1080, 2280)))

    def clickSearchIcon(self):
        touch(self.Search_icon)

    def clickFirstIcon(self):
        self.poco("android.view.View").child(type="android.widget.ImageView").click()

    def get_drop_down_list_common_designs(self, category=False):
        prev = []
        temp = []
        flag = 1
        while flag:
            curr = [child.get_name() for child in self.poco("android.widget.FrameLayout")[4].child().child().child()[0].child().child().child()]
            if curr == prev:
                break
            for i in curr:
                if i not in temp:
                    if "CATEGORIES" in i or "DESIGNS" in i:
                        i = i.split("\n")[1]
                    if category:
                        if "DESIGNS" in i:
                            flag = 0
                            break
                    temp.append(i)
            prev = curr
            self.poco.swipe([0.5, 0.5], [0.5, 0.2])
        return temp

    def clickCancelSearch(self):
        self.poco("android.widget.Button")[-1].click()

    def get_all_categories_in_common_designs(self, name=False):
        temp = []
        prev = []
        while 1:
            if name:
                curr = [child.get_name().split('\n')[0] for child in
                        self.poco(nameMatches="(?s).*For use with Label Cartridges:.*")]
            else:
                curr = [child.get_name() for child in self.poco(nameMatches="(?s).*For use with Label Cartridges:.*")]
            for i in curr:
                if i not in temp:
                    temp.append(i)
            if prev == curr:
                break
            prev = curr
            self.poco.scroll()
        return temp

    def get_all_designs_in_search_designs(self, name=False):
        while not self.poco(nameMatches=".*Designs .*", enabled=True).exists():
            self.poco.scroll()

        temp = self.get_all_designs_in_my_designs(name)
        return temp

    def waitForAppearanceTypeName(self, elementType, elementName, time_out=20):
        self.poco(type=elementType, nameMatches="(?s).*"+elementName+".*").wait_for_appearance(timeout=time_out)

    def get_all_search_results_in_search_designs(self, name=False):
        a = len(self.poco(nameMatches="(?s).*result.*"))
        temp = []
        if a < 5:
            for i in range(a):
                if name:
                    temp.append(self.poco(nameMatches="(?s).*result.*")[i].get_name().split("\n")[0])
                else:
                    temp.append(self.poco(nameMatches="(?s).*result.*")[i].get_name())
        else:
            total = []
            prev = []
            while 1:
                if name:
                    curr = [child.get_name().split("\n")[0] for child in self.poco(nameMatches="(?s).*result.*")]
                else:
                    curr = [child.get_name() for child in self.poco(nameMatches="(?s).*result.*")]
                if curr != prev:
                    for i in curr:
                        if i not in total:
                            total.append(i)

                if curr == prev:
                    break

                self.poco.swipe([0.5, 0.5], [0.5, 0.2])
                prev = curr

            return total
        return temp

    def click_scrim(self):
        self.poco("Scrim").click()

    def verifySearchResults_n(self, n):
        return self.poco(f"Search results ({n})").exists()


    def check_suggestion_window_in_common_design(self):
        regex_pattern = "(?s).*CATEGORIES.*"
        a = self.poco(nameMatches=regex_pattern).exists()

        regex_pattern = "(?s).*DESIGNS.*"
        b = self.poco(nameMatches=regex_pattern).exists()

        regex_pattern = "(?s).*No results found..*"
        c = self.poco(nameMatches=regex_pattern).exists()

        regex_pattern = "(?s).*result.*"
        d = self.poco(nameMatches=regex_pattern).exists()

        return a or b or c or d

    def get_all_fields_print_page(self):
        elements = set()
        previous = set()
        while 1:
            current = set()
            for child in self.poco("android.widget.ScrollView").child("android.view.View").child():
                current.add(child.get_text())
            if current == previous:
                break
            elements = elements.union(current)
            previous = current.copy()
            self.poco.scroll()
        return elements

    def fill_all_print_fields(self, value=None):
        elements = []
        previous = []
        while 1:
            current = []
            for child in self.poco("android.widget.ScrollView").child("android.view.View").child():
                current.append(child.get_text())
            if current == previous:
                break
            for field in current:
                print(field)
                if field is not None and field not in elements:
                    print("selection "+field)
                    if value is None:
                        random_word = data_sources_page.generateRandomWord(8)
                    else:
                        random_word = value
                    print(random_word)
                    self.poco(text=field).click()
                    self.poco(text=field).set_text(random_word)
                    keyevent("back")
                    elements.append(random_word)
            previous = current

    def getLastPrintFromFirstDesignInRecentlyPrintedDesigns(self):
        return self.poco("android.view.View").child(type="android.widget.ImageView")[1].get_name().split("\n")[-1].split(":")[-1].strip()

    def get_remaining_label_count(self):
        labels_left = int(self.poco(nameMatches=".*Printer.*").get_name().split(" ")[1][1:])
        return labels_left

    def wait_for_appearance_enabled(self, element, time_out=20):
        self.poco(element, enabled=True).wait_for_appearance(timeout=time_out)

    def wait_for_appearance_disabled(self, element, time_out=20):
        self.poco(element, enabled=False).wait_for_appearance(timeout=time_out)

    def wait_for_appearance_disabled(self, element, time_out=20):
        self.poco(element, enabled=False).wait_for_appearance(timeout=time_out)

    def verify_design_manipulation_for_all_designs(self):
        total = []
        prev = []
        while 1:
            curr = [child.get_name() for child in self.poco("android.view.View").child(type="android.widget.ImageView")]
            for name in curr:
                if name not in total:
                    self.poco(name).click()
                    self.verify_design_manipulation_options()
                    self.click_scrim()
                    total.append(name)
            if curr == prev:
                break
            self.poco.scroll()
            prev = curr

    def verify_design_manipulation_options(self):
        if self.poco("Print").exists():
            pass
        else:
            raise Exception("Print option not present")
        if self.poco("Rename").exists():
            pass
        else:
            raise Exception("Rename option not present")
        if self.poco("Duplicate").exists():
            pass
        else:
            raise Exception("Duplicate option not present")
        if self.poco("Delete").exists():
            pass
        else:
            raise Exception("Delete option not present")

    def scroll_my_designs(self, direction="up"):
        total = []
        prev = []
        while 1:
            curr = [child.get_name() for child in self.poco("android.view.View").child(type="android.widget.ImageView")]
            for name in curr:
                if name not in total:
                    total.append(name)
            if curr == prev:
                break
            scroll_view = self.poco("android.view.View")
            scroll_view.swipe(direction)
            scroll_view.swipe(direction)
            prev = curr

    def changeCopiesCount(self, new_copies_count):
        self.poco("Copies").parent().child("android.widget.EditText").click()
        self.poco("Copies").parent().child("android.widget.EditText").set_text(new_copies_count)

    def get_the_name_size_and_lastprint_of_design(self, design):
        a = design.split("\n")
        try:
            return a[0], a[1], a[2].split(":")[1].strip()
        except:
            return a[0], a[1], 0

    def checkIfDataSourceIsLinked(self):
        if self.poco("Choose an option").exists():
            raise Exception("Data Source not linked.")
        else:
            pass

    def closeNotification(self):
        touch(Template(r"close_notification.png", record_pos=(0.415, -0.896), resolution=(1080, 2280)))

    def clickAccept(self):
        self.poco("Accept").click()

    def check_if_on_print_preview_page(self):
        return self.poco(nameMatches=".*Label.*").exists()

    def get_label_print_range(self):
        return self.poco("android.widget.ScrollView").child()[6].get_name()

    def get_first_row_first_column_value(self):
        return self.poco("android.widget.CheckBox")[3].parent().child()[1].get_name()

    def verify_only_selected_rows_displayed_in_label_range(self, number_of_selected_rows):
        print(self.poco("Print").parent().child()[-7].get_name())
        if self.poco("Print").parent().child()[-7].get_name() == "1-" + number_of_selected_rows:
            pass
        else:
            raise Exception("rows displayed on the label range field not matching with the selected number of rows")

    def verify_My_Designs_pagination(self):
        return self.poco("android.widget.ListView").exists()

    def verify_pagination_shown_is_correct(self):
        total_designs = int(self.poco(textMatches=".*Showing.*").get_text().split(" ")[3])
        number_of_pages = len(self.poco("android.widget.ListView").child()) - 2
        items_per_page = int(self.poco(textMatches=".*items.*").get_text().split(" ")[1])
        print(total_designs, number_of_pages, items_per_page)
        if items_per_page * number_of_pages >= total_designs > items_per_page * (number_of_pages - 1):
            pass
        else:
            raise Exception(
                "Number of pages not satisfying formula\n \"Items per page * Number of pages >= Total nuber of designs > Items per page * Number of pages -1\" ")

    def clickSave(self):
        try:
            self.poco("Save").click()
        except:
            self.poco(text="Save").click()

    def verifyErrorPopUp_forInvalidCopies(self):
        try:
            self.poco(nameMatches="(?s).*Error.*").wait_for_appearance(timeout=10)
            if self.poco(nameMatches="(?s).*Error.*").get_name().split("\n")[1] == "An Unknown Error has Occured.":
                pass
            else:
                error = f"Error shown as {self.poco(nameMatches="(?s).*Error.*").get_name().split("\n")[1]} instead of \"An Unknown Error has Occured.\"."
                raise Exception(error)

        except:
            raise Exception("No Error Pop Up.")

    def wait_for_element_appearance_type(self, element, time_out=15):
        self.poco(type=element).wait_for_appearance(timeout=time_out)

    def clickImport(self):
        self.poco(text="Import").wait_for_appearance(timeout=10)
        self.poco(text="Import").click()

    def get_all_icons_zebra_gallery(self):
        elements = set()
        previous = set()
        while 1:
            current = set()
            for child in self.poco("android.view.View").child(type="android.widget.ImageView"):
                current.add(child.get_name())
            if current == previous:
                break
            elements = elements.union(current)
            previous = current.copy()
            self.poco.scroll()
        scroll_view = self.poco("android.widget.ScrollView")
        while not self.poco(type="android.view.View", name="Alert").exists():
            scroll_view.swipe("down")
        return elements

    def search_Icons(self, icon_name):
        self.poco("android.widget.EditText").wait_for_appearance(timeout=15)
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(icon_name)

    def select_file_update_data_connections(self, filename):
        selected_file_name = self.poco(nameMatches=f"(?s).*{filename}.*").get_name().split("(")[0].strip()
        self.poco(nameMatches=f"(?s).*{filename}.*").click()
        return selected_file_name

    def verify_update_data_connections_dialog(self):
        try:
            self.poco(nameMatches="The below data sources are missing for the .* label. They must be updated in order to print.")
        except:
            raise Exception("\"The below data sources are missing for the label. They must be updated in order to print.\" dialog did not appear")

    def selectDesign(self, design_name):
        self.poco(name=design_name).click()

    def get_Labels_left_in_printer_info(self):
        printer_info = self.poco(nameMatches="(?s).*prints left.*").get_name()
        label_info = printer_info.split("\n")[4]
        return label_info

    def search_label_range(self):
        self.poco("android.widget.EditText").set_text("1.01")

    def getDesignInfo(self, design_name):
        return self.poco(nameMatches="(?s).*"+design_name+".*").get_name()






