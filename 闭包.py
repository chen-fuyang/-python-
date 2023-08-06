def func_a(number_a):#高阶函数，返回一个函数

    def func_b(number_b):
        print("内嵌函数func_b的参数是:%s,外部函数func_a的参数是:%s"%(number_b,number_a))
        return number_b+number_a

    return func_b

result = func_a(10)
#print(result(10))
#print(result(90))

#func_b就是闭包


#闭包的应用

def creat_line(a,b):

    def line(x):
        return a*x +b

    return line

# 得到一个一元线性函数
l1 = creat_line(2,2)
l2 = creat_line(1.5,-2)

#计算线一函数中，当x=5时对应的y
y = l1(5)
#print(y)


#闭包里面修改外部变量的值
def test1():
    #count其实不是局部变量，介于全局变量和局部变量之间的一种变量,nonLocal标识
    count = 1
    def add():
        nonlocal count
        print(count)
        count+=1
        return count
    return add

#print(test1()())


#4、闭包的陷阱

def test3():
    func_list = []
    for i in range(1,4):

        def test4(_i = i):
            return _i**2
        func_list.append(test4)

    return func_list

f1,f2,f3 =test3()
print(f1(),f2(),f3())



