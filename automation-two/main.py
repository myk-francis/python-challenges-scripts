
from jobs.jobs import Jobs

with Jobs() as bot:
    bot.landing_page()
    print('Done!')