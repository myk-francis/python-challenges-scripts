from selenium import webdriver
import gov_jobs.constants as const 

class Jobs:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.quit()

    def __exit__(self):
        self.driver.quit()

    def landing_page(self):
        self.driver.get(const.BASE_URL)