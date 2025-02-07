import random
import time
from selenium.webdriver.common.by import By
from pages.insider_open_position_page import InsiderOpenPositionPage
link = "https://useinsider.com/careers/open-positions/?department=qualityassurance" # Link of the page
time_out = 10 # 10 seconds for timed outs

'''
I'm not sure is right thing call a test function from another test function but I did it.
When i check another case i need to check the previous case.
For example, I test to location filter works correctly but users if don't any response from backend in 10 seconds,
It will be a problem. So, I need to check the response time for location filter.
On the other hand if i didn't do that, Test is failed because of the response time and I need to always repeat the test.
It is not a good way and take my time. So, I call the response time test function from location filter test function.
'''

# Check if the page is opened
def test_is_page_opened(driver):
    expected_link = "https://useinsider.com/careers/open-positions/?department=qualityassurance"
    insider_open_position = InsiderOpenPositionPage(driver)
    insider_open_position.open(link)
    assert driver.current_url == expected_link, f"Error: {driver.current_url} is not equal to {expected_link}"


# Check to response time for department filter
'''
I noticed to to response time is always random. Sometimes it is too long, sometimes it is normal.
I will check the response time for department filter and location filter.
If the response time is too long, I will print an error message.
'''
def test_filter_by_department_response_time(driver):
    insider_open_position = InsiderOpenPositionPage(driver)
    insider_open_position.open(link)
    department_filter = insider_open_position.filter_by_department()
    department_filter.click()
    department_list = insider_open_position.filter_by_department_list()
    start_time = time.time()

    while len(department_list) <= 1:
        department_filter.click()
        department_filter.click()
        department_list = insider_open_position.filter_by_department_list()
        if time.time() - start_time > time_out:
            assert False, f"Response time is too long: {time.time() - start_time} seconds"
        time.sleep(1)
    assert True, "Response time is normal"


# Check to response time for location filter
'''
I noticed to to response time is always random. Sometimes it is too long, sometimes it is normal.
I will check the response time for location filter and location filter.
If the response time is too long, I will print an error message.
'''
def test_filter_by_location_response_time(driver):
    insider_open_position = InsiderOpenPositionPage(driver)
    insider_open_position.open(link)
    location_filter = insider_open_position.filter_by_location()
    location_filter.click()
    location_list = insider_open_position.filter_by_department_list()
    start_time = time.time()
    while len(location_list) <= 1:
        location_filter.click()
        location_filter.click()
        location_list = insider_open_position.filter_by_location_list()
        if time.time() - start_time > time_out:
            assert False, f"Response time is too long: {time.time() - start_time} seconds"
        time.sleep(1)
    assert True, "Response time is normal"


# Check to location filter works correctly
def test_filter_by_location_turkiye(driver):
    test_filter_by_location_response_time(driver)
    insider_open_position = InsiderOpenPositionPage(driver)
    location_filter = insider_open_position.filter_by_location()
    if not location_filter.is_displayed():
        location_filter.click()
    insider_open_position.filter_by_location_list_istanbul_turkiye().click()
    location_filter = insider_open_position.filter_by_location()
    assert location_filter.get_attribute(
        "title") == "Istanbul, Turkiye", f"Error: {location_filter.get_attribute('title')} is not equal to Istanbul, Turkiye"

# Check to right jobs filtered by department and location
def test_check_position_filtered_by_department_and_location(driver):
    test_filter_by_location_turkiye(driver)
    insider_open_position = InsiderOpenPositionPage(driver)
    time.sleep(5)
    jobs = insider_open_position.filter_by_department_list_open_positions()
    for job in jobs:
        card_element = insider_open_position.job_card_element(job)
        department_element = card_element["department"]
        location_element = card_element["location"]
        title_element = card_element["title"]
        assert department_element.text == "Quality Assurance", f"Error: {department_element.text} is not equal to Quality Assurance"
        assert location_element.text == "Istanbul, Turkiye", f"Error: {location_element.text} is not equal to Istanbul, Turkiye"
        assert "Quality Assurance" in title_element.text or "QA" in title_element.text, f"Error: {title_element.text} is not equal to Quality Assurance or QA"

# Check to view role button works correctly
def test_check_view_role_button(driver):
    test_check_position_filtered_by_department_and_location(driver)
    insider_open_position = InsiderOpenPositionPage(driver)
    insider_open_position.click_cookie_button()
    jobs = insider_open_position.filter_by_department_list_open_positions()
    print(*range(len(jobs)))
    choice = random.choice([*range(len(jobs))])
    choice_job = jobs[choice]
    insider_open_position.move_to_element(choice_job)
    view_role = choice_job.find_element(By.LINK_TEXT, 'View Role')
    job_link = view_role.get_attribute("href")
    view_role.click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == job_link, f"Error: {current_url} is not equal to {job_link}"
    time.sleep(2)