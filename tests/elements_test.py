from pages.elements_page import TextBoxPage
import time


class TestElements:
    class TestTextBox:


        def text_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            time.sleep(5)