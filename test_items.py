import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_for_adding_item_to_cart(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("button[type='submit']")
    assert button, 'Unable to locate the button'