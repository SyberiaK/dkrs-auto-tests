from selenium.webdriver.common.by import By


class AuthPageLocators:
    LOGIN_INPUT = By.CSS_SELECTOR, 'input#username'
    PASSWORD_INPUT = By.CSS_SELECTOR, 'input#password'
    LOGIN_BTN = By.CSS_SELECTOR, 'button#submit'


class PersonPageLocators:
    PEOPLE_ACTIVE_TAB = By.ID, 'tab-Active'
    PEOPLE_REMOVED_TAB = By.ID, 'tab-Removed'

    PERSON_INFO = By.CSS_SELECTOR, 'tbody tr'

    DRAWER_CLOSE_BTN = By.CSS_SELECTOR, 'button.el-drawer__close-btn'
    DIALOG_CLOSE_BTN = By.CSS_SELECTOR, 'button.el-dialog__headerbtn'
    MSGBOX_CLOSE_BTN = By.CSS_SELECTOR, 'button.el-message-box__headerbtn'

    DROPDOWN_CONTENT = By.XPATH, '//div[@aria-hidden="false"]//li'
    DROPDOWN_CONTENT_SPAN = By.XPATH, '//div[@aria-hidden="false"]//li/span'


class PerformerPageLocators:
    ADD_PERFORMER_BTN = By.XPATH, '//button[@class="el-button el-button--primary"]'

    PERFORMER_ID_INPUT = By.XPATH, '//form[@class="el-form"]/div[1]//input'
    PERFORMER_FIO_INPUT = By.XPATH, '//form[@class="el-form"]/div[2]//input'
    PERFORMER_BIRTHYEAR_INPUT = By.XPATH, '//form[@class="el-form"]/div[3]//input'
    PERFORMER_PASSPORT_INPUT = By.XPATH, '//form[@class="el-form"]/div[4]//input'
    PERFORMER_INN_INPUT = By.XPATH, '//form[@class="el-form"]/div[5]//input'
    PERFORMER_PHONE_INPUT = By.XPATH, '//form[@class="el-form"]/div[6]//input'
    PERFORMER_BANKCARD_INPUT = By.XPATH, '//form[@class="el-form"]/div[7]//input'
    PERFORMER_SAVE_BTN = By.XPATH, '//form[@class="el-form"]/div[8]//button'

    PERFORMER_CREATION = {'Performer ID input': PERFORMER_ID_INPUT,
                          'Performer FIO input': PERFORMER_FIO_INPUT,
                          'Performer birth year input': PERFORMER_BIRTHYEAR_INPUT,
                          'Performer passport input': PERFORMER_PASSPORT_INPUT,
                          'Performer INN input': PERFORMER_INN_INPUT,
                          'Performer phone input': PERFORMER_PHONE_INPUT,
                          'Performer bank card input': PERFORMER_BANKCARD_INPUT,
                          'Save performer button': PERFORMER_SAVE_BTN}

    PERFORMER_INFO_SELECT_CHECKER = By.XPATH, '//tbody/tr[1]/td[1]/div/span'
    PERFORMER_INFO_ID = By.XPATH, '//tbody/tr[1]/td[1]//span/span'
    PERFORMER_INFO_DATE = By.XPATH, '//tbody/tr[1]/td[2]//span/span'
    PERFORMER_INFO_FIO = By.XPATH, '//tbody/tr[1]/td[3]//span/span'
    PERFORMER_INFO_PHONE = By.XPATH, '//tbody/tr[1]/td[4]//span/span'
    PERFORMER_INFO_QR_LINK = By.XPATH, '//tbody/tr[1]/td[5]//a'
    PERFORMER_ADD_TO_BLACKLIST_BTN = PERFORMER_RETURN_FROM_BLACKLIST_BTN = By.XPATH, '//tbody/tr[1]/td[6]/div/div'

    PERFORMER_DETAILED_INFO_ID_INPUT = By.XPATH, '//form[@class="el-form"]/div[1]//input'
    PERFORMER_DETAILED_INFO_FIO_INPUT = By.XPATH, '//form[@class="el-form"]/div[2]//input'
    PERFORMER_DETAILED_INFO_BIRTHYEAR_INPUT = By.XPATH, '//form[@class="el-form"]/div[3]//input'
    PERFORMER_DETAILED_INFO_PASSPORT_INPUT = By.XPATH, '//form[@class="el-form"]/div[4]//input'
    PERFORMER_DETAILED_INFO_INN_INPUT = By.XPATH, '//form[@class="el-form"]/div[5]//input'
    PERFORMER_DETAILED_INFO_PHONE_INPUT = By.XPATH, '//form[@class="el-form"]/div[6]//input'
    PERFORMER_DETAILED_INFO_BANKCARD_INPUT = By.XPATH, '//form[@class="el-form"]/div[7]//input'
    PERFORMER_DETAILED_INFO_QR_LINK = By.XPATH, '//form[@class="el-form"]/div[8]//a'
    PERFORMER_DETAILED_INFO_STATUS_INPUT = By.XPATH, '//form[@class="el-form"]/div[9]//input'
    PERFORMER_DETAILED_INFO_SAVE_BTN = By.XPATH, '//form[@class="el-form"]/div[10]//button'

    PERFORMER_DETAILED_INFO = {'Performer ID input in detailed info': PERFORMER_DETAILED_INFO_ID_INPUT,
                               'Performer FIO input in detailed info': PERFORMER_DETAILED_INFO_FIO_INPUT,
                               'Performer birth year input in detailed info': PERFORMER_DETAILED_INFO_BIRTHYEAR_INPUT,
                               'Performer passport input in detailed info': PERFORMER_DETAILED_INFO_PASSPORT_INPUT,
                               'Performer INN input in detailed info': PERFORMER_DETAILED_INFO_INN_INPUT,
                               'Performer phone input in detailed info': PERFORMER_DETAILED_INFO_PHONE_INPUT,
                               'Performer bank card input in detailed info': PERFORMER_DETAILED_INFO_BANKCARD_INPUT,
                               'Performer QR code link in detailed info': PERFORMER_DETAILED_INFO_QR_LINK,
                               'Performer status input in detailed info': PERFORMER_DETAILED_INFO_STATUS_INPUT,
                               'Save performer button in detailed info': PERFORMER_DETAILED_INFO_SAVE_BTN}

    PERFORMER_BL_DETAILED_INFO_COMMENT_INPUT = By.XPATH, '//form[@class="el-form"]/div[10]//input'
    PERFORMER_BL_DETAILED_INFO_SAVE_BTN = By.XPATH, '//form[@class="el-form"]/div[11]//button'

    PERFORMER_BL_COMMENT_INPUT = By.CSS_SELECTOR, 'input.el-input__inner'
    PERFORMER_BL_CONFIRM_BTN = By.CSS_SELECTOR, '.el-message-box__btns button.btn-next'
    PERFORMER_BL_CANCEL_BTN = PERFORMER_UNBL_CANCEL_BTN = By.CSS_SELECTOR, '.el-message-box__btns ' \
                                                                           'button.el-button--default'

    PERFORMER_UNBL_CONFIRM_BTN = By.CSS_SELECTOR, '.el-message-box__btns button.prompt-primary-btn'

    PERFORMER_BL = {'Blacklist comment input': PERFORMER_BL_COMMENT_INPUT,
                    'Confirm blacklist button': PERFORMER_BL_CONFIRM_BTN,
                    'Cancel blacklist button': PERFORMER_BL_CANCEL_BTN}

    PERFORMER_UNBL = {'Confirm unblacklist button': PERFORMER_UNBL_CONFIRM_BTN,
                      'Cancel unblacklist button': PERFORMER_UNBL_CANCEL_BTN}


