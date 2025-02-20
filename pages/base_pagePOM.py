from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


class Page:
    BACK_BUTTON = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    SAVED_TAB = (AppiumBy.ID, "org.wikipedia:id/nav_tab_reading_lists")
    MORE_TAB = (AppiumBy.ID, "org.wikipedia:id/nav_more_container")
    READING_SYNC_NO_THANKS = (AppiumBy.ID, "android:id/button2")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)

    def tap(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def save_screenshot(self, name):
        self.driver.save_screenshot(f'{name}.png')

    def wait_for_element_tap(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        ).click()

    def wait_for_element_appear(self, *locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator),
            message=f'Element by {locator} not appear'
        )
        return element

    def wait_for_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by {locator} is still visible'
        )

    def wait_for_element_visible(self, *locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} not visible'
        )
        return element

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f"Expected text '{expected_text}' not in actual '{actual_text}'"

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, \
            f"Expected text '{expected_text}' did not match actual '{actual_text}'"

    def go_back(self):
        self.tap(*self.BACK_BUTTON)


    def open_saved_tab(self):
        self.tap(*self.SAVED_TAB)


    def open_more_tab(self):
        self.tap(*self.MORE_TAB)


    def warn_reading_list_sync_no(self):
        self.tap(*self.READING_SYNC_NO_THANKS)