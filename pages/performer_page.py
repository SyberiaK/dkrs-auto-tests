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
        assert self.is_element_present(*PerformerPageLocators.PERFORMER_ID_INPUT), \
            'Performer ID input is not presented'
        assert self.is_element_present(*PerformerPageLocators.PERFORMER_FIO_INPUT), \
            'Performer FIO input is not presented'
        assert self.is_element_present(*PerformerPageLocators.PERFORMER_BIRTHYEAR_INPUT), \
            'Performer birth year input is not presented'
        assert self.is_element_present(*PerformerPageLocators.PERFORMER_PASSPORT_INPUT), \
            'Performer passport input is not presented'
        assert self.is_element_present(*PerformerPageLocators.PERFORMER_INN_INPUT), \
            'Performer INN input is not presented'
        assert self.is_element_present(*PerformerPageLocators.PERFORMER_PHONE_INPUT), \
            'Performer phone input is not presented'
        assert self.is_element_present(*PerformerPageLocators.PERFORMER_BANKCARD_INPUT), \
            'Performer bank card input is not presented'
        assert self.is_element_present(*PerformerPageLocators.PERFORMER_SAVE_BTN), \
            'Performer save button is not presented'

    def should_not_be_performer_creation(self, action: str):
        match action:
            case PersonPage.NOT_PRESENT:
                assert self.is_not_element_present(*PerformerPageLocators.PERFORMER_ID_INPUT), \
                    'Performer ID input is presented, but it shouldn\'t be'
                assert self.is_not_element_present(*PerformerPageLocators.PERFORMER_FIO_INPUT), \
                    'Performer FIO input is presented, but it shouldn\'t be'
                assert self.is_not_element_present(*PerformerPageLocators.PERFORMER_BIRTHYEAR_INPUT), \
                    'Performer birth year input is presented, but it shouldn\'t be'
                assert self.is_not_element_present(*PerformerPageLocators.PERFORMER_PASSPORT_INPUT), \
                    'Performer passport input is presented, but it shouldn\'t be'
                assert self.is_not_element_present(*PerformerPageLocators.PERFORMER_INN_INPUT), \
                    'Performer INN input is presented, but it shouldn\'t be'
                assert self.is_not_element_present(*PerformerPageLocators.PERFORMER_PHONE_INPUT), \
                    'Performer phone input is presented, but it shouldn\'t be'
                assert self.is_not_element_present(*PerformerPageLocators.PERFORMER_BANKCARD_INPUT), \
                    'Performer bank card input is presented, but it shouldn\'t be'
                assert self.is_not_element_present(*PerformerPageLocators.PERFORMER_SAVE_BTN), \
                    'Performer save button is presented, but it shouldn\'t be'
            case PersonPage.DISAPPEAR:
                assert self.is_disappeared(*PerformerPageLocators.PERFORMER_ID_INPUT), \
                    'Performer ID input is presented, but it shouldn\'t be'
                assert self.is_disappeared(*PerformerPageLocators.PERFORMER_FIO_INPUT), \
                    'Performer FIO input is presented, but it shouldn\'t be'
                assert self.is_disappeared(*PerformerPageLocators.PERFORMER_BIRTHYEAR_INPUT), \
                    'Performer birth year input is presented, but it shouldn\'t be'
                assert self.is_disappeared(*PerformerPageLocators.PERFORMER_PASSPORT_INPUT), \
                    'Performer passport input is presented, but it shouldn\'t be'
                assert self.is_disappeared(*PerformerPageLocators.PERFORMER_INN_INPUT), \
                    'Performer INN input is presented, but it shouldn\'t be'
                assert self.is_disappeared(*PerformerPageLocators.PERFORMER_PHONE_INPUT), \
                    'Performer phone input is presented, but it shouldn\'t be'
                assert self.is_disappeared(*PerformerPageLocators.PERFORMER_BANKCARD_INPUT), \
                    'Performer bank card input is presented, but it shouldn\'t be'
                assert self.is_disappeared(*PerformerPageLocators.PERFORMER_SAVE_BTN), \
                    'Performer save button is presented, but it shouldn\'t be'

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
        actual_id = self.browser.find_element(*PerformerPageLocators.PERFORMER_INFO_ID).text
        actual_date = self.browser.find_element(*PerformerPageLocators.PERFORMER_INFO_DATE).text
        actual_fio = self.browser.find_element(*PerformerPageLocators.PERFORMER_INFO_FIO).text
        actual_phone = self.browser.find_element(*PerformerPageLocators.PERFORMER_INFO_PHONE).text

        assert actual_id == expected_id, f'Actual performer id: {actual_id}, ' \
                                         f'expected: {expected_id}'
        assert actual_date == expected_date, f'Actual date: {actual_date}, ' \
                                             f'expected: {expected_date}'
        assert actual_fio == expected_fio, f'Actual FIO: {actual_fio}, ' \
                                           f'expected: {expected_fio}'
        assert actual_phone == expected_phone, f'Actual phone: {actual_phone}, ' \
                                               f'expected: {expected_phone}'

    def go_to_blacklist(self):
        self.browser.find_element(*PerformerPageLocators.PERFORMER_ADD_TO_BLACKLIST_BTN).click()

    def blacklist(self, comment: str = str(int(time.time()))):
        self.browser.find_element(*PerformerPageLocators.PERFORMER_BL_COMMENT_INPUT).send_keys(comment)
        self.browser.find_element(*PerformerPageLocators.PERFORMER_BL_CONFIRM_BTN).click()