from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://portal.ajira.go.tz/advert/index/13")

driver.quit()