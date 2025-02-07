from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage


class InsiderHomePage(BasePage):
    COMPANY = (By.XPATH, '//*[@id="navbarNavDropdown"]')
    COMPANY_CAREERS = (By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[6]/div/div[2]/a[2]')
    def __init__(self, driver):
        super().__init__(driver)

    # Returns the company element in the head bar
    def company_head_bar(self)-> WebElement:
        #head bardaki company elementini bulur
        return self.find_element(*self.COMPANY)

    # Returns the careers element in the company head bar element
    def company_head_bar_careers(self) -> WebElement:
        #company elementinin içindeki careers elementini bulur
        return self.find_element(*self.COMPANY_CAREERS)

