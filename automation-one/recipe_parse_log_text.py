from delorean import Delorean
from delorean import parse
from decimal import Decimal

d = Delorean()

log = '[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.99'

divide_it = log.split(' - ')

timestamp_string, _, product_string, price_string = divide_it

time_stamp = parse(timestamp_string.strip('[]'))

product_id = int(product_string.split(':')[-1])

price = Decimal(price_string.split('$')[-1])

print(time_stamp, product_id, price)