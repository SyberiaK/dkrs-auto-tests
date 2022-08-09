import datetime as dt
import time

from .work_page_READONLY import WorkPage
from selenium.webdriver.common.keys import Keys
from .locators import WorkPageLocators, OrderPageLocators

# Данный код не подразумевается для использования в основном коде для тестов
# и предназначен лишь в качестве источника с готовой реализацией класса страницы
# и относящихся к ней методов (грубо говоря, шаблон). Подлежит удалению.


class OrderPage(WorkPage):
    def should_be_create_order_button(self):
        assert self.is_element_present(*OrderPageLocators.CREATE_ORDER_BTN), 'Add order button is not presented'

    def should_be_order_creation(self):
        assert self.is_element_present(*OrderPageLocators.ORDER_NUMBER_INPUT), 'Order number input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DATE_INPUT), 'Order date input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_SHOP_INPUT), 'Order shop input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_PROVIDER_INPUT), 'Order provider input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_SAVE_BTN), 'Order save button is not presented'

    def should_not_be_order_creation(self, pres_or_dis: str):
        if pres_or_dis == 'pres':
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_NUMBER_INPUT), 'Order number input is presented, but it shouldn\'t be'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_DATE_INPUT), 'Order date input is presented, but it shouldn\'t be'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_SHOP_INPUT), 'Order shop input is presented, but it shouldn\'t be'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_PROVIDER_INPUT), 'Order provider input is presented, but it shouldn\'t be'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_SAVE_BTN), 'Order save button is presented, but it shouldn\'t be'
        elif pres_or_dis == 'dis':
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_NUMBER_INPUT), 'Order number input is presented, but it shouldn\'t be'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_DATE_INPUT), 'Order date input is presented, but it shouldn\'t be'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_SHOP_INPUT), 'Order shop input is presented, but it shouldn\'t be'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_PROVIDER_INPUT), 'Order provider input is presented, but it shouldn\'t be'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_SAVE_BTN), 'Order save button is presented, but it shouldn\'t be'

    def go_to_create_order(self):
        self.browser.find_element(*OrderPageLocators.CREATE_ORDER_BTN).click()

    def create_order(self,
                     number: str = f'AUTOTEST_{int(time.time())}',
                     date: str = dt.date.today().strftime("%d.%m.%Y"),
                     shop: str = 'Magazine №2',
                     provider: str = 'Firma Regress'):
        self.browser.find_element(*OrderPageLocators.ORDER_NUMBER_INPUT).send_keys(number)
        if date:
            self.browser.find_element(*OrderPageLocators.ORDER_DATE_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*OrderPageLocators.ORDER_DATE_INPUT).send_keys(date)
            self.browser.find_element(*OrderPageLocators.ORDER_NUMBER_INPUT).click()
            time.sleep(.5)
        self.browser.find_element(*OrderPageLocators.ORDER_SHOP_INPUT).click()
        time.sleep(.5)
        for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
            if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == shop:
                self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No shop found with this name: {shop}')
        self.browser.find_element(*OrderPageLocators.ORDER_PROVIDER_INPUT).click()
        time.sleep(.5)
        for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
            if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == provider:
                self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No provider found with this name: {provider}')
        self.browser.find_element(*OrderPageLocators.ORDER_SAVE_BTN).click()

    def check_order_info(self,
                         expected_number: str,
                         expected_date: str = dt.date.today().strftime("%d.%m.%Y"),
                         expected_provider: str = 'Firma Regress',
                         expected_netto: str = '0',
                         expected_status: str = 'Entwurf'):
        actual_number = self.browser.find_element(*OrderPageLocators.ORDER_INFO_NUMBER).text
        actual_date = self.browser.find_element(*OrderPageLocators.ORDER_INFO_DATE).text
        actual_provider = self.browser.find_element(*OrderPageLocators.ORDER_INFO_PROVIDER).text
        actual_netto = self.browser.find_element(*OrderPageLocators.ORDER_INFO_NETTO).text
        actual_status = self.browser.find_element(*OrderPageLocators.ORDER_INFO_STATUS).text

        assert actual_number == expected_number, f'Actual number: {actual_number}, ' \
                                                 f'expected: {expected_number}'
        assert actual_date == expected_date, f'Actual date: {actual_date}, ' \
                                             f'expected: {expected_date}'
        assert actual_provider == expected_provider, f'Actual provider: {actual_provider}, ' \
                                                     f'expected: {expected_provider}'
        assert actual_netto == expected_netto, f'Actual netto: {actual_netto}, ' \
                                               f'expected: {expected_netto}'
        assert actual_status == expected_status, f'Actual status: {actual_status}, ' \
                                                 f'expected: {expected_status}'

        if actual_status == 'Abgesagt':
            self.go_to_work()
            finish_btn_state = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_FINISH_BTN).get_attribute(
                "disabled")
            cancel_btn_state = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_CANCEL_BTN).get_attribute(
                "disabled")
            save_btn_state = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_SAVE_BTN).get_attribute(
                "disabled")
            add_btn_state = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_ADD_BTN).get_attribute(
                "disabled")
            assert finish_btn_state == "true", 'Finish button is not disabled, but it should be'
            assert cancel_btn_state == "true", 'Cancel button is not disabled, but it should be'
            assert save_btn_state == "true", 'Save button is not disabled, but it should be'
            assert add_btn_state == "true", 'Add button is not disabled, but it should be'

    def should_be_order_draft(self):
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_NUMBER_INPUT), \
            'Order draft number input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_DATE_INPUT), \
            'Order draft date input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_SHOP_INPUT), \
            'Order draft shop input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_PROVIDER_INPUT), \
            'Order draft provider input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_DOWNLOAD_BTN), \
            'Order draft download button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_CANCEL_BTN), \
            'Order draft cancel button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_FINISH_BTN), \
            'Order draft finish button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_SAVE_BTN), \
            'Order draft save button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_ADD_BTN), \
            'Order draft add element button is not presented'

    def should_not_be_order_draft(self):
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_NUMBER_INPUT), \
            'Order draft number input is presented, but it shouldn\'t be'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_DATE_INPUT), \
            'Order draft date input is presented, but it shouldn\'t be'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_SHOP_INPUT), \
            'Order draft shop input is presented, but it shouldn\'t be'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_PROVIDER_INPUT), \
            'Order draft provider input is presented, but it shouldn\'t be'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_DOWNLOAD_BTN), \
            'Order draft download button is presented, but it shouldn\'t be'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_CANCEL_BTN), \
            'Order draft cancel button is presented, but it shouldn\'t be'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_FINISH_BTN), \
            'Order draft finish button is presented, but it shouldn\'t be'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_SAVE_BTN), \
            'Order draft save button is presented, but it shouldn\'t be'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_ADD_BTN), \
            'Order draft add element button is presented, but it shouldn\'t be'

    def check_order_draft_info(self,
                               expected_number: str,
                               expected_date=dt.date.today().strftime("%d.%m.%Y"),
                               expected_shop: str = 'Magazine №2',
                               expected_provider: str = 'Firma Regress'):
        time.sleep(1)
        actual_number = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_NUMBER_INPUT)\
                                    .get_attribute('value')
        actual_date = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_DATE_INPUT)\
                                  .get_attribute('value')
        actual_shop = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_SHOP_INPUT)\
                                  .get_attribute('value')
        actual_provider = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_PROVIDER_INPUT)\
                                      .get_attribute('value')

        assert actual_number == expected_number, f'Actual number: {actual_number}, expected: {expected_number}'
        assert actual_date == expected_date, f'Actual date: {actual_date}, expected: {expected_date}'
        assert actual_shop == expected_shop, f'Actual shop: {actual_shop}, expected: {expected_shop}'
        assert actual_provider == expected_provider, \
            f'Actual provider: {actual_provider}, expected: {expected_provider}'

    def edit_order(self,
                   number: str = None,
                   date: str = None,
                   shop: str = None,
                   provider: str = None):
        if not (number or date or shop or provider):
            raise AssertionError(f'No edit')
        if number:
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_NUMBER_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_NUMBER_INPUT).send_keys(number)
        if date:
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_DATE_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_DATE_INPUT).send_keys(date)
        if shop:
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_SHOP_INPUT).click()
            time.sleep(.5)
            for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
                if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == shop:
                    self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No shop found with this name: {shop}')
        if provider:
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_PROVIDER_INPUT).click()
            time.sleep(.5)
            for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
                if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == provider:
                    self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No provider found with this name: {provider}')

    def save_order(self):
        time.sleep(1)
        self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_SAVE_BTN).click()
        time.sleep(2)

    def change_order_status(self,
                            status: str):
        if status == 'finish':
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_FINISH_BTN).click()
        elif status == 'cancel':
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_CANCEL_BTN).click()
        else:
            raise AssertionError(f'Wrong status (statuses avaliable: finish, cancel)')

    def should_be_element_creation(self):
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_TYPE_INPUT), 'Element type input is not presented'
        assert self.is_element_present(
            *OrderPageLocators.ORDER_ELEM_PRODUCT_INPUT), 'Element product input is not presented'
        assert self.is_element_present(
            *OrderPageLocators.ORDER_ELEM_COUNT_INPUT), 'Element count input is not presented'
        assert self.is_element_present(
            *OrderPageLocators.ORDER_ELEM_ACCOUNT_INPUT), 'Element account input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_MVZ_INPUT), 'Element MVZ input is not presented'
        assert self.is_element_present(
            *OrderPageLocators.ORDER_ELEM_INNER_INPUT), 'Element inner order input is not presented'
        assert self.is_element_present(
            *OrderPageLocators.ORDER_ELEM_PRICE_INPUT), 'Element price input is not presented'
        assert self.is_element_present(
            *OrderPageLocators.ORDER_ELEM_STORAGE_INPUT), 'Element storage input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_ROW_INPUT), 'Element row input is not presented'
        assert self.is_element_present(
            *OrderPageLocators.ORDER_ELEM_STACK_INPUT), 'Element stack input is not presented'
        assert self.is_element_present(
            *OrderPageLocators.ORDER_ELEM_BOARD_INPUT), 'Element board input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_CELL_INPUT), 'Element cell input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_SAVE_BTN), 'Element save button is not presented'

    def should_not_be_element_creation(self, pres_or_dis: str):
        if pres_or_dis == 'pres':
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_ELEM_TYPE_INPUT), 'Element type input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_ELEM_PRODUCT_INPUT), 'Element product input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_ELEM_COUNT_INPUT), 'Element count input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_ELEM_ACCOUNT_INPUT), 'Element account input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_ELEM_MVZ_INPUT), 'Element MVZ input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_ELEM_INNER_INPUT), 'Element inner order input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_ELEM_PRICE_INPUT), 'Element price input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_ELEM_STORAGE_INPUT), 'Element storage input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_ELEM_ROW_INPUT), 'Element row input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_ELEM_STACK_INPUT), 'Element stack input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_ELEM_BOARD_INPUT), 'Element board input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_ELEM_CELL_INPUT), 'Element cell input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *OrderPageLocators.ORDER_ELEM_SAVE_BTN), 'Element save button is presented, but it shouldn\'t'
        elif pres_or_dis == 'dis':
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_ELEM_TYPE_INPUT), 'Element type input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_ELEM_PRODUCT_INPUT), 'Element product input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_ELEM_COUNT_INPUT), 'Element count input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_ELEM_ACCOUNT_INPUT), 'Element account input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_ELEM_MVZ_INPUT), 'Element MVZ input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_ELEM_INNER_INPUT), 'Element inner order input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_ELEM_PRICE_INPUT), 'Element price input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_ELEM_STORAGE_INPUT), 'Element storage input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_ELEM_ROW_INPUT), 'Element row input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_ELEM_STACK_INPUT), 'Element stack input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_ELEM_BOARD_INPUT), 'Element board input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_ELEM_CELL_INPUT), 'Element cell input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *OrderPageLocators.ORDER_ELEM_SAVE_BTN), 'Element save button is presented, but it shouldn\'t'

    def go_to_create_element(self):
        self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_ADD_BTN).click()

    def create_element(self, ttype: str = 'K',
                       product: str = 'Dichtung DN 65, NBR (blau), '
                                      '71x81x5,0mmDichtung DN 65, NBR (blau),'
                                      ' 71x81x5,0mm Alle Werkstoffe entsp... (0001)',
                       count: int = 3,
                       account: str = 'Regress sachkonto (003)',
                       mvz: str = 'Double Regress MVZ (001)',
                       inner: str = 'Double regress inner order (001)',
                       price: float = 16.00,
                       storage: str = 'Lager of Magazine №2',
                       row: str = 'Reihe 1',
                       stack: str = 'Stack 1',
                       board: str = 'Board 1',
                       cell: str = 'Cell 1',
                       subcell: str = 'Подяейка 1'):
        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_TYPE_INPUT).click()
        time.sleep(1)
        for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
            if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == ttype:
                self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No element type found with this name: {ttype}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_PRODUCT_INPUT).click()
        time.sleep(2)
        for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT))):
            if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].text == product:
                self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No product found with this name: {product}')
        time.sleep(1)
        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_COUNT_INPUT).send_keys(str(count))

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_ACCOUNT_INPUT).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_ACCOUNT_INPUT).send_keys(Keys.DELETE)
        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_ACCOUNT_INPUT).click()
        time.sleep(1)
        for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT))):
            if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].text == account:
                self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No account found with this name: {account}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_MVZ_INPUT).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_MVZ_INPUT).send_keys(Keys.DELETE)
        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_MVZ_INPUT).click()
        time.sleep(.5)
        for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT))):
            if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].text == mvz:
                self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No MVZ found with this name: {mvz}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INNER_INPUT).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INNER_INPUT).send_keys(Keys.DELETE)
        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INNER_INPUT).click()
        time.sleep(1)
        for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT))):
            if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].text == inner:
                self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No inner order found with this name: {inner}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_PRICE_INPUT).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_PRICE_INPUT).send_keys(str(price))

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_STORAGE_INPUT).click()
        time.sleep(2)
        for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT))):
            if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].text == storage:
                self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No storage found with this name: {storage}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_ROW_INPUT).click()
        time.sleep(2)
        for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
            if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == row:
                self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No row found with this name: {row}')

        self.browser.execute_script("return arguments[0].scrollIntoView(true);",
                                    self.browser.find_element(*OrderPageLocators.ORDER_ELEM_ROW_INPUT))

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_STACK_INPUT).click()
        time.sleep(2)
        for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
            if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == stack:
                self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No stack found with this name: {stack}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_BOARD_INPUT).click()
        time.sleep(2)
        for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
            if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == board:
                self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No board found with this name: {board}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_CELL_INPUT).click()
        time.sleep(2)
        for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
            if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == cell:
                self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No cell found with this name: {cell}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_SUBCELL_INPUT).click()
        time.sleep(2)
        for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
            if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == subcell:
                self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No subcell found with this name: {subcell}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_SAVE_BTN).click()

    def go_to_cancel_element(self):
        self.browser.find_element(*WorkPageLocators.WORK_CLOSE_BTN).click()

    def check_element_info(self,
                           expected_type: str = 'K',
                           expected_account: str = 'Regress sachkonto',
                           expected_mvz: str = 'Double Regress MVZ',
                           expected_inner: str = 'Double regress inner order',
                           expected_product: str = 'Dichtung DN 65, NBR (blau), 71x81x5,0mmDichtung DN 65, NBR (blau),'
                                                   ' 71x81x5,0mm Alle Werkstoffe entsp',
                           expected_count: str = '3',
                           expected_netto: str = "48,00",
                           expected_price: str = "16,00",
                           expected_unit: str = 'Stuck'):
        expected_count, expected_netto, expected_price = str(expected_count), str(expected_netto), str(expected_price)
        actual_type = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_TYPE).text
        actual_account = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_ACCOUNT).text
        actual_mvz = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_MVZ).text
        actual_inner = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_INNER).text
        actual_product = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_PRODUCT).text
        actual_count = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_COUNT).text
        actual_netto = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_NETTO).text
        actual_price = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_PRICE).text
        actual_unit = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_UNIT).text

        assert actual_type == expected_type, f'Actual type: {actual_type}, expected: {expected_type}'
        assert actual_account.startswith(expected_account), \
            f'Actual account: {actual_account}, expected: {expected_account}'
        assert actual_mvz == expected_mvz, f'Actual MVZ: {actual_mvz}, expected: {expected_mvz}'
        assert actual_inner.startswith(expected_inner), \
            f'Actual inner order: {actual_inner}, expected: {expected_inner}'
        assert actual_product.startswith(expected_product), f'Actual product: {actual_product}, expected: {expected_product}'
        assert actual_count == expected_count, f'Actual count: {actual_count}, expected: {expected_count}'
        assert actual_netto == expected_netto, f'Actual netto: {actual_netto}, expected: {expected_netto}'
        assert actual_price == expected_price, f'Actual price: {actual_price}, expected: {expected_price}'
        assert actual_unit == expected_unit, f'Actual unit: {actual_unit}, expected: {expected_unit}'

    def should_be_any_element(self):
        assert self.is_element_present(*WorkPageLocators.WORK_ELEM_INFO), f'No element found'

    def should_not_be_any_element(self):
        assert self.is_not_element_present(
            *WorkPageLocators.WORK_ELEM_INFO), f'Element was found, but it shouldn\'t be'

    def go_to_delete_element(self):
        self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_DELETE_ELEM_BTN).click()

    def count_elements(self, count: int):
        elements = self.browser.find_elements(*WorkPageLocators.WORK_ELEM_INFO)
        assert len(elements) == count, f'Actual number of elements is {len(elements)}, expected: {count}'

    def go_to_edit_element(self):
        self.browser.find_element(*WorkPageLocators.WORK_ELEM_INFO).click()

    def edit_element(self, ttype: str = None,
                     product: str = None,
                     count: int = None,
                     account: str = None,
                     mvz: str = None,
                     inner: str = None,
                     price: float = None,
                     storage: str = None,
                     row: str = None,
                     stack: str = None,
                     board: str = None,
                     cell: str = None,
                     subcell: str = None):
        if not (ttype or product or count or account or mvz
                or inner or price or storage or row or stack or board or cell or subcell):
            raise AssertionError(f'No edit')
        if ttype:
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_TYPE_INPUT).click()
            time.sleep(1)
            for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
                if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == ttype:
                    self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No element type found with this name: {ttype}')
        if product:
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_PRODUCT_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_PRODUCT_INPUT).send_keys(Keys.DELETE)
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_PRODUCT_INPUT).click()
            time.sleep(2)
            for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT))):
                if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].text == product:
                    self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No product found with this name: {product}')
            time.sleep(1)
        if count:
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_COUNT_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_COUNT_INPUT).send_keys(str(count))
        if account:
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_ACCOUNT_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_ACCOUNT_INPUT).send_keys(Keys.DELETE)
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_ACCOUNT_INPUT).click()
            time.sleep(2)
            for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT))):
                if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].text == account:
                    self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No account found with this name: {account}')
        if mvz:
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_MVZ_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_MVZ_INPUT).send_keys(Keys.DELETE)
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_MVZ_INPUT).click()
            time.sleep(1)
            for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT))):
                if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].text == mvz:
                    self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No MVZ found with this name: {mvz}')
        if inner:
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INNER_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INNER_INPUT).send_keys(Keys.DELETE)
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INNER_INPUT).click()
            time.sleep(1)
            for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT))):
                if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].text == inner:
                    self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No inner order found with this name: {inner}')
        if price:
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_PRICE_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_PRICE_INPUT).send_keys(str(price))
        if storage:
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_STORAGE_INPUT).click()
            time.sleep(2)
            for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
                if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == storage:
                    self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No storage found with this name: {storage}')
        if row:
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_ROW_INPUT).click()
            time.sleep(2)
            for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
                if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == row:
                    self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No row found with this name: {row}')

        self.browser.execute_script("return arguments[0].scrollIntoView(true);",
                                    self.browser.find_element(*OrderPageLocators.ORDER_ELEM_ROW_INPUT))
        if stack:
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_STACK_INPUT).click()
            time.sleep(2)
            for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
                if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == stack:
                    self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No stack found with this name: {stack}')
        if board:
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_BOARD_INPUT).click()
            time.sleep(2)
            for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
                if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == board:
                    self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No board found with this name: {board}')
        if cell:
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_CELL_INPUT).click()
            time.sleep(2)
            for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
                if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == cell:
                    self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No cell found with this name: {cell}')
        if subcell:
            self.browser.find_element(*OrderPageLocators.ORDER_ELEM_SUBCELL_INPUT).click()
            time.sleep(3)
            for i in range(len(self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN))):
                if self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == subcell:
                    self.browser.find_elements(*WorkPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No subcell found with this name: {subcell}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_SAVE_BTN).click()
