# author        :   ignorantshr
# create_date   :   2020/04/22 22:04
# description   :   使用 clock_deco.py 中的装饰器

from clock_deco import clock


# N 的阶乘
@clock
def factorial(n):
    assert n >= 1
    return 1 if n == 1 else n * factorial(n - 1)

if __name__ == '__main__':
    print("6! = %d" % factorial(6))
