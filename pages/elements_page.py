import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('sdswd')
        self.element_is_visible(self.locators.EMAIL).send_keys('asds@mail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('sdasd')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('asdsa')
        self.element_is_visible(self.locators.SUBMIT).click()
