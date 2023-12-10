from appium.webdriver.common.appiumby import AppiumBy

from pages.base_pagePOM import Page


class SavedPage(Page):
    LOGIN_JOIN_WIKI = (AppiumBy.ID, "org.wikipedia:id/positiveButton")
    LOG_IN_PAGE = (AppiumBy.ID, "org.wikipedia:id/create_account_login_button")
    USERNAME_FIELD = (AppiumBy.XPATH, "//android.widget.EditText[@text='Username']")
    PASSWORD_FIELD = (AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")
    REPEAT_PASSWORD_FIELD = (AppiumBy.XPATH, "//android.widget.EditText[@text='Repeat password']")
    EMAIL_FIELD = (AppiumBy.XPATH, "//android.widget.EditText[@text='Email (Optional)']")
    LOGIN_BUTTON = (AppiumBy.ID, "org.wikipedia:id/login_button")
    PROFILE_NAME_BUTTON = (AppiumBy.ID, "org.wikipedia:id/main_drawer_account_name")


    def log_in_or_join_wiki(self):
        self.tap(*self.LOGIN_JOIN_WIKI)


    def open_login(self):
        self.tap(*self.LOG_IN_PAGE)


    def log_in(self, username, password):
        self.input(username, *self.USERNAME_FIELD)
        self.input(password, *self.PASSWORD_FIELD)
        self.tap(*self.LOGIN_BUTTON)


    def verify_logged_in(self, username):
        self.verify_text(username, *self.PROFILE_NAME_BUTTON)






