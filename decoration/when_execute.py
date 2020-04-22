# author        :   ignorantshr
# create_date   :   2020/04/22 20:35
# description   :   装饰器执行时机

"""
装饰器的一个关键特性是，它在被装饰的函数定义之后立即运行。
这通常是在 导入时（即python加载模块时）发生。
"""

registry = []

def decor(func):
    print('in decoration executing %s' % func)
    registry.append(func)
    return func

print('step one')

@decor
def f1():
    print('executing f1')

print('step two')

def f2():
    print('executing f2')

if __name__ == '__main__':
    print('exec main')
    print('registry = %s' % registry)
    f1()
    f2()