class ResponsiblePageLocators:
    ADD_RESPONSIBLE_BTN = By.XPATH, '//button[@class="el-button el-button--primary"]'

    RESPONSIBLE_FIO_INPUT = By.XPATH, '//form[@class="el-form"]/div[1]//input'
    RESPONSIBLE_EMAIL_INPUT = By.XPATH, '//form[@class="el-form"]/div[2]//input'
    RESPONSIBLE_PHONE_INPUT = By.XPATH, '//form[@class="el-form"]/div[3]//input'
    RESPONSIBLE_PASSWORD_INPUT = By.XPATH, '//form[@class="el-form"]/div[4]//input'
    RESPONSIBLE_OBJECTS_CHECKBOXES = By.XPATH, '//form[@class="el-form"]/div[5]//' \
                                               'span[contains(@class, "el-checkbox__input")]'
    RESPONSIBLE_SAVE_BTN = By.XPATH, '//form[@class="el-form"]/div[6]//button'

    RESPONSIBLE_CREATION = {'Responsible FIO input': RESPONSIBLE_FIO_INPUT,
                            'Responsible email input': RESPONSIBLE_EMAIL_INPUT,
                            'Responsible phone input': RESPONSIBLE_PHONE_INPUT,
                            'Responsible password input': RESPONSIBLE_PASSWORD_INPUT,
                            'Responsible objects checkboxes': RESPONSIBLE_OBJECTS_CHECKBOXES,
                            'Save responsible button': RESPONSIBLE_SAVE_BTN}

    RESPONSIBLE_INFO_FIO = By.XPATH, '//tbody/tr[1]/td[1]//span/span'
    RESPONSIBLE_INFO_EMAIL = By.XPATH, '//tbody/tr[1]/td[2]//span/span'
    RESPONSIBLE_INFO_PHONE = By.XPATH, '//tbody/tr[1]/td[3]//span/span'
    RESPONSIBLE_INFO_OBJECT = By.XPATH, '//tbody/tr[1]/td[4]//span/span//span[1]'
    RESPONSIBLE_INFO_SERVICES = By.XPATH, '//tbody/tr[1]/td[4]//span/span//span[3]'
    RESPONSIBLE_ADD_TO_ARCHIVE_BTN = RESPONSIBLE_RETURN_FROM_ARCHIVE_BTN = By.XPATH, '//tbody/tr[1]/td[5]/div/div'

    RESPONSIBLE_DETAILED_INFO_FIO_INPUT = By.XPATH, '//form[@class="el-form"]/div[1]//input'
    RESPONSIBLE_DETAILED_INFO_EMAIL_INPUT = By.XPATH, '//form[@class="el-form"]/div[2]//input'
    RESPONSIBLE_DETAILED_INFO_PHONE_INPUT = By.XPATH, '//form[@class="el-form"]/div[3]//input'
    RESPONSIBLE_DETAILED_INFO_OBJECTS_N_SERVICES_CHECKBOXES = By.XPATH, '//form[@class="el-form"]/div[4]//' \
                                                                        'span[contains(@class, "el-checkbox__input")]'
    RESPONSIBLE_DETAILED_INFO_SAVE_BTN = By.XPATH, '//form[@class="el-form"]/div[5]//button'
    RESPONSIBLE_DETAILED_INFO_CHANGEPASS_BTN = By.XPATH, '//button[contains(@class, "btn-change-pass")]'

    RESPONSIBLE_DETAILED_INFO = {'Responsible FIO input in detailed info': RESPONSIBLE_DETAILED_INFO_FIO_INPUT,
                                 'Responsible email input in detailed info': RESPONSIBLE_DETAILED_INFO_EMAIL_INPUT,
                                 'Responsible phone input in detailed info': RESPONSIBLE_DETAILED_INFO_PHONE_INPUT,
                                 'Responsible objects checkboxes in detailed info':
                                     RESPONSIBLE_DETAILED_INFO_OBJECTS_N_SERVICES_CHECKBOXES,
                                 'Save responsible button in detailed info': RESPONSIBLE_DETAILED_INFO_SAVE_BTN,
                                 'Change responsible password button in detailed info':
                                     RESPONSIBLE_DETAILED_INFO_CHANGEPASS_BTN}

    RESPONSIBLE_CHANGEPASS_NEWPASS_INPUT = By.XPATH, '//div[@class="el-overlay" and ' \
                                                     'not(contains(@style, "display: none;"))]' \
                                                     '//div[@class="el-dialog__body"]/div[2]/input'
    RESPONSIBLE_CHANGEPASS_CONFIRMPASS_INPUT = By.XPATH, '//div[@class="el-overlay" and ' \
                                                         'not(contains(@style, "display: none;"))]' \
                                                         '//div[@class="el-dialog__body"]/div[4]/input'
    RESPONSIBLE_CHANGEPASS_CONFIRM_BTN = By.XPATH, '//div[@class="el-overlay" and ' \
                                                   'not(contains(@style, "display: none;"))]' \
                                                   '//div[contains(@class, "el-dialog__footer")]' \
                                                   '//button[contains(@class, "el-button--primary")]'
    RESPONSIBLE_CHANGEPASS_CANCEL_BTN = By.XPATH, '//div[@class="el-overlay" and ' \
                                                  'not(contains(@style, "display: none;"))]' \
                                                  '//div[contains(@class, "el-dialog__footer")]' \
                                                  '//button[contains(@class, "el-button--default")]'

    RESPONSIBLE_CHANGEPASS = {'New password input': RESPONSIBLE_CHANGEPASS_NEWPASS_INPUT,
                              'Confirm password input': RESPONSIBLE_CHANGEPASS_CONFIRMPASS_INPUT,
                              'Confirm change password button': RESPONSIBLE_CHANGEPASS_CONFIRM_BTN,
                              'Cancel change password button': RESPONSIBLE_CHANGEPASS_CANCEL_BTN}

    RESPONSIBLE_AR_CONFIRM_BTN = RESPONSIBLE_UNAR_CONFIRM_BTN = By.CSS_SELECTOR, '.el-message-box__btns ' \
                                                                                 'button.prompt-primary-btn'
    RESPONSIBLE_AR_CANCEL_BTN = RESPONSIBLE_UNAR_CANCEL_BTN = By.CSS_SELECTOR, '.el-message-box__btns ' \
                                                                               'button.el-button--default'

    RESPONSIBLE_AR = {'Confirm archive button': RESPONSIBLE_AR_CONFIRM_BTN,
                      'Cancel archive button': RESPONSIBLE_AR_CANCEL_BTN}

    RESPONSIBLE_UNAR = {'Confirm unarchive button': RESPONSIBLE_UNAR_CONFIRM_BTN,
                        'Cancel unarchive button': RESPONSIBLE_UNAR_CANCEL_BTN}
