from selenium import webdriver
from selenium.webdriver.common.by import By
import jobs.constants as const 

class Jobs(webdriver.Chrome):
    def __init__(self):
        super(Jobs, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()

    def landing_page(self):
        self.get(const.BASE_URL)

    def get_titles(self):
        titles = self.find_elements(By.CSS_SELECTOR, "a[class='advert-title']")
        print ([title.text for title in titles])

    def get_closing_dates(self):
        dates = self.find_elements(By.CSS_SELECTOR, "td[class='text-right']")
        print ([date.text for date in dates])