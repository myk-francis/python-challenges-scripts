
import jobs.constants as const 

class Jobs:
    def __init__(self, driver):
        self.driver = driver

    def __exit__(self):
        self.driver.quit()

    def landing_page(self):
        self.driver.get(const.BASE_URL)