import time
from typing import List
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Open to URL
    def open(self,url):
        self.driver.get(url)

    # Move to the element
    def find_element(self,by,element) -> WebElement:
        try:
            return self.driver.find_element(by, element)
        except NoSuchElementException:
            print("Element not found")
        except Exception as e:
            print(e)
        # Find the element and return, if not found, print error

    def move_to_element(self,element):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
        except NoSuchElementException:
            print("Element not found")
        except Exception as e:
            print(e)

    # Find the element in the parent element and return, if not found, print error
    @staticmethod
    def find_element_in_element(parent:WebElement,by,element) -> WebElement:
        try:
            return parent.find_element(by,element)
        except NoSuchElementException:
            print("Element not found")
        except Exception as e:
            print(e)

    # Find elements and return, if not found, print error
    def find_elements(self,by,element) -> List[WebElement]:
        try:
            return self.driver.find_elements(by, element)
        except NoSuchElementException:
            print("Element not found")
        except Exception as e:
            print(e)


    # Wait for the element to be found, if not in 10 seconds, print error
    def wait_for_element(self,by,element,timeout=10):
        try:
            return WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located((by,element)))
        except NoSuchElementException:
            print("Element not found")
        except TimeoutException:
            print("Timeout")
        except Exception as e:
            print(e)

    # Click to the element
    def click_element(self,element):
        try:
            button_element = self.find_element(*element)
            button_element.click()
        except NoSuchElementException:
            print("Element not found")
            return False
        except Exception as e:
            print(e)
            return False,

    # Check if the element exists
    def is_element_exist(self, element, by) -> bool:
        try:
            self.find_element(by, element)  # Elementi bulmaya çalış
            return True  # Bulundu
        except NoSuchElementException:
            return False  # Bulunamadı
        except Exception as e:
            print(e)
            return False

    # Click to the cookie button
    def click_cookie_button(self):
        try:
            cookie_button = self.driver.find_element(By.XPATH, '//*[@id="wt-cli-accept-all-btn"]')
            cookie_button.click()
            time.sleep(1)
            print("Cookie Button Clicked")
        except NoSuchElementException:
            pass
