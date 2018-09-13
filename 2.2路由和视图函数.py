#使用修饰器声明路由#
@app.route('/')
def index():
    return '<h1>HELLO WORLD</h1>'
#修饰器是Python语言的标准特性，可以使用不同的方式修改函数的行为。惯常用法是使用修饰器把函数注册为事件的处理程序#
#这里将index()函数注册成程序根地址处理的程序。这个函数的返回值称为响应，即客户端接收到的内容。#

#动态名字#
@app.route('/user/<name>')
def user(name):
    return'<h1>hello,%s!</h1>'%name
#尖括号中为动态内容，任何能匹配静态部分的URL都会映射到这个路由上#
#调用视图函数时flask会将动态部分传入函数#
#路由中的动态部分默认使用字符串#

@app.route('/user/<int:id>')#这条路由中，只会匹配动态片段id为整数的URL#
#Flask支持在路由中使用int、float、path类型#
#path类型也是字符串，但不把斜杠视作分隔符，而将其当做动态片段的一部分#
