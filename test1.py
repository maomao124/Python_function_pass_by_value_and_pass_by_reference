"""
 * Project name(项目名称)：Python函数值传递和引用传递
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 19:43
 * Version(版本): 1.0
 * Description(描述)：
 形式参数：在定义函数时，函数名后面括号中的参数就是形式参数
 实际参数：在调用函数时，函数名后面括号中的参数称为实际参数，也就是函数的调用者给函数的参数
 根据实际参数的类型不同，函数参数的传递方式可分为 2 种，分别为值传递和引用（地址）传递：
值传递：适用于实参类型为不可变类型（字符串、数字、元组）；
引用（地址）传递：适用于实参类型为可变类型（列表，字典）；
值传递和引用传递的区别是，函数参数进行值传递后，若形参的值发生改变，不会影响实参的值；而函数参数继续引用传递后，改变形参的值，实参的值也会一同改变。
 """


def f(obj):
    obj += obj
    print("形参值为：", obj)


if __name__ == '__main__':
    print("-------值传递-----")
    a = "hello"
    print("a的值为：", a)
    f(a)
    print("实参值为：", a)
    a = 123
    print("a的值为：", a)
    f(a)
    print("实参值为：", a)
    a = (1, 2)
    print("a的值为：", a)
    f(a)
    print("实参值为：", a)
    print("-----引用传递-----")
    a = [1, 2, 3]
    print("a的值为：", a)
    f(a)
    print("实参值为：", a)
