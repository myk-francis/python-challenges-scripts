from parse import *

LOG = '[2018-05-06T12:58:00.714611] - SALE - PRODUCT: 1345 - PRICE: $09.99'

FORMAT = '[{date}] - SALE - PRODUCT: {product} - PRICE:${price}'

result = parse(FORMAT, LOG)

print(result)