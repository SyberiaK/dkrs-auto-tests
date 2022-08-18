import time
import datetime as dt
from selenium.webdriver.common.keys import Keys

from .person_page import PersonPage
from .locators import PersonPageLocators, PerformerPageLocators


class PerformerPage(PersonPage):
    ACTIVE_STATUS = 'Активен'
    BLACKLIST_STATUS = 'В черном списке'

    def should_be_add_performer_button(self):
        assert self.is_element_present(*PerformerPageLocators.ADD_PERFORMER_BTN), \
            'Add performer button is not presented'

    def go_to_add_performer(self):
        self.browser.find_element(*PerformerPageLocators.ADD_PERFORMER_BTN).click()

    def should_be_performer_creation(self):
        for elem_name, elem_path in PerformerPageLocators.PERFORMER_CREATION.items():
            assert self.is_element_present(*elem_path), f'{elem_name} is not presented'

    def should_not_be_performer_creation(self, action: str):
        match action:
            case PersonPage.NOT_PRESENT:
                for elem_name, elem_path in PerformerPageLocators.PERFORMER_CREATION.items():
                    assert self.is_not_element_present(*elem_path), f'{elem_name} is presented, but it shouldn\'t be'
            case PersonPage.DISAPPEAR:
                for elem_name, elem_path in PerformerPageLocators.PERFORMER_CREATION.items():
                    assert self.is_disappeared(*elem_path), f'{elem_name} is presented, but it should disappear'

    def add_performer(self,
                      fio: str,
                      birth_year: str,
                      passport: str,
                      phone: str,
                      performer_id: str = None,
                      inn: str = None,
                      bank_card: str = None):
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
        time.sleep(1)

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
        for elem_name, elem_path in PerformerPageLocators.PERFORMER_DETAILED_INFO.items():
            assert self.is_element_present(*elem_path), f'{elem_name} is not presented'

    def should_not_be_performer_detailed_info(self, action: str):
        match action:
            case PersonPage.NOT_PRESENT:
                for elem_name, elem_path in PerformerPageLocators.PERFORMER_DETAILED_INFO.items():
                    assert self.is_not_element_present(*elem_path), f'{elem_name} is presented, but it shouldn\'t be'
            case PersonPage.DISAPPEAR:
                for elem_name, elem_path in PerformerPageLocators.PERFORMER_DETAILED_INFO.items():
                    assert self.is_disappeared(*elem_path), f'{elem_name} is presented, but it should disappear'

    def check_performer_detailed_info(self,
                                      expected_fio: str,
                                      expected_birthyear: str,
                                      expected_passport: str,
                                      expected_phone: str,
                                      expected_id: str = None,
                                      expected_inn: str = None,
                                      expected_bankcard: str = None,
                                      expected_status: str = ACTIVE_STATUS,
                                      expected_comment: str = ''):
        expected_id = expected_id if expected_id else '<EMPTY>'
        expected_fio = expected_fio if expected_fio else '<EMPTY>'
        expected_birthyear = expected_birthyear if expected_birthyear else '<EMPTY>'
        expected_passport = expected_passport if expected_passport else '<EMPTY>'
        expected_inn = expected_inn if expected_inn else '<EMPTY>'
        expected_phone = expected_phone if expected_phone else '<EMPTY>'
        expected_bankcard = expected_bankcard if expected_bankcard else '<EMPTY>'
        expected_status = expected_status if expected_status else '<EMPTY>'

        actual_id = self.browser.find_element(*PerformerPageLocators
                                              .PERFORMER_DETAILED_INFO_ID_INPUT).get_property('value')
        actual_fio = self.browser.find_element(*PerformerPageLocators
                                               .PERFORMER_DETAILED_INFO_FIO_INPUT).get_property('value')
        actual_birthyear = self.browser.find_element(*PerformerPageLocators
                                                     .PERFORMER_DETAILED_INFO_BIRTHYEAR_INPUT).get_property('value')
        actual_passport = self.browser.find_element(*PerformerPageLocators
                                                    .PERFORMER_DETAILED_INFO_PASSPORT_INPUT).get_property('value')
        actual_inn = self.browser.find_element(*PerformerPageLocators
                                               .PERFORMER_DETAILED_INFO_INN_INPUT).get_property('value')
        actual_phone = self.browser.find_element(*PerformerPageLocators
                                                 .PERFORMER_DETAILED_INFO_PHONE_INPUT).get_property('value')
        actual_bankcard = self.browser.find_element(*PerformerPageLocators
                                                    .PERFORMER_DETAILED_INFO_BANKCARD_INPUT).get_property('value')
        actual_status = self.browser.find_element(*PerformerPageLocators
                                                  .PERFORMER_DETAILED_INFO_STATUS_INPUT).get_property('value')

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
        assert actual_passport == expected_passport, f'Actual passport: {actual_passport}, ' \
                                                     f'expected: {expected_passport}'
        assert actual_inn == expected_inn, f'Actual INN: {actual_inn}, ' \
                                           f'expected: {expected_inn}'
        assert actual_phone == expected_phone, f'Actual phone: {actual_phone}, ' \
                                               f'expected: {expected_phone}'
        assert actual_bankcard == expected_bankcard, f'Actual bank card: {actual_bankcard}, ' \
                                                     f'expected: {expected_bankcard}'
        assert actual_status == expected_status, f'Actual status: {actual_status}, ' \
                                                 f'expected: {expected_status}'

        if actual_status == 'В черном списке':
            expected_comment = expected_comment if expected_comment else '<EMPTY>'

            assert self.is_element_present(*PerformerPageLocators.PERFORMER_BL_DETAILED_INFO_COMMENT_INPUT), \
                f'Performer status is {actual_status}, but there are no comment input'

            actual_comment = self.browser\
                .find_element(*PerformerPageLocators.PERFORMER_BL_DETAILED_INFO_COMMENT_INPUT).get_property('value')
            actual_comment = actual_comment if actual_comment else '<EMPTY>'

            assert actual_comment == expected_comment, f'Actual comment: {actual_comment}, ' \
                                                       f'expected: {expected_comment}'

    def edit_performer(self,
                       performer_id: str = None,
                       fio: str = None,
                       birthyear: str = None,
                       passport: str = None,
                       inn: str = None,
                       phone: str = None,
                       bank_card: str = None):
        if not (fio or birthyear or passport or phone or performer_id or inn or bank_card):
            raise AssertionError('No edit')
        if performer_id:
            entry = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_ID_INPUT)
            entry.send_keys(Keys.CONTROL + "a")
            entry.send_keys(performer_id)
        if fio:
            entry = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_FIO_INPUT)
            entry.send_keys(Keys.CONTROL + "a")
            entry.send_keys(fio)
        if birthyear:
            entry = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_BIRTHYEAR_INPUT)
            entry.send_keys(Keys.CONTROL + "a")
            entry.send_keys(birthyear)
        if passport:
            entry = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_PASSPORT_INPUT)
            entry.send_keys(Keys.CONTROL + "a")
            entry.send_keys(passport)
        if inn:
            entry = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_INN_INPUT)
            entry.send_keys(Keys.CONTROL + "a")
            entry.send_keys(inn)
        if phone:
            entry = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_PHONE_INPUT)
            entry.send_keys(Keys.CONTROL + "a")
            entry.send_keys(phone)
        if bank_card:
            entry = self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_BANKCARD_INPUT)
            entry.send_keys(Keys.CONTROL + "a")
            entry.send_keys(bank_card)

    def scroll_down(self):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);",
                                    self.browser.find_element(*PerformerPageLocators
                                                              .PERFORMER_DETAILED_INFO_BANKCARD_INPUT))

    def save_performer(self):
        self.scroll_down()
        status = self.browser.find_element(*PerformerPageLocators
                                           .PERFORMER_DETAILED_INFO_STATUS_INPUT).get_property('value')
        if status == PerformerPage.BLACKLIST_STATUS:
            self.browser.find_element(*PerformerPageLocators.PERFORMER_BL_DETAILED_INFO_SAVE_BTN).click()
        else:
            self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_SAVE_BTN).click()
        time.sleep(1)

    def check_performer_selection(self, expected_result: bool):
        classes = self.browser.find_element(*PerformerPageLocators.PERFORMER_INFO_SELECT_CHECKER).get_attribute("class")
        actual_result = 'selected' in classes
        assert actual_result == expected_result, f'Performer selection, actual result: {actual_result}, ' \
                                                 f'expected: {expected_result}'

    def change_performer_status(self, status: str, comment: str = f'CHANGED_STATUS_{str(int(time.time()))}'):
        self.scroll_down()
        self.browser.find_element(*PerformerPageLocators.PERFORMER_DETAILED_INFO_STATUS_INPUT).click()
        dropdown_content_spans = self.browser.find_elements(*PersonPageLocators.DROPDOWN_CONTENT_SPAN)
        for i in range(len(dropdown_content_spans)):
            if dropdown_content_spans[i].get_attribute("innerHTML") == status:
                self.browser.find_elements(*PersonPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'Cannot find "{status}" status')
        time.sleep(1)
        if status == PerformerPage.BLACKLIST_STATUS:
            self.scroll_down()
            self.browser.find_element(*PerformerPageLocators.PERFORMER_BL_DETAILED_INFO_COMMENT_INPUT)\
                .send_keys(comment)

    def go_to_blacklist(self):
        if self.get_current_tab() == PerformerPage.ACTIVE_TAB:
            self.browser.find_element(*PerformerPageLocators.PERFORMER_ADD_TO_BLACKLIST_BTN).click()
        else:
            raise Exception('Not an active tab so can\'t go to blacklist')

    def should_be_performer_blacklist(self):
        for elem_name, elem_path in PerformerPageLocators.PERFORMER_BL.items():
            assert self.is_element_present(*elem_path), f'{elem_name} is not presented'

    def should_not_be_performer_blacklist(self, action: str):
        match action:
            case PersonPage.NOT_PRESENT:
                for elem_name, elem_path in PerformerPageLocators.PERFORMER_BL.items():
                    assert self.is_not_element_present(*elem_path), f'{elem_name} is presented, but it shouldn\'t be'
            case PersonPage.DISAPPEAR:
                for elem_name, elem_path in PerformerPageLocators.PERFORMER_BL.items():
                    assert self.is_disappeared(*elem_path), f'{elem_name} is presented, but it should disappear'

    def blacklist(self, comment: str = str(int(time.time()))):
        self.browser.find_element(*PerformerPageLocators.PERFORMER_BL_COMMENT_INPUT).send_keys(comment)
        self.browser.find_element(*PerformerPageLocators.PERFORMER_BL_CONFIRM_BTN).click()

    def cancel_blacklist(self):
        self.browser.find_element(*PerformerPageLocators.PERFORMER_BL_CANCEL_BTN).click()

    def go_to_unblacklist(self):
        if self.get_current_tab() == PerformerPage.REMOVED_TAB:
            self.browser.find_element(*PerformerPageLocators.PERFORMER_ADD_TO_BLACKLIST_BTN).click()
        else:
            raise Exception('Not a blacklist tab so can\'t go to unblacklist')

    def should_be_performer_unblacklist(self):
        for elem_name, elem_path in PerformerPageLocators.PERFORMER_UNBL.items():
            assert self.is_element_present(*elem_path), f'{elem_name} is not presented'

    def should_not_be_performer_unblacklist(self, action: str):
        match action:
            case PersonPage.NOT_PRESENT:
                for elem_name, elem_path in PerformerPageLocators.PERFORMER_UNBL.items():
                    assert self.is_not_element_present(*elem_path), f'{elem_name} is presented, but it shouldn\'t be'
            case PersonPage.DISAPPEAR:
                for elem_name, elem_path in PerformerPageLocators.PERFORMER_UNBL.items():
                    assert self.is_disappeared(*elem_path), f'{elem_name} is presented, but it should disappear'

    def unblacklist(self):
        self.browser.find_element(*PerformerPageLocators.PERFORMER_UNBL_CONFIRM_BTN).click()

    def cancel_unblacklist(self):
        self.browser.find_element(*PerformerPageLocators.PERFORMER_UNBL_CANCEL_BTN).click()
