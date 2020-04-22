# author        :   ignorantshr
# create_date   :   2020/04/22 20:54
# description   :   变量作用域规则

from dis import dis

global_var = 1

def f1(num):
    print(num)
    print(global_var)

# 这里python会把global_var当作局部变量
def f2(num):
    print(num)
    print(global_var)
    global_var = 2

if __name__ == '__main__':
    # f1(2)
    # print('===================')
    # f2(4)

    # 反汇编
    dis(f1)
    print('===================')
    dis(f2)

    """
    LOAD_FAST 载入局部变量
    LOAD_GLOBAL 载入全局变量
    """
