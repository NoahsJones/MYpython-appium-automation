from appium.webdriver.common.appiumby import AppiumBy

from pages.base_pagePOM import Page


class OnboardingPage(Page):
    SKIP_BTN = (AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')

    def click_skip_ob(self):
        self.tap(*self.SKIP_BTN)
