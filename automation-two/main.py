
from jobs.jobs import Jobs

with Jobs() as bot:
    bot.landing_page()
    bot.get_titles()
    bot.get_closing_dates()
    print('Done!')