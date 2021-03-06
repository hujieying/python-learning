## 重要知识点
### 入门

* 如果看到关于ASCII编码的错误，那就在你的Python脚本的最上面加入下面这一行：

``` python
# -*- coding: utf-8 -*-  
```
* =（单等号）的作用是将右边的值赋给左边的变量名。==（双等号）的作用是检查左右两边是否相等。

### 数字和数学计算

#### 浮点数
* 整数运算结果仍然是整数，浮点数运算结果仍然是浮点数。
* 整数和浮点数混合运算的结果就变成浮点数。

##### 特别注意：
* %是求余数符号，不是百分号。
* 运算优先级：括号、指数、乘、除、加、减。
* 整数除法算出来比实际小，是因为它将小数部分丢弃了，可以使用浮点数解决。

### 文件相关操作
比较常用的命令：
* close----关闭文件。跟编辑器的“文件”>“保存”是一个意思。
* read----读取文件内容。你可以把结果赋给一个变量。
* readline----读取文本文件中的一行。
* truncate----清空文件。要小心使用哦！
* write(stuff)----将stuff写入文件。

### 函数
#### 函数注意事项
运行（run）函数、调用（call）函数、使用（use）函数是同一个意思。
检查要点：
1. 调用函数时是否使用了函数名？
2. 函数名是否紧跟着(？
3. 括号后有无参数？多个参数是否以逗号隔开？
4. 函数是否以)结尾？

#### 常见函数
* exit(0)可以中断某个程序，其中的数字参数表示程序是否是遇到错误而中断的；exit(0)表示正常退出，exit(1)表示发生了错误。

### 逻辑关系（布尔逻辑表达式 boolean logic expression）
#### 逻辑术语
在Python中会使用下面的术语（字符或者词汇）来定义事物的真（True）或者假（False）。计算机的逻辑就是在某个位置检查这些字符或者变量组合在一起表达的结果是真是假。
* and  与
* or    或
* not    非
* !=   不等于
* ==   等于
* \>=    大于等于
* <=    小于等于
* True    真
* False    假

#### 真值表
我们将使用这些字符来创建你需要记住的真值表。

|     NOT   |   真假 |
|----------|:---------:|
|not False  |  True|
|not True  | False|

|  OR   |   真假   |
|-------|:-------:|
|True or False|True|
|True or True|True|
|False or True|True|
|False or False|False|

|  AND  |   真假   |
|-------|:-------:|
|True and False| False|
|True and True|True|
|False and True|False|
|False and False|False|

|  NOT OR  |   真假   |
|-------|:-------:|
|not(True or False)|False|
|not(True or True)|False|
|not(False or True)|False|
|not(False or False)|True|

|  NOT AND  |   真假   |
|-------|:-------:|
|not(True and False)|True|
|not(True and True)|False|
|not(False and True)|True|
|not(False and False)|True|

|  !=  |   真假   |
|-------|:-------:|
|1!=0|True|
|1!=1|False|
|0!=1|True|
|0!=0|False|

|  ==  |   真假   |
|-------|:-------:|
|1==0|False|
|1==1|True|
|0==1|False|
|0==0|True|

#### if
作用：如果这个布尔表达式为真，就运行接下来的代码，否则就跳过这一段。

#### elif
如果多个elif块都是True，Python只会运行它遇到的是True的第一块，所以只有第一个为True的块会运行。

### 循环和列表
#### for循环和while循环
1. 尽量少用while循环，for循环更优。
2. 检查while语句，确定你的布尔表达式最终会变成False
3. 如果不确定，就在while循环的结尾打印出你要测试的值。
4. for循环中可以使用in range(a,b,c) a->起始值，b->结束值，c->跨度（step）值

### 复习各种符号
[参考](http://blog.csdn.net/wws563/article/details/52227705)
#### 关键字
* and：逻辑判断的"与"
* del：list操作符号，用于删除元素
* from：和import一起用，用于导入模块，使用其中的功能。
* not：逻辑判断的"非"
* while：用于在指定条件下循环
* as：用法①：import模块中，给模块起别称；用法②：用于替换try...finally。
* elif：用在if后作为后续选择分支
* global：用于声明全局变量
* or：逻辑判断的"或"
* with：见as
* assert：断言功能，非真的时候会报assertionError，用来debug很好
* else：else用来判断if，elif未包含的其他可能性时执行的内容。
* if：根据布尔值决定是否执行内容。
* pass：在类或函数等下面，加上pass不发生任何事，但保证格式正确，不会报错；在构建时可以先写出空的方法占好位，但不会因为空而导致报错。
``` python
def null_methon():
	pass # do nothing.
```
* yield：yield是用于生成器（Generator）的方法。比较复杂，用于对于通过计算生成大量数据时，节省内存用。
* break：用于中断循环。
* except：用try/except块处理异常状况
* import：导入模块用
* print：打印
* class：生成类
* exec：exec()是个方法，在括号中填入字符串形式的python语句，再执行。不常用
* in：和for连用，执行循环；用于元素是否在元组内（tuple），list内容（字典等未研究能否使用。）
* raise：try下面用于跑出错误的关键词
* continue：用于循环中，表示继续执行
* finally：在try下面用于表示不论正确失败都会执行的内容。
* is：用来对比两个两边的对象是否相等
* return：用于方法返回值用的关键词
* def：声明方法（函数）
* for：循环用的关键词
* lambda：生成匿名函数。（对于不需要多次复用的函数，1.用于提高性能；2.不需要单独声明，简化代码。）
* try：异常处理

#### 数据类型
* True
* False
* None
1.None是一个对象
2.当与None进行比较时不要用 ==，要用is。is是用来比较两个变量是否指向同一个对象。
3.None是False
* strings：字符串
* numbers：数字类型
* floats：浮点数字类型
* lists：列表类型

#### 字符串转义序列
* \\\    --> 输入\
* \'     --> 输出'
* \"   --> 输出"
* \a  --> 响铃
* \b   --> 退格（Backspace）
* \f   --> 换页符
* \n  --> 换行符
* \r  -->  回车符
* \t  --> 横向制表符
* \v  --> 纵向制表符

#### 字符串格式化
* %d --> 有符号整数，10进制
* %i --> 同%d
* %o --> 无符号整数，8进制
* %u --> 无符号整数，10进制
* %x --> 无符号整数，16进制
* %X --> 无符号整数，16进制大写字符
* %e --> 浮点数字，科学计数法
* %E --> 浮点数字，科学计数法，用E替代e
* %f --> 浮点数字，小数点
* %F --> 同%f
* %g --> 浮点数字，根据数字大小自动切换%e或%f
* %G --> 浮点数字，根据数字大小自动切换%E或%F
* %c --> 字符及其ASCII码(输出为字符或ASCII码对应的字符)
* %r --> 字符串 (采用repr()的显示)
* %s --> 字符串 (采用string()的显示)
* %% --> 输出一个百分号

#### 操作符
*    +
*    -
*    *
*    **    --->幂
* /
* //
* %
* <
* \>
* <=
* \>=
* ==
* !=
* <>
* ( ) --> 一个空的元组（Tuple）
* [  ]   --> 一个空的列表（List）
* { }   --> 一个空的字典（Dictionary）
* @   --> 修饰符，@一个函数，把下面一行的函数作为上面@行函数的参数，执行。
* ,
* :
* .
* =
* +=
* -=
* *=
* /=
* //=
* %=
* **=
