
import time
from functools import wraps


def logger(func):
    @wraps(func)
    def write_logging():
        print("[info]--时间是: %s"%time.strftime('%H:%M:%S',time.localtime()))
        func
    return write_logging

@logger  #使用装饰器来给所有工作增加记录日志的功能
def work():
    print("我在工作")

work()

