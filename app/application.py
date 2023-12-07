from pages.base_pagePOM import Page
from pages.explore_pagePOM import ExplorePage
from pages.onboarding_pagePOM import OnboardingPage
from pages.search_pagePOM import SearchPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.explore_page = ExplorePage(driver)
        self.ob_page = OnboardingPage(driver)
        self.search_page = SearchPage(driver)
