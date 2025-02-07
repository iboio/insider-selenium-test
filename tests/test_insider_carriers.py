import time

from Tools.scripts.make_ctype import flags

from pages.insider_carriers_page import InsiderCarriersPage
from urllib.parse import urlparse, parse_qs
time_out = 10

# This test checks Team, Location and Life at Insider blogs are exist on the page
def test_blog_existing(driver):
    link = "https://useinsider.com/careers/"
    insider_carriers = InsiderCarriersPage(driver)
    insider_carriers.open(link)
    team = insider_carriers.team_blog_element()
    location = insider_carriers.check_blog_element()
    life = insider_carriers.check_life_at_insider_blog_element()
    assert team == True, "Team blog is not exist"
    assert location == True, "Location blog is not exist"
    assert life == True, "Life at Insider blog is not exist"


# This test checks when click to button, Checks that the page is correct for the open position page
# This function maybe can run with for loop. But I didn't use it because of the time.
'''
I checked to team blog in carriers page, when i click random open position job, page redirect to page who mentioned job and a button
for redirect position page. This button XPATH always same but the job name is different. So I think we can use for loop for this test.
For check "is page is correct for the open position page" I notice to "job name" in the URL with query. 
So I think we can check to page job name in the URL query.
'''

def test_open_position_page_for_qa(driver):
    link = "https://useinsider.com/careers/quality-assurance/"
    job = "qualityassurance"
    insider_carriers = InsiderCarriersPage(driver)
    insider_carriers.open(link)
    insider_carriers.move_to_open_position_page_with_button_with_specific_job()
    current_url = driver.current_url
    parsed_url = urlparse(current_url)
    parsed_query = parse_qs(parsed_url.query)
    assert parsed_query["department"] == [job], "Job is not correct"
    assert current_url == "https://useinsider.com/careers/open-positions/?department=qualityassurance", "URL is not correct"
