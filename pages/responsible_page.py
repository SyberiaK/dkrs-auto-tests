import time
import datetime as dt
from selenium.webdriver.common.keys import Keys

from .person_page import PersonPage
from .locators import PersonPageLocators, ResponsiblePageLocators


class ResponsiblePage(PersonPage):
    def should_be_add_responsible_button(self):
        assert self.is_element_present(*ResponsiblePageLocators.ADD_RESPONSIBLE_BTN), \
            'Add responsible button is not presented'

    def go_to_add_responsible(self):
        self.browser.find_element(*ResponsiblePageLocators.ADD_RESPONSIBLE_BTN).click()

    def should_be_responsible_creation(self):
        for elem_name, elem_path in ResponsiblePageLocators.RESPONSIBLE_CREATION.items():
            assert self.is_element_present(*elem_path), f'{elem_name} is not presented'

    def should_not_be_responsible_creation(self, action: str):
        match action:
            case PersonPage.NOT_PRESENT:
                for elem_name, elem_path in ResponsiblePageLocators.RESPONSIBLE_CREATION.items():
                    assert self.is_not_element_present(*elem_path), f'{elem_name} is presented, but it shouldn\'t be'
            case PersonPage.DISAPPEAR:
                for elem_name, elem_path in ResponsiblePageLocators.RESPONSIBLE_CREATION.items():
                    assert self.is_disappeared(*elem_path), f'{elem_name} is presented, but it should disappear'

    def add_responsible(self,
                        fio: str,
                        email: str,
                        phone: str,
                        password: str,
                        objects: list = None):
        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_FIO_INPUT).send_keys(fio)
        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_PHONE_INPUT).send_keys(phone)
        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_PASSWORD_INPUT).send_keys(password)

        if objects:
            if len(objects) != 5:
                raise AttributeError('ADD_RESPONSIBLE: Wrong number of checks in objects list')
            if any(not isinstance(x, bool) for x in objects):
                raise AttributeError('ADD_RESPONSIBLE: All checks must be bool')
            objects_checkboxes = self.browser.find_elements(*ResponsiblePageLocators.RESPONSIBLE_OBJECTS_CHECKBOXES)
            for i, v in enumerate(objects_checkboxes):
                if objects[i]:
                    v.click()

        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_SAVE_BTN).click()
        time.sleep(1)

    def should_be_responsible_detailed_info(self):
        for elem_name, elem_path in ResponsiblePageLocators.RESPONSIBLE_DETAILED_INFO.items():
            assert self.is_element_present(*elem_path), f'{elem_name} is not presented'

    def should_not_be_responsible_detailed_info(self, action: str):
        match action:
            case PersonPage.NOT_PRESENT:
                for elem_name, elem_path in ResponsiblePageLocators.RESPONSIBLE_DETAILED_INFO.items():
                    assert self.is_not_element_present(*elem_path), f'{elem_name} is presented, but it shouldn\'t be'
            case PersonPage.DISAPPEAR:
                for elem_name, elem_path in ResponsiblePageLocators.RESPONSIBLE_DETAILED_INFO.items():
                    assert self.is_disappeared(*elem_path), f'{elem_name} is presented, but it should disappear'

    def go_to_archive(self):
        if self.get_current_tab() == ResponsiblePage.ACTIVE_TAB:
            self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_ADD_TO_ARCHIVE_BTN).click()
        else:
            raise Exception('Not an active tab so can\'t go to blacklist')

    def archive(self):
        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_AR_CONFIRM_BTN).click()

    def cancel_archive(self):
        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_AR_CANCEL_BTN).click()