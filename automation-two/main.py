
from jobs.jobs import Jobs

with Jobs() as bot:
    bot.landing_page()
    titles = bot.get_titles()
    dates = bot.get_closing_dates()
    print(f'There are {len(titles)} jobs:')
    for title, date in zip(titles, dates):
        print(f'{title} - {date}')
    print('Done!')