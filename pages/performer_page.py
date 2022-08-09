from base_page import BasePage
from locators import PerformerPageLocators


class PerformerPage(BasePage):
    def should_be_add_performer_button(self):
        assert self.is_element_present(*PerformerPageLocators.ADD_PERFORMER_BTN), \
            'Add performer button is not presented'

    def go_to_add_performer(self):
        self.browser.find_element(*PerformerPageLocators.ADD_PERFORMER_BTN).click()

    def should_be_performer_creation(self):
        assert self.is_element_present(*PerformerPageLocators.PERFORMER_ID_INPUT), \
            'Performer ID input is not presented'
        assert self.is_element_present(*PerformerPageLocators.OPERFORMER_FIO_INPUT), \
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

    def should_not_be_performer_creation(self, pres_or_dis: str):
        if pres_or_dis == 'pres':
            assert self.is_not_element_present(*PerformerPageLocators.PERFORMER_ID_INPUT), \
                'Performer ID input is presented, but it shouldn\'t be'
            assert self.is_not_element_present(*PerformerPageLocators.OPERFORMER_FIO_INPUT), \
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
        elif pres_or_dis == 'dis':
            assert self.is_disappeared(*PerformerPageLocators.PERFORMER_ID_INPUT), \
                'Performer ID input is presented, but it shouldn\'t be'
            assert self.is_disappeared(*PerformerPageLocators.OPERFORMER_FIO_INPUT), \
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
