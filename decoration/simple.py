# author        :   ignorantshr
# create_date   :   2020/04/22 20:05
# description   :   简单装饰器

def decor(func):
    print('in decoration executing %s' % func)
    return func

"""
以下两种写法是一样的，所以装饰器只是语法糖而已。通常它把函数给替换成另一个函数。
"""

# 第一种写法
def f1():
    print('executing f1')

target = decor(f1)
# print(target) # target 就是 decor 返回的函数对象
target()

# 第二种写法
@decor
def f1():
    print('executing f1')

f1()
