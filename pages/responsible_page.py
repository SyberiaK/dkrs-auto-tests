import time
import datetime as dt

from selenium.common import NoSuchElementException
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
                        services: list = None):
        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_FIO_INPUT).send_keys(fio)
        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_PHONE_INPUT).send_keys(phone)
        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_PASSWORD_INPUT).send_keys(password)

        if services:
            if len(services) != 5:
                raise AttributeError('ADD_RESPONSIBLE: Wrong number of checks in objects list')
            if any(not isinstance(x, bool) for x in services):
                raise AttributeError('ADD_RESPONSIBLE: All checks must be bool')
            objects_checkboxes = self.browser.find_elements(*ResponsiblePageLocators.RESPONSIBLE_OBJECTS_CHECKBOXES)
            for i, v in enumerate(objects_checkboxes):
                if services[i]:
                    v.click()

        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_SAVE_BTN).click()
        time.sleep(1)

    def check_responsible_info(self,
                               expected_fio: str,
                               expected_email: str,
                               expected_phone: str,
                               expected_object_n_services: list = None):
        services_available = ['Комплектация', 'О_АРМ', 'Погрузки и разгрузки', 'Разноса']

        expected_fio = expected_fio if expected_fio else '<EMPTY>'
        expected_email = expected_email if expected_email else '<EMPTY>'
        expected_phone = expected_phone if expected_phone else '<EMPTY>'
        if expected_object_n_services:
            if len(expected_object_n_services) != 5:
                raise AttributeError('CHECK_RESPONSIBLE: Wrong number of checks in objects list')
            if any(not isinstance(x, bool) for x in expected_object_n_services):
                raise AttributeError('CHECK_RESPONSIBLE: All checks must be bool')
            if all(not x for x in expected_object_n_services):
                expected_object_n_services = ['<EMPTY>']
        else:
            expected_object_n_services = ['<EMPTY>']

        actual_fio = self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_INFO_FIO).text
        actual_email = self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_INFO_EMAIL).text
        actual_phone = self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_INFO_PHONE).text

        try:
            object_name = self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_INFO_OBJECT).text
        except NoSuchElementException:
            object_name = ''

        try:
            services_list = self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_INFO_SERVICES)\
                .get_property('innerHTML').split(', ')
        except NoSuchElementException:
            services_list = []

        actual_object_n_services = [bool(object_name)] + \
                                   [service in services_list for service in services_available]

        actual_fio = actual_fio if actual_fio else '<EMPTY>'
        actual_email = actual_email if actual_email else '<EMPTY>'
        actual_phone = actual_phone if actual_phone else '<EMPTY>'
        if all(not x for x in actual_object_n_services):
            actual_object_n_services = ['<EMPTY>']

        assert actual_fio == expected_fio, f'Actual FIO: {actual_fio}, ' \
                                           f'expected: {expected_fio}'
        assert actual_email == expected_email, f'Actual email: {actual_email}, ' \
                                               f'expected: {expected_email}'
        assert actual_phone == expected_phone, f'Actual phone: {actual_phone}, ' \
                                               f'expected: {expected_phone}'
        assert actual_object_n_services == expected_object_n_services, f'Actual object and services: ' \
                                                                       f'{actual_object_n_services}, ' \
                                                                       f'expected: {expected_object_n_services}'

    def check_responsible_detailed_info(self,
                                        expected_fio: str,
                                        expected_email: str,
                                        expected_phone: str,
                                        expected_object_n_services: list = None):
        expected_fio = expected_fio if expected_fio else '<EMPTY>'
        expected_email = expected_email if expected_email else '<EMPTY>'
        expected_phone = expected_phone if expected_phone else '<EMPTY>'
        if expected_object_n_services:
            if len(expected_object_n_services) != 5:
                raise AttributeError('CHECK_RESPONSIBLE_DETAILED: Wrong number of checks in objects list')
            if any(not isinstance(x, bool) for x in expected_object_n_services):
                raise AttributeError('CHECK_RESPONSIBLE_DETAILED: All checks must be bool')
            if all(not x for x in expected_object_n_services):
                expected_object_n_services = ['<EMPTY>']
        else:
            expected_object_n_services = ['<EMPTY>']

        actual_fio = self.browser.find_element(*ResponsiblePageLocators
                                               .RESPONSIBLE_DETAILED_INFO_FIO_INPUT).get_property('value')
        actual_email = self.browser.find_element(*ResponsiblePageLocators
                                                 .RESPONSIBLE_DETAILED_INFO_EMAIL_INPUT).get_property('value')
        actual_phone = self.browser.find_element(*ResponsiblePageLocators
                                                 .RESPONSIBLE_DETAILED_INFO_PHONE_INPUT).get_property('value')
        object_n_services = self.browser.find_elements(*ResponsiblePageLocators
                                                       .RESPONSIBLE_DETAILED_INFO_OBJECTS_N_SERVICES_CHECKBOXES)
        actual_object_n_services = ['is-checked' in x.get_attribute("class") for x in object_n_services]

        actual_fio = actual_fio if actual_fio else '<EMPTY>'
        actual_email = actual_email if actual_email else '<EMPTY>'
        actual_phone = actual_phone if actual_phone else '<EMPTY>'
        if all(not x for x in actual_object_n_services):
            actual_object_n_services = ['<EMPTY>']

        assert actual_fio == expected_fio, f'Actual FIO: {actual_fio}, ' \
                                           f'expected: {expected_fio}'
        assert actual_email == expected_email, f'Actual email: {actual_email}, ' \
                                               f'expected: {expected_email}'
        assert actual_phone == expected_phone, f'Actual phone: {actual_phone}, ' \
                                               f'expected: {expected_phone}'
        assert actual_object_n_services == expected_object_n_services, f'Actual object and services: ' \
                                                                       f'{actual_object_n_services}, ' \
                                                                       f'expected: {expected_object_n_services}'

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

    def edit_responsible(self,
                         fio: str = None,
                         email: str = None,
                         phone: str = None,
                         object_n_services: list = None):
        if not (fio or email or phone or object_n_services):
            raise AssertionError('No edit')
        if fio:
            entry = self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_DETAILED_INFO_FIO_INPUT)
            entry.send_keys(Keys.CONTROL + "a")
            entry.send_keys(fio)
        if email:
            entry = self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_DETAILED_INFO_EMAIL_INPUT)
            entry.send_keys(Keys.CONTROL + "a")
            entry.send_keys(email)
        if phone:
            entry = self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_DETAILED_INFO_PHONE_INPUT)
            entry.send_keys(Keys.CONTROL + "a")
            entry.send_keys(phone)
        if object_n_services:
            if len(object_n_services) != 5:
                raise AttributeError('EDIT_RESPONSIBLE: Wrong number of checks in objects list')
            if any(not isinstance(x, bool) for x in object_n_services):
                raise AttributeError('EDIT_RESPONSIBLE: All checks must be bool')
            object_n_services_checkboxes = self.browser.find_elements(
                *ResponsiblePageLocators.RESPONSIBLE_DETAILED_INFO_OBJECTS_N_SERVICES_CHECKBOXES)
            checkboxes_checked = ['is-checked' in x.get_attribute("class") for x in object_n_services_checkboxes]
            for i, v in enumerate(object_n_services):
                if checkboxes_checked[i] != v:
                    object_n_services_checkboxes[i].click()

    def save_responsible(self):
        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_DETAILED_INFO_SAVE_BTN).click()
        time.sleep(1)

    def go_to_change_password(self):
        self.browser.find_element(*ResponsiblePageLocators.RESPONSIBLE_DETAILED_INFO_CHANGEPASS_BTN).click()

    def should_be_responsible_change_password(self):
        for elem_name, elem_path in ResponsiblePageLocators.RESPONSIBLE_CHANGEPASS.items():
            assert self.is_element_present(*elem_path), f'{elem_name} is not presented'

    def should_not_be_responsible_change_password(self, action: str):
        match action:
            case PersonPage.NOT_PRESENT:
                for elem_name, elem_path in ResponsiblePageLocators.RESPONSIBLE_CHANGEPASS.items():
                    assert self.is_not_element_present(*elem_path), f'{elem_name} is presented, but it shouldn\'t be'
            case PersonPage.DISAPPEAR:
                for elem_name, elem_path in ResponsiblePageLocators.RESPONSIBLE_CHANGEPASS.items():
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
