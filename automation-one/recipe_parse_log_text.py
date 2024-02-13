from delorean import Delorean
from decimal import Decimal

d = Delorean()

log = '[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.99'

devide_it = log.split('-')
print(devide_it)

