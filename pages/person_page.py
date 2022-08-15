import time

from .base_page import BasePage
from .locators import PersonPageLocators


class PersonPage(BasePage):
    ACTIVE_TAB = 'active_tab'
    REMOVED_TAB = 'removed_tab'

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.__current_tab = PersonPage.ACTIVE_TAB

    def get_current_tab(self): return self.__current_tab

    def go_to_active_tab(self):
        self.browser.find_element(*PersonPageLocators.PEOPLE_ACTIVE_TAB).click()
        self.__current_tab = PersonPage.ACTIVE_TAB
        time.sleep(1)

    def go_to_removed_tab(self):
        self.browser.find_element(*PersonPageLocators.PEOPLE_REMOVED_TAB).click()
        self.__current_tab = PersonPage.REMOVED_TAB
        time.sleep(1)

    def go_to_detailed_info(self):
        self.browser.find_element(*PersonPageLocators.PERSON_INFO).click()

    def close_drawer(self):
        self.browser.find_element(*PersonPageLocators.DRAWER_CLOSE_BTN).click()
        time.sleep(1)

    '''def cancel(self,
               dec: str):
        if dec == 'cancel':
            self.browser.find_element(*WorkPageLocators.MSGBOX_CANCEL_BTN).click()
        elif dec == 'leave':
            self.browser.find_element(*WorkPageLocators.MSGBOX_LEAVE_BTN).click()
        else:
            raise AssertionError('Wrong decision (decisions avaliable: cancel, leave)')

    def delete_element(self,
                       dec: str):
        if dec == 'cancel':
            self.browser.find_element(*WorkPageLocators.MSGBOX2_CANCEL_BTN).click()
        elif dec == 'delete':
            self.browser.find_element(*WorkPageLocators.MSGBOX2_DELETE_BTN).click()
        else:
            raise AssertionError('Wrong decision (decisions available: cancel, delete)')'''