from selenium import webdriver
from selenium.webdriver.common.by import By
import jobs.constants as const 
import re

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
        return [title.text for title in titles]

    def get_closing_dates(self):
        dates = self.find_elements(By.CSS_SELECTOR, "td[class='text-right']")
        return [re.search(r'\d{4}-\d{2}-\d{2}', date.text).group() for date in dates]