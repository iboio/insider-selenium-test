from pages.insider_home import InsiderHomePage


# This test checks the page is opened
def test_is_page_opened(driver):
    expected_title = "#1 Leader in Individualized, Cross-Channel CX — Insider"
    expected_link = "https://useinsider.com/"
    insider_home = InsiderHomePage(driver)
    insider_home.open("https://useinsider.com/")
    driver.get("https://useinsider.com/")
    assert driver.title == expected_title and driver.current_url == expected_link

# This page checks the page is opened and checks the page is correct for the open carriers page
def test_open_carriers_page(driver):
    expected_link = "https://useinsider.com/careers/"
    insider_home = InsiderHomePage(driver)
    insider_home.open("https://useinsider.com/")
    insider_home.company_head_bar().click()
    insider_home.company_head_bar_careers().click()
    assert driver.current_url == expected_link, "URL is not correct"