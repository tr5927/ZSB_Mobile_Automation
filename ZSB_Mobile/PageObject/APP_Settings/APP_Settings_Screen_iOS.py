from airtest.core.assertions import assert_exists
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException


class App_Settings_Screen_iOS:
    pass

    def __init__(self, poco):
        self.poco = poco

        self.Printer_Settings_Btn = "Printer Settings"
        self.PrinterName_In_Printer_Settings = (Template(r"tpl1705401014619.png", record_pos=(0.165, -0.724), resolution=(1170, 2532)))
        # self.WiFi_Tab = (Template(r"tpl1705401064196.png", record_pos=(0.232, -0.579), resolution=(1170, 2532)))
        self.WiFi_Tab = "Wi-Fi"
        self.Current_Network_Txt = "Current Networks"
        self.Network_Name_Txt = "NESTWIFI"
        self.Network_Status_Txt = "Network Status"
        self.Network_Status_Result_Txt = "Connected"
        self.IPAddress_Txt = "IP Address"
        self.IPAddress_Result_Txt = "192.168.86.175"
        self.Manage_Network = "Manage Networks"
        self.Save_Network_Message_Txt = "You can save up to 5 network profiles to your Saved Networks. If no saved networks are available, you will have to add a new one."
        self.Threedot_On_Workspace = (Template(r"tpl1705401141406.png", record_pos=(0.254, -0.686), resolution=(1170, 2532)))
        self.Test_Print_Btn = "Test Print"
        self.Bluetooth_Connection_Required_Msg = " You are about to connect to the printer using Bluetooth. If you have not connected to the printer from this device before, please set the printer into pairing mode by holding the power button for 3 seconds. If you have connected to this printer from another mobile device in the past, please remove this bond in the devices bluetooth settings or power off the device."
        self.Continue_Btn_on_Bluetooth_Connection_Failed_popup = "Continue"
        self.Cancel_Btn_n_Bluetooth_Connection_Failed_Popup = "Cancel"
        self.Red_Icon_to_remove_network = " "
        self.Add_Network = "Add Network"
        self.Add_Network_Txt = "Add Network"
        self.Deleted_Network = "Zebra"
        self.Edit_Txt = "Edit"
        self.Change_Theme = "Change Theme"
        self.Save_Exit_Btn = "Save & Exit"
        self.Home_text_on_homepage = "Home"
        self.Pen_Icon = "Button"
        self.Units_Of_Measurements_Text = (Template(r"tpl1705419067128.png", record_pos=(-0.231, 0.074), resolution=(1170, 2532)))
        self.Inches_Option = (Template(r"tpl1705419132252.png", record_pos=(-0.235, 0.199), resolution=(1170, 2532)))
        self.Expand_Icon = (Template(r"tpl1705419196892.png", record_pos=(0.384, 0.191), resolution=(1170, 2532)))
        self.Milimetres_Text = "Millimetres"
        self.Centimetres_Text = "Centimetres"
        self.Inches_Text = "Inches"
        self.Updated_Msg = "Units of Measurement updated successfully"
        self.Home_Text = "Home"
        self.Size_In_Cm = (Template(r"tpl1705419282061.png", record_pos=(0.071, -0.321), resolution=(1170, 2532)))
        self.My_Design = "My Designs"
        self.Mydesign_Size_In_Cm = (Template(r"tpl1705419343855.png", record_pos=(0.193, -0.037), resolution=(1170, 2532)))
        self.Upload_Photo = "Upload photo"
        self.Edit_Workspace = "Edit Workspace"
        self.Profile_Avatar_Letter = (Template(r"tpl1705419524147.png", record_pos=(-0.353, -0.6), resolution=(1170, 2532)))

        self.Show_roots_Hamburger_Icn = "Show roots"
        self.Recent_Images = "android:id/title"
        self.Camera_Option = "androidx.cardview.widget.CardView"
        self.First_Picture = "android.view.View"
        self.Remove_Image = "Remove image"
        self.Back_Icon = "com.android.systemui:id/back"

        self.Workspace_Name_Text_Field = "TextField"
        self.Edit_Workspace_Back_Icon = "Button"
        self.Workspace_Name_Text = "Workspace name"
        self.Keyboard_back_Icon = "Done"
        self.Previous_Workspace_Name = (Template(r"tpl1705419993824.png", record_pos=(0.011, -0.14), resolution=(1170, 2532)))
        self.Workspace_Name_Update_update_message = ""
        self.Updated_Workspace_Name = (Template(r"tpl1705420425792.png", record_pos=(0.003, -0.135), resolution=(1170, 2532)))

        self.Profile_Name = "My First Workspace"

        self.First_Name_Text = (Template(r"tpl1705420538483.png", record_pos=(-0.327, -0.074), resolution=(1170, 2532)))
        self.Last_Name_Text = (Template(r"tpl1705420583545.png", record_pos=(-0.321, 0.191), resolution=(1170, 2532)))
        self.First_Name = (Template(r"tpl1705420663756.png", record_pos=(0.009, 0.019), resolution=(1170, 2532)))
        self.Last_Name = (Template(r"tpl1705420683027.png", record_pos=(0.004, 0.289), resolution=(1170, 2532)))
        self.Recently_Printed_Labels_Text = "Recently Printed Labels"
        self.Firstone_In_Recently_Printed_Labels = "Other"
        self.Printer_is_present = (Template(r"tpl1705420889960.png", record_pos=(-0.33, -0.439), resolution=(1170, 2532)))
        self.Name_Updated_Message = "Your changes have been saved"
        self.Buy_More_Labels = "Buy More Labels"



    def click_Printer_Settings(self):
        printer_settings = self.poco(self.Printer_Settings_Btn)
        printer_settings.click()

    def Enter_Google_Password(self):
        enter_google_password = self.poco(self.Google_Password)
        sleep(2)
        enter_google_password.set_text("Swdvt@#123")

    def click_PrinterName_On_Printersettings(self):
        # printerName = self.poco(self.PrinterName_In_Printer_Settings)
        touch(self.PrinterName_In_Printer_Settings)

    def click_wifi_tab(self):

        touch(self.WiFi_Tab)

    def test_CurrentNetwork_Txt_is_present_on_printer_settings_page(self):

        if self.poco(name="Current Network").exists():
            print("Current Network Text is not present.")
            assert True

        else:
            print("Current Network Text is not present.")
            assert False

    def test_Network_Status_Txt_is_present_on_printer_settings_page(self):

        if self.poco(name="Network Status").exists():
            print("Network Status Text is not present.")
            assert True
        else:
            print("Network Status Text is not present.")
            assert False

    # def get_text_Network_Status_Txt(self):
    #     if self.Network_Status_Txt.exists():
    #         network_status_txt = self.poco(self.Network_Status_Txt)
    #         text = network_status_txt.get_text()
    #         print("Network Status is present.")
    #         assert True
    #         return text
    #     else:
    #         print("Network Status is not present.")
    #         assert False

    # def get_text_Network_Status_Txt(self):
    #     if self.poco(name="Network Status").exists():
    #      print("Network Status is present.")
    #      assert True
    # else:
    #       print("Network Status is not present.")
    #       assert False

    def get_text_Network_Status_Result_Txt(self):
        network_status_result_txt = self.poco(self.Network_Status_Result_Txt)
        network_status_result_txt.get_text()
        return network_status_result_txt

    def get_text_IPAddress_Txt(self):
        IPaddress_txt = self.poco(self.IPAddress_Txt)
        IPaddress_txt.get_text()
        return IPaddress_txt

    def get_text_IPAddress_Result_Txt(self):
        IPaddress_result_txt = self.poco(self.IPAddress_Result_Txt)
        IPaddress_result_txt.get_text()
        return IPaddress_result_txt

    def click_Manage_Networks_Btn(self):
        manage_network = self.poco(self.Manage_Network)
        manage_network.click()

    def IS_Present_Save_Network_Message_Txt(self):
        save_network_message = self.poco(self.Save_Network_Message_Txt)
        save_network_message.get_text()
        return save_network_message

    def Test_Print_button_is_present_on_printer_settings_page(self):
        if self.poco(name="Test Print").exists():
            print("Test Print button is present.")
            assert True
        else:
            print("Test Print button is not present.")
            assert False

    def get_text_Bluetooth_connection_required_Txt(self):
        save_network_message = self.poco(self.Bluetooth_Connection_Required_Msg)
        save_network_message.get_text()
        return save_network_message

    def accept_Continue_popup(self):
        # Look for the "OK" or "Allow" button in the popup
        Continue_button = self.poco(name="Continue")

        if Continue_button.exists():
            # Click on the "OK" or "Allow" button
            Continue_button.click()
            print("Popup accepted.")
            return True
        else:
            print("Popup not found or already accepted.")
            return False

    def click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup(self):
        Continue_button = self.poco(name="Continue")

        if Continue_button.exists():
            # Click on the "OK" or "Allow" button
            Continue_button.click()
            print("Popup accepted.")
            return True
        else:
            print("Popup not found or already accepted.")
            return False

    def Cancel_is_present_on_Bluetooth_Connection_Failed_Popup(self):
        cancel_btn = self.poco(self.Cancel_Btn_n_Bluetooth_Connection_Failed_Popup)
        cancel_btn.get_text()
        print("Text of Cancel button:", cancel_btn)

        return cancel_btn

    #
    # def get_text_of_cancel_button(self):
    #     # Set a timeout value (in seconds) for waiting for the element to be visible
    #     timeout_seconds = 10
    #
    #     try:
    #         # Wait until the element is visible
    #         cancel_btn = self.poco(self.Cancel_Btn_n_Bluetooth_Connection_Failed_Popup).wait_for_visible(timeout=timeout_seconds)
    #
    #         # Get the text of the cancel button
    #         cancel_btn_text = cancel_btn.get_text()
    #
    #         # Print the text (optional)
    #         print("Text of Cancel button:", cancel_btn_text)
    #
    #         # Return the text
    #         return cancel_btn_text
    #
    #     except PocoTargetTimeout:
    #         # Handle the timeout exception (e.g., print an error message)
    #         print("Timeout waiting for Cancel button to be visible")
    #         return None  # You may want to return a specific value or raise an exception here

    def test_get_text_of_cancel_button(self):
        # Set a timeout value (in seconds) for waiting for the element to be visible
        timeout_seconds = 80

        # Wait until the element is visible
        wait(self.poco(self.Cancel_Btn_n_Bluetooth_Connection_Failed_Popup), timeout=timeout_seconds)

        # Get the text of the cancel button
        cancel_btn_text = self.poco(self.Cancel_Btn_n_Bluetooth_Connection_Failed_Popup).get_text()

        # Print the text (optional)
        print("Text of Cancel button:", cancel_btn_text)

        # Return the text
        return cancel_btn_text

    def click_Red_Icon_to_remove_network(self):
        touch(self.Red_Icon_to_remove_network)

    def click_Add_Network(self):
        add_network = self.poco(self.Add_Network)

        if add_network.exists():
            # Click on the "OK" or "Allow" button
            add_network.click()
            print("Able to click on the add network.")
            return True
        else:
            print("Unable to click on the add network.")
            return False

    def get_text_Add_Network(self):
        add_network_txt = self.poco(self.Add_Network_Txt)
        add_network_txt.get_text()
        print("Text of Cancel button:", add_network_txt)

        return add_network_txt

    def click_deleted_network(self):
        deleted_network = self.poco(self.Deleted_Network)
        deleted_network.click()

    def click_Three_Dot_On_Workspace(self):
        touch(self.Threedot_On_Workspace)

    def get_text_Edit_Txt(self):
        edit_txt = self.poco(self.Edit_Txt)
        edit_txt.get_text()
        print("Text of Edit Text:", edit_txt)
        return edit_txt

    def click_Edit_Txt(self):
        edit_txt = self.poco(self.Edit_Txt)
        edit_txt.click()

    def click_Change_Theme(self):
        change_theme = self.poco(self.Change_Theme)
        change_theme.click()

    def get_text_Change_Theme_Header(self):
        change_theme_header = self.poco(self.Change_Theme)
        change_theme_header.get_text()
        print("Change Theme Text:", change_theme_header)
        return change_theme_header

    # def check_Change_Modern_Theme(self):
    #     modern_theme = self.poco("name=android.widget.RadioButton[1]")
    #     modern_theme.click()

    def check_Change_Electic_Theme(self):
        # Assuming modern_theme is a UIObjectProxy
        # electic_theme = self.poco(name="android.widget.RadioButton[1]")
        electic_theme = self.poco(name="Eclectic")

        try:
            # Get the actual string selector from the UIObjectProxy
            electic_theme_selector = electic_theme.get_name()

            # Wait for the RadioButton to be visible
            self.poco(electic_theme_selector).wait_for_appearance(timeout=10)

            # Click on the RadioButton
            self.poco(electic_theme_selector).click()

            # Optional: Add a print statement to indicate success
            print("Clicked on the Electic theme RadioButton.")

        except PocoNoSuchNodeException:
            # Handle the case when the element is not found
            print("Electic theme RadioButton not found. Test continues...")

    # Call the method
    # check_Change_Modern_Theme(your_instance_of_the_class)

    def click_Save_Exit_Btn(self):
        save_exit = self.poco(self.Save_Exit_Btn)
        save_exit.click()

    def Home_text_is_present_on_homepage(self):
        home_text = self.poco(self.Home_text_on_homepage)
        home_text.get_text()
        print("Home Text is present on home page:", home_text)
        return home_text

    def check_radio_button_enabled(self):
        # Replace the following with the actual coordinates or image of the radio button
        # radio_button_position = (100, 200)

        # Check if the radio button exists on the screen
        if exists(Template(r"tpl1704961019063.png", record_pos=(-0.414, -0.149), resolution=(1080, 2400))):

            # Get the current state of the radio button (enabled or not)
            radio_button_enabled = (
                Template(r"tpl1704961019063.png", record_pos=(-0.414, -0.149), resolution=(1080, 2400)))

            # Check the state and perform actions accordingly
            if radio_button_enabled:
                print("Radio button is enabled.")
            else:
                print("Radio button is not enabled.")
        else:
            print("Radio button not found on the screen.")

    def check_Change_Bohemian_Theme(self):

        # Bohemian_theme = self.poco(name="android.widget.RadioButton[2]")
        Bohemian_theme = self.poco(name="Bohemian")

        try:
            # Get the actual string selector from the UIObjectProxy
            Bohemian_theme_selector = Bohemian_theme.get_name()

            # Wait for the RadioButton to be visible
            self.poco(Bohemian_theme_selector).wait_for_appearance(timeout=10)

            # Click on the RadioButton
            self.poco(Bohemian_theme_selector).click()

            # Optional: Add a print statement to indicate success
            print("Clicked on the Bohemian theme RadioButton.")

        except PocoNoSuchNodeException:
            # Handle the case when the element is not found
            print("Bohemian theme RadioButton not found. Test continues...")

    def check_Change_Professional_Theme(self):
        Professional_theme = self.poco(name="Professional")

        try:
            # Get the actual string selector from the UIObjectProxy
            Professional_theme_selector = Professional_theme.get_name()

            # Wait for the RadioButton to be visible
            self.poco(Professional_theme_selector).wait_for_appearance(timeout=10)

            # Click on the RadioButton
            self.poco(Professional_theme_selector).click()

            # Optional: Add a print statement to indicate success
            print("Clicked on the Professional  theme RadioButton.")

        except PocoNoSuchNodeException:
            # Handle the case when the element is not found
            print("Professional theme RadioButton not found. Test continues...")

    def check_Change_Maker_Theme(self):
        Maker_theme = self.poco(name="Maker")

        try:
            # Get the actual string selector from the UIObjectProxy
            Maker_theme_selector = Maker_theme.get_name()

            # Wait for the RadioButton to be visible
            self.poco(Maker_theme_selector).wait_for_appearance(timeout=10)

            # Click on the RadioButton
            self.poco(Maker_theme_selector).click()

            # Optional: Add a print statement to indicate success
            print("Clicked on the  Maker  theme RadioButton.")

        except PocoNoSuchNodeException:
            # Handle the case when the element is not found
            print("Maker theme RadioButton not found. Test continues...")

    def check_Change_Modern_Theme(self):
        Modern_theme = self.poco(name="Modern")

        try:
            # Get the actual string selector from the UIObjectProxy
            Modern_theme_selector = Modern_theme.get_name()

            # Wait for the RadioButton to be visible
            self.poco(Modern_theme_selector).wait_for_appearance(timeout=10)

            # Click on the RadioButton
            self.poco(Modern_theme_selector).click()

            # Optional: Add a print statement to indicate success
            print("Clicked on the  Modern  theme RadioButton.")

        except PocoNoSuchNodeException:
            # Handle the case when the element is not found
            print("Modern theme RadioButton not found. Test continues...")

    def click_pen_Icon_near_UserName(self):
        pen_icon = self.poco(self.Pen_Icon)
        pen_icon.click()

    def check_If_Units_of_Measurements_Is_Present(self):
        assert_exists(self.Units_Of_Measurements_Text, "Units_Of_Measurements_Text is present")

    def Inches_is_displaying(self):
        assert_exists(self.Inches_Option, "Inches Option is displaying by-default")

    def click_Units_of_Measurements(self):
        touch(self.Expand_Icon)

    def verify_Milimetres_Is_Present(self):
        milimetres_text = self.poco(self.Milimetres_Text)
        milimetres_text.get_text()
        print(" Milimetres is present:", milimetres_text)
        return milimetres_text

    def verify_Centimetres_Is_Present(self):
        centimetres_text = self.poco(self.Centimetres_Text)
        centimetres_text.get_text()
        print(" Centimetres Text is present:", centimetres_text)
        return centimetres_text

    def verify_Inches_Is_Present(self):
        inches_text = self.poco(self.Inches_Text)
        inches_text.get_text()
        print(" Inches Text is present:", inches_text)
        return inches_text

    def click_Centimeters(self):
        centimetres_Text = self.poco(self.Centimetres_Text)
        centimetres_Text.click()

    def verify_updated_msg(self):
        updated_msg = self.poco(self.Updated_Msg)
        updated_msg.get_text()
        print(" Units of Measurement updated successfully:", updated_msg)
        return updated_msg

    def click_Home_Tab(self):
        home_Text = self.poco(self.Home_Text)
        home_Text.click()

    def verify_printer_details_in_Centimeters(self):
        assert_exists(self.Size_In_Cm, "Printer details are displaying in cm")

    def click_My_Design(self):
        my_design = self.poco(self.My_Design)
        my_design.click()

    def verify_My_Details_Design_in_Centimeters(self):
        assert_exists(self.Mydesign_Size_In_Cm, "My Design details are displaying in cm")

    def click_Inches(self):
        inches_Text = self.poco(self.Inches_Text)
        inches_Text.click()

    def click_upload_photo(self):
        upload_photo = self.poco(self.Upload_Photo)
        upload_photo.click()

    def get_text_Edit_Workspace(self):
        edit_workspace = self.poco(self.Edit_Workspace)
        edit_workspace.get_text()
        print(" Edit Workspace text is displaying:", edit_workspace)
        return edit_workspace

    def click_Show_roots_Hamburger_Icn(self):
        show_roots_Hamburger_Icn = self.poco(self.Show_roots_Hamburger_Icn)
        show_roots_Hamburger_Icn.click()

    def click_Recent_Images(self):
        images = self.poco(self.Recent_Images)
        images.click()

    def click_Camera_Option(self):
        camera_option = self.poco(self.Camera_Option)
        camera_option.click()

    def click_First_Image(self):
        first_pic = self.poco(self.First_Picture)
        first_pic.click()

    def click_Remove_Image(self):
        remove_image = self.poco(self.Remove_Image)
        remove_image.click()

    def Is_Present_Profile_Avatar_Letter(self):
        assert_exists(self.Profile_Avatar_Letter, "Profile Avatar is displaying as initial letters")

    def click_Back_Icon(self):
        back_icon = self.poco(self.Back_Icon)
        back_icon.click()

    def Is_Present_Workspace_Name_Text(self):
        workspaceName_Text = self.poco(self.Workspace_Name_Text)
        workspaceName_Text.get_text()
        print(" Workspace name text is displaying:", workspaceName_Text)
        return workspaceName_Text

    def click_Workspace_Name_Text_Field(self):
        workspace_name = self.poco(self.Workspace_Name_Text_Field)
        workspace_name.click()

    def Clear_Workspace_Name(self):
        workspace_name = self.poco(self.Workspace_Name_Text_Field)
        workspace_name.set_text("")

    def click_Keyboard_back_Icon(self):
        keyboard_back_icon = self.poco(self.Keyboard_back_Icon)
        keyboard_back_icon.click()

    def Verify_SaveExit_Option_Is_Not_There(self):
        assert_not_exists(self.Save_Exit_Btn, "Save & Exit button is present")
        sleep(2)

    def click_back_Icon_On_Edit_Workspace(self):
        edit_workspace_back_icon = self.poco(self.Edit_Workspace_Back_Icon)
        edit_workspace_back_icon.click()

    def Is_Present_Workspace_Name(self):
        assert_exists(self.Previous_Workspace_Name, "Previous Workspace name is displaying")

    def Update_Workspace_Name_With_Space(self):
        workspace_name = self.poco(self.Workspace_Name_Text_Field)
        workspace_name.set_text("  ")

    def Update_Workspace_Name_With_Special_Characters_with_30_characters(self):
        workspace_name = self.poco(self.Workspace_Name_Text_Field)
        workspace_name.set_text("@abcdefghijklmn!@#abcdefghijklmn")

    def Verify_Updated_Name(self):
        assert_exists(self.Updated_Workspace_Name, "Updated Workspace name is displaying")

    def Update_Workspace_Name_with_Original_Name(self):
        workspace_name = self.poco(self.Workspace_Name_Text_Field)
        workspace_name.set_text("My First Workspace")

    def Profile_Name_Is_Displaying(self):
        profilename = self.poco(self.Profile_Name)
        profilename.get_text()
        print(" Profile name text is displaying:", profilename)
        return profilename

    def Is_Present_First_Name_Text(self):
        assert_exists(self.First_Name_Text, "First name text is displaying")

    def Is_Present_Last_Name_Text(self):
        assert_exists(self.Last_Name_Text, "Last name text is displaying")

    def verify_First_Name(self):
        firstname = self.poco(self.First_Name)
        firstname.get_text()
        print(" First name text is displaying:", firstname)
        return firstname

    def verify_Last_Name(self):
        lastname = self.poco(self.Last_Name)
        lastname.get_text()
        print(" Last name text is displaying:", lastname)
        return lastname

    def click_First_Name_Text_Field(self):
        touch(self.First_Name)

    def clear_First_Name(self):
        touch(self.First_Name).set_text("")

    def Is_Present_Recently_Printed_Labels_Text(self):
        recently_printed_labels = self.poco(self.Recently_Printed_Labels_Text)
        recently_printed_labels.get_text()
        print(" Recently printed Labels text is displaying:", recently_printed_labels)
        return recently_printed_labels

    def Is_Present_Firstone_In_Recently_Printed_Label(self):
        firstone_in_printed_labels = self.poco(self.Firstone_In_Recently_Printed_Labels)
        firstone_in_printed_labels.get_text()
        print(" Recently printed Labels text is displaying:", firstone_in_printed_labels)
        return firstone_in_printed_labels

    def Verify_Printer_is_already_added(self):
        assert_exists(self.Printer_is_present, "Printer is already added")

    def click_Firstone_In_Recently_Prtinted_Label(self):
        firstone = self.poco(self.Firstone_In_Recently_Printed_Labels)
        firstone.click()

    def Update_First_Name_With_Special_Characters_with_30_characters(self):
        first_name = self.poco(self.First_Name)
        first_name.set_text("@abcdefghijklmn!@#abcdefghijklmn")

    def click_Last_Name_Text_Field(self):
        lastname = self.poco(self.Last_Name)
        lastname.click()

    def clear_Last_Name(self):
        last_name = self.poco(self.Last_Name)
        last_name.set_text("")

    def Update_Last_Name_With_Special_Characters_with_30_characters(self):
        last_name = self.poco(self.Last_Name)
        last_name.set_text("@abcdefghijklmn!@#abcdefghijklml")

    def verify_Your_changes_have_been_saved_Message(self):
        name_updated_message = self.poco(self.Name_Updated_Message)
        name_updated_message.get_text()
        print(" Name updated text is displaying:", name_updated_message)
        return name_updated_message

    def Update_Default_First_Name(self):
        first_name = self.poco(self.First_Name)
        first_name.set_text("SohoApp")

    def Update_Default_Last_Name(self):
        last_name = self.poco(self.Last_Name)
        last_name.set_text("Testing")

    def Is_Present_Buy_More_Labels(self):
        buy_more_labels = self.poco(self.Buy_More_Labels)
        buy_more_labels.get_text()
        print(" Recently printed Labels text is displaying:", buy_more_labels)
        return buy_more_labels
