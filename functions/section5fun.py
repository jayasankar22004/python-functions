def power(base,exponent=2):
    return base^exponent
def connect(host,port=3306,protocol='TCP'):
    return f'host:{host},\nport{port},\nprotocol{protocol}'
def discount_price(price,discount=10):
    return (price/100)*10
print(power(5))
print(connect('jaya sankar'))
print(discount_price(1500))
'''def func(name='guest',age):'''

