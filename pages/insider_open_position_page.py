from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from typing import Dict


class InsiderOpenPositionPage(BasePage):
    FILTER_BY_LOCATION = (By.XPATH, '//*[@id="select2-filter-by-location-container"]')
    FILTER_BY_DEPARTMENT = (By.XPATH, '//*[@id="select2-filter-by-department-container"]')
    FILTER_BY_LOCATION_LIST = (By.XPATH, '//*[@id="select2-filter-by-location-results"]/li')
    FILTER_BY_DEPARTMENT_LIST = (By.XPATH, '//*[@id="select2-filter-by-department-results"]/li')
    FILTER_BY_JOB_LIST_OPEN_POSITIONS = (By.XPATH, '//*[@id="jobs-list"]/div')
    FILTER_BY_LOCATION_LIST_ISTANBUL_TURKIYE = (By.XPATH, '/html/body/span/span/span[2]/ul/li[2]')
    JOB_CARD_DEPARTMENT = (By.XPATH, '//*[@class = "position-department text-large font-weight-600 text-primary"]')
    JOB_CARD_LOCATION = (By.XPATH, '//*[@class = "position-location text-large"]')
    JOB_CARD_TITLE = (By.TAG_NAME, "p")

    # FILTER_BY_LOCATION_LIST_ISTANBUL_TURKIYE = (By.XPATH, '//*[@id="select2-filter-by-location-result-isbg-Istanbul,Turkiye"]') Don't work
    # FILTER_BY_LOCATION_LIST_ISTANBUL_TURKIYE = (By.XPATH, 'li[id="select2-filter-by-location-result-q03z-Istanbul, Turkiye"]') Don't work
    def __init__(self, driver):
        super().__init__(driver)

    # Return a element for location filter span
    def filter_by_location(self) -> WebElement:
        return self.find_element(*self.FILTER_BY_LOCATION)

    # Return a list of element for location filter span
    def filter_by_location_list(self) -> List[WebElement]:
        return self.find_elements(*self.FILTER_BY_LOCATION_LIST)

    # Return a element for location filter span
    def filter_by_location_list_istanbul_turkiye(self) -> WebElement:
        return self.find_element(*self.FILTER_BY_LOCATION_LIST_ISTANBUL_TURKIYE)

    # Return a list of element for department filter span
    def filter_by_department(self) -> WebElement:
        return self.find_element(*self.FILTER_BY_DEPARTMENT)

    # Return a list of elements for a open positions for a department
    def filter_by_department_list_open_positions(self) -> List[WebElement]:
        return self.find_elements(*self.FILTER_BY_JOB_LIST_OPEN_POSITIONS)

    # Return a list of elements for a department
    def filter_by_department_list(self) -> List[WebElement]:
        return self.find_elements(*self.FILTER_BY_DEPARTMENT_LIST)

    # Return a dictionary of elements for a job card
    def job_card_element(self, parent: WebElement) -> Dict[str, WebElement]:
        return {
            "department": self.find_element_in_element(parent, *self.JOB_CARD_DEPARTMENT),
            "location": self.find_element_in_element(parent, *self.JOB_CARD_LOCATION),
            "title": self.find_element_in_element(parent, *self.JOB_CARD_TITLE)
        }

    # def get_department_element(self, parent: WebElement) -> WebElement:
    #     return self.find_element_in_element(parent, *self.JOB_CARD_DEPARTMENT)
    #
    # def get_location_element(self, parent: WebElement) -> WebElement:
    #     return self.find_element_in_element(parent, *self.JOB_CARD_LOCATION)
    #
    # def get_title_element(self, parent: WebElement) -> WebElement:
    #     return self.find_element_in_element(parent, *self.JOB_CARD_TITLE)
