# author        :   ignorantshr
# create_date   :   2020/04/22 21:36
# description   :   声明自由变量
"""
nonlocal 将不可变类型的变量声明为自由变量
"""


def make_average1():
    nums = []

    def average(n):
        """
        并没有给可变变量赋值，利用了列表可变的特性
        """
        nums.append(n)
        total = sum(nums)
        return total / len(nums)

    return average

def make_average2():
    count = 0
    total = 0

    def average(n):
        """
        但是对于不可变的类型，只能读取，不能更新
        如果尝试重新绑定，例如 count = count + 1
        会隐式地创建局部变量 count。这样 count 就不是自由变量了，因此就不会保留在闭包中
        """
        count += 1
        total += n
        return total / count

    return average

def make_average3():
    count = 0
    total = 0

    def average(n):
        """
        nonlocal 把变量标记为自由变量
        """
        nonlocal count, total
        count += 1
        total += n
        return total / count

    return average
