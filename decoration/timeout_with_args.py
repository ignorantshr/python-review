# author        :   ignorantshr
# create_date   :   2020/04/23 8:51 AM
# description   :   超时装饰器

import functools
import threading
import time


def timeout(seconds=0):
    assert type(seconds) == int

    def decorator(func):
        re = None

        def timer():
            count = seconds
            while count > 0:
                time.sleep(1)
                count -= 1

        def run(*args, **kwargs):
            nonlocal re
            re = func(*args, **kwargs)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timer_thread = threading.Thread(target=timer)
            # quit with main thread
            timer_thread.setDaemon(True)
            timer_thread.start()

            run_thread = threading.Thread(target=run, args=args, kwargs=kwargs)
            # quit with main thread
            run_thread.setDaemon(True)
            run_thread.start()

            while True:
                if run_thread.is_alive():
                    # still running
                    if timer_thread.is_alive():
                        time.sleep(1)   # Query once per second
                        continue
                    else:
                        # run func timeout
                        return None
                # run func done
                else:
                    return re
        return wrapper
    return decorator


@timeout(5)
def f1():
    print('running f1')


def f2():
    print('running f2')


if __name__ == '__main__':
    """
    这两种方式是一样的
    """
    f1()
    print('================')
    deco = timeout(5)
    wrapper_ = deco(f2)
    wrapper_()
