from selenium import webdriver
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