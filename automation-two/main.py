from selenium import webdriver
from jobs.jobs import Jobs

browser = webdriver.Chrome()

with Jobs(driver=browser) as bot:
    bot.landing_page()
    print('Done!')