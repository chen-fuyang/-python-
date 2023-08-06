from functools import wraps


def test1(func):#定义一个额外功能
    @wraps(func)#使用function来包装test2
    def test2():
        print("帮你把饭做好")
        func()
        print("洗碗")
    return test2
@test1 #装饰器
def eat():
    print("我正在吃饭")

# eat = test1(eat)

eat()

print(eat.__name__)
#eat函数变成test2了

