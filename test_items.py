from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_for_adding_item_to_cart(browser):
    browser.get(link)
    css_selector = "button[type='submit']"
    def check_exists_by_css(css_selector):
        try:
            browser.find_element_by_css_selector(css_selector)
        except NoSuchElementException:
            return False
        return True

    assert check_exists_by_css(css_selector) == True, 'Unable to locate the button'