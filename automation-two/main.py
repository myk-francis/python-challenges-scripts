
from jobs.jobs import Jobs
import pywhatkit
from selenium import webdriver
import time

with Jobs() as bot:
    final_text = ""
    bot.landing_page()
    titles = bot.get_titles()
    dates = bot.get_closing_dates()
    print(f'There are {len(titles)} jobs:')
    for title, date in zip(titles, dates):
        final_text += f'{title} - {date}\n'

    print(final_text)

    bot.switch_tab()

    time.sleep(10)

    bot.go_to_whatsapp(final_text)

    time.sleep(120)

    bot.send_text()

    time.sleep(3)

    # pywhatkit.sendwhatmsg("+255710503304", final_text, 0, 4, True, 2)
    
    print('Done!')