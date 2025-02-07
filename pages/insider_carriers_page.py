from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class InsiderCarriersPage(BasePage):
    OUR_LOCATION=(By.XPATH, '//*[@id="career-our-location"]/div/div/div')
    TEAM=(By.XPATH, '//*[@id="career-find-our-calling"]')
    LIFE_AT_INSIDER=(By.CSS_SELECTOR, 'body > div.elementor.elementor-22610 > section.elementor-section.elementor-top-section.elementor-element.elementor-element-a8e7b90.elementor-section-full_width.elementor-section-height-default.elementor-section-height-default')
    OPEN_POSITION=(By.XPATH, '//*[@id="page-head"]/div/div/div[1]/div/div/a')

    def __init__(self, driver):
        super().__init__(driver)

    # Returns True if the element is present, False if it is not
    def team_blog_element(self) -> bool:
        return self.is_element_exist(*self.TEAM)

    # Returns True if the element is present, False if it is not
    def check_blog_element(self) -> bool:
        return self.is_element_exist(*self.OUR_LOCATION)

    # Returns True if the element is present, False if it is not
    def check_life_at_insider_blog_element(self) -> bool:
        return self.is_element_exist(*self.LIFE_AT_INSIDER)

    # Move to open position page with button with specific job
    def move_to_open_position_page_with_button_with_specific_job(self):
        self.find_element(*self.OPEN_POSITION).click()