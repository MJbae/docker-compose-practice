from time import sleep

from core.tasks import say_hello, add, mul, xsum

say_hello()
result = add(1, 10)
print(f'result of adding: {result}')
result_mul = mul(result, result)
print(f'result_mul: {result_mul}')
result_xsum = xsum([result_mul, result])
print(f'result_xsum: {result_xsum}')

