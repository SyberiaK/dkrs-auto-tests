from .base_page import BasePage
from .locators import AuthPageLocators


class AuthPage(BasePage):
    def should_be_auth_page(self):
        assert 'auth' in self.browser.current_url, 'This page is not a auth page'
        assert self.is_element_present(*AuthPageLocators.LOGIN_INPUT), 'Email input is not presented'
        assert self.is_element_present(*AuthPageLocators.PASSWORD_INPUT), 'Password input is not presented'

    def auth(self, login, password):
        self.browser.find_element(*AuthPageLocators.LOGIN_INPUT).send_keys(login)
        self.browser.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*AuthPageLocators.LOGIN_BTN).click()
