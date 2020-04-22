# author        :   ignorantshr
# create_date   :   2020/04/22 21:55
# description   :   计时装饰器
from time import time
import functools

# func 是自由变量
def clock(func):
    @functools.wraps(func)  # 把func的属性复制到wrapper中
    def wrapper(*args, **kwargs):
        start_time = time()
        re = func(*args, **kwargs)
        elapsed = time() - start_time

        arg_list = []
        if args:
            arg_list.append(*args)
        if kwargs:
            arg_list.append(**kwargs)
        print('[%.8fs] %s(%s)' % (elapsed, func.__name__, arg_list))
        return re

    return wrapper

