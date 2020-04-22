# author        :   ignorantshr
# create_date   :   2020/04/22 21:13
# description   :   闭包举例
"""
闭包是一种函数，它会保留定义函数时存在的自由变量绑定。
这样在调用函数时，虽然定义作用域不可用了，但仍然能使用那些绑定

注意：只有嵌套在其他函数中的函数才可能处理不在全局作用域中的外部变量
"""


"""
avg 实现了累计平均的效果
"""

# 第一种方法
class Average:
    def __init__(self):
        self._nums = []

    def __call__(self, value):
        assert type(value) == int
        self._nums.append(value)
        total = sum(self._nums)
        return total / len(self._nums)


# 第二种方法
"""
在average中，nums 是自由变量，指在本地作用域绑定的变量
"""
def make_average():
    nums = []

    def average(n):
        nums.append(n)
        total = sum(nums)
        return total / len(nums)

    return average


if __name__ == '__main__':
    avg1 = Average()
    avg2 = make_average()

    print(avg1(1))
    print(avg1(2))
    print(avg1(3))

    print("===========")

    print(avg2(1))
    print(avg2(2))
    print(avg2(3))
    print(avg2.__closure__) # 闭包
    print(avg2.__closure__[0].cell_contents) # 闭包中存储的值
    print(avg2.__code__.co_varnames)    # 局部变量
    print(avg2.__code__.co_freevars)    # 自由变量
