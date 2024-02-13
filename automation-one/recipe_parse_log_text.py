from delorean import Delorean
from delorean import parse
from decimal import Decimal

d = Delorean()

log = '[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.99'

divide_it = log.split('-')

print(divide_it)

timestamp_string = divide_it[0]
product_id = divide_it[2]
price = divide_it[3]

# timestamp_string, _, product_string, price_string = divide_it
print(timestamp_string, product_id, price)

