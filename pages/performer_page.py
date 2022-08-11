import time
import datetime as dt

from .person_page import PersonPage
from .locators import PerformerPageLocators


class PerformerPage(PersonPage):

    def should_be_add_performer_button(self):
        assert self.is_element_present(*PerformerPageLocators.ADD_PERFORMER_BTN), \
            'Add performer button is not presented'

    def go_to_add_performer(self):
        self.browser.find_element(*PerformerPageLocators.ADD_PERFORMER_BTN).click()

    def should_be_performer_creation(self):
        for key, val in PerformerPageLocators.PERFORMER_CREATION.items():
            assert self.is_element_present(*val), f'{key} is not presented'

    def should_not_be_performer_creation(self, action: str):
        match action:
            case PersonPage.NOT_PRESENT:
                for key, val in PerformerPageLocators.PERFORMER_CREATION.items():
                    assert self.is_not_element_present(*val), f'{key} is presented, but it shouldn\'t be'
            case PersonPage.DISAPPEAR:
                for key, val in PerformerPageLocators.PERFORMER_CREATION.items():
                    assert self.is_disappeared(*val), f'{key} is presented, but it should disappear'

    def add_performer(self,
                      fio: str,
                      birth_year: str,
                      passport: str,
                      phone: str,
                      performer_id: str = '',
                      inn: str = '',
                      bank_card: str = ''):
        if performer_id:
            self.browser.find_element(*PerformerPageLocators.PERFORMER_ID_INPUT).send_keys(performer_id)
        self.browser.find_element(*PerformerPageLocators.PERFORMER_FIO_INPUT).send_keys(fio)
        self.browser.find_element(*PerformerPageLocators.PERFORMER_BIRTHYEAR_INPUT).send_keys(birth_year)
        self.browser.find_element(*PerformerPageLocators.PERFORMER_PASSPORT_INPUT).send_keys(passport)
        if inn:
            self.browser.find_element(*PerformerPageLocators.PERFORMER_INN_INPUT).send_keys(inn)
        self.browser.find_element(*PerformerPageLocators.PERFORMER_PHONE_INPUT).send_keys(phone)
        if bank_card:
            self.browser.find_element(*PerformerPageLocators.PERFORMER_BANKCARD_INPUT).send_keys(bank_card)
        self.browser.find_element(*PerformerPageLocators.PERFORMER_SAVE_BTN).click()

    def check_performer_info(self,
                             expected_fio: str,
                             expected_phone: str,
                             expected_id: str = '-',
                             expected_date: str = dt.date.today().strftime("%d.%m.%Y")):
        expected_id = expected_id if expected_id else '<EMPTY>'
        expected_date = expected_date if expected_date else '<EMPTY>'
        expected_fio = expected_fio if expected_fio else '<EMPTY>'
        expected_phone = expected_phone if expected_phone else '<EMPTY>'

        actual_id = self.browser.find_element(*PerformerPageLocators.PERFORMER_INFO_ID).text
        actual_date = self.browser.find_element(*PerformerPageLocators.PERFORMER_INFO_DATE).text
        actual_fio = self.browser.find_element(*PerformerPageLocators.PERFORMER_INFO_FIO).text
        actual_phone = self.browser.find_element(*PerformerPageLocators.PERFORMER_INFO_PHONE).text

        actual_id = actual_id if actual_id else '<EMPTY>'
        actual_date = actual_date if actual_date else '<EMPTY>'
        actual_fio = actual_fio if actual_fio else '<EMPTY>'
        actual_phone = actual_phone if actual_phone else '<EMPTY>'

        assert actual_id == expected_id, f'Actual performer id: {actual_id}, ' \
                                         f'expected: {expected_id}'
        assert actual_date == expected_date, f'Actual date: {actual_date}, ' \
                                             f'expected: {expected_date}'
        assert actual_fio == expected_fio, f'Actual FIO: {actual_fio}, ' \
                                           f'expected: {expected_fio}'
        assert actual_phone == expected_phone, f'Actual phone: {actual_phone}, ' \
                                               f'expected: {expected_phone}'

    def should_be_performer_detailed_info(self):
        for key, val in PerformerPageLocators.PERFORMER_DETAILED_INFO.items():
            assert self.is_element_present(*val), f'{key} is not presented'

    def should_not_be_performer_detailed_info(self, action: str):
        match action:
            case PersonPage.NOT_PRESENT:
                for key, val in PerformerPageLocators.PERFORMER_DETAILED_INFO.items():
                    assert self.is_not_element_present(*val), f'{key} is presented, but it shouldn\'t be'
            case PersonPage.DISAPPEAR:
                for key, val in PerformerPageLocators.PERFORMER_DETAILED_INFO.items():
                    assert self.is_disappeared(*val), f'{key} is presented, but it should disappear'

    def check_performer_detailed_info(self,
                                      expected_fio: str,
                                      expected_birthyear: str,
                                      expected_passport: str,
                                      expected_phone: str,
                                      expected_id: str = '',
                                      expected_inn: str = '',
                                      expected_bankcard: str = '',
                                      expected_status: str = 'Активен'):
        expected_id = expected_id if expected_id else '<EMPTY>'
        expected_fio = expected_fio if expected_fio else '<EMPTY>'
        expected_birthyear = expected_birthyear if expected_birthyear else '<EMPTY>'
        expected_passport = expected_passport if expected_passport else '<EMPTY>'
        expected_inn = expected_inn if expected_inn else '<EMPTY>'
        expected_phone = expected_phone if expected_phone else '<EMPTY>'
        expected_bankcard = expected_bankcard if expected_bankcard else '<EMPTY>'
        expected_status = expected_status if expected_status else '<EMPTY>'

        actual_id = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_ID_INPUT).text
        actual_fio = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_FIO_INPUT).text
        actual_birthyear = self.browser\
            .find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_BIRTHYEAR_INPUT).text
        actual_passport = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_PASSPORT_INPUT).text
        actual_inn = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_INN_INPUT).text
        actual_phone = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_PHONE_INPUT).text
        actual_bankcard = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_BANKCARD_INPUT).text
        actual_status = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_STATUS_INPUT).text

        actual_id = actual_id if actual_id else '<EMPTY>'
        actual_fio = actual_fio if actual_fio else '<EMPTY>'
        actual_birthyear = actual_birthyear if actual_birthyear else '<EMPTY>'
        actual_passport = actual_passport if actual_passport else '<EMPTY>'
        actual_inn = actual_inn if actual_inn else '<EMPTY>'
        actual_phone = actual_phone if actual_phone else '<EMPTY>'
        actual_bankcard = actual_bankcard if actual_bankcard else '<EMPTY>'
        actual_status = actual_status if actual_status else '<EMPTY>'

        assert actual_id == expected_id, f'Actual performer id: {actual_id}, ' \
                                         f'expected: {expected_id}'
        assert actual_fio == expected_fio, f'Actual FIO: {actual_fio}, ' \
                                           f'expected: {expected_fio}'
        assert actual_birthyear == expected_birthyear, f'Actual birth year: {actual_birthyear}, ' \
                                                       f'expected: {expected_birthyear}'
        assert actual_passport == expected_passport, f'Actual FIO: {actual_passport}, ' \
                                                     f'expected: {expected_passport}'
        assert actual_inn == expected_inn, f'Actual birth year: {actual_inn}, ' \
                                           f'expected: {expected_inn}'
        assert actual_phone == expected_phone, f'Actual phone: {actual_phone}, ' \
                                               f'expected: {expected_phone}'
        assert actual_bankcard == expected_bankcard, f'Actual birth year: {actual_bankcard}, ' \
                                                     f'expected: {expected_bankcard}'
        assert actual_status == expected_status, f'Actual phone: {actual_status}, ' \
                                               f'expected: {expected_status}'

    def go_to_blacklist(self):
        self.browser.find_element(*PerformerPageLocators.PERFORMER_ADD_TO_BLACKLIST_BTN).click()

    def blacklist(self, comment: str = str(int(time.time()))):
        self.browser.find_element(*PerformerPageLocators.PERFORMER_BL_COMMENT_INPUT).send_keys(comment)
        self.browser.find_element(*PerformerPageLocators.PERFORMER_BL_CONFIRM_BTN).click()