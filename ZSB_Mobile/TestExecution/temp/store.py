login_page = Login_Screen(poco)
others = Others(poco)
#
# login_page.click_Menu_HamburgerICN()
#
# others.click_Printer_Settings()
# others.swipe_left()
# others.click_selected_printer()
#
# others.click_test_print()

def test_Others_TestcaseID_47972():
    pass

login_page.click_Menu_HamburgerICN()

sleep(1)

""" Select the Printer Settings """
others.click_Printer_Settings()

others.swipe_left()
""" Select a printer """
others.click_selected_printer()
sleep(2)

""" Click on the icon """
others.click_icon()
sleep(1)

"""Click On the Demo video"""
others.click_demo_video()
sleep(5)

"""Close The Demo Video"""
others.close_demo_video()


def test_Others_TestcaseID_49203():
    pass

"""Click On the Three dots of the Home page Printer"""
others.click_three_dots()

"""Click on the Delete Button"""
others.click_delete_button()

"""Verify the text image (Currently The text cannot be extracted so verifying using the name)"""
others.verify_delete_printer_text()

"""Check cancel and delete button exists"""
others.check_cancel_and_delete_button()

"""cancel the delete printer dialogue"""
others.click_cancel_delete_printer()


def test_Others_TestcaseID_47946():
    pass

"""take the prvious number of cartridges"""
previous = others.get_no_of_left_cartridge()
print(previous)

"""click on navigation option"""
login_page.click_Menu_HamburgerICN()

"""Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
others.click_Printer_Settings()
others.click_selected_printer()
sleep(2)
n=2

"""test the printer to print the label"""
for i in range(n):
    others.click_test_print()
    sleep(2)

sleep(1)
"""Go to the Home Page"""
login_page.click_Menu_HamburgerICN()
others.click_home_button()
sleep(2)

"""After printing Get the number of cartridges"""
after = others.get_no_of_left_cartridge()
print(after)

"""Check wheather the cartridges are updated"""
res = others.check_auto_update_cartridge(previous,after,n)
if res:
    print("success")
else:
    print("Failed")

























