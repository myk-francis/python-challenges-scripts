from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import jobs.constants as const 
import re
import time

whatsappurl = "https://web.whatsapp.com/send?phone=255710503304/&text="

class Jobs(webdriver.Chrome):
    def __init__(self):
        super(Jobs, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()

    def landing_page(self):
        self.get(const.HR_BASE_URL)

    def get_titles(self):
        titles = self.find_elements(By.CSS_SELECTOR, "a[class='advert-title']")
        return [title.text for title in titles]

    def get_closing_dates(self):
        dates = self.find_elements(By.CSS_SELECTOR, "td[class='text-right']")
        return [re.search(r'\d{4}-\d{2}-\d{2}', date.text).group() for date in dates]
    
    def go_to_whatsapp(self, text):
        self.get(const.WHATSAPP_BASE_URL + text)

    def switch_tab(self):
        self.switch_to.new_window('tab')

    def send_text(self):
        # content = self.switch_to.active_element
        # content.send_keys(text)
        # time.sleep(10)
        # content.send_keys(Keys.RETURN)
        send_btn = self.find_elements(By.CSS_SELECTOR, "button[aria-label='Send']")
        send_btn.click()
