file_paths = ['docs/contents.html', 'docs/introduction.html', 'docs/welcome.html', 'docs/chunks-of-bytecode.html', 'docs/a-bytecode-virtual-machine.html', 'docs/a-map-of-the-territory.html', 'docs/the-lox-language.html']

text = ''

for file_path in file_paths:
    with open(file_path, 'r') as fin:
        text = fin.read()
        text = text.replace('Next Chapter', '下一章')
        text = text.replace('Next Part', '下一部分')
        text = text.replace('What’s in a Name?', '为什么起Lox这个名字？')
        text = text.replace('Expressions and Statements', '表达式和语句')
        text = text.replace('Implicit Semicolons', '隐式分号')
        text = text.replace('Logic Versus History', '逻辑与历史')
        text = text.replace('Static and Dynamic Typing', '动态类型和静态类型')
        text = text.replace('Implicit Variable Declaration', '隐式变量声明')
        text = text.replace('Spoonfuls of Syntactic Sugar', '语法糖')
        text = text.replace('Prototypes and Power', '原型和力量')
        text = text.replace('Test Your Language', '测试你设计的语言')
        text = text.replace('Register-Based Bytecode', '基于寄存器的字节码虚拟机')
        text = text.replace('It’s Just Parsing', '仅仅是解析')
        text = text.replace('String Encoding', '字符串的编码')
        text = text.replace('Considering Goto Harmful', 'Goto有害论')
        text = text.replace('Closing Over the Loop Variable', '循环变量上的闭包')
        text = text.replace('Generational Collectors', '分代垃圾收集器')
        text = text.replace('Novelty Budget', '预算')
        text = text.replace('Appendix', '附录')
        text = text.replace('Scanning on Demand', '按需编写词法扫描器')
        text = text.replace('Generated Syntax Tree Classes', '如何生成抽象语法树类')
        text = text.replace('Classes and Instances', '类和继承')
        text = text.replace('Calls and Functions', '函数调用和函数')
        text = text.replace('Table of Contents', '目录')
        text = text.replace('Welcome', '欢迎')
        text = text.replace('First Part', '第一部分')
        text = text.replace('Introduction', '介绍')
        text = text.replace('A Map of the Territory', '全书导航')
        text = text.replace('The Lox Language', 'Lox语言')
        text = text.replace('A Tree-Walk Interpreter', '一个树遍历解释器的实现')
        text = text.replace('Representing Code', '用抽象语法树来表示代码')
        text = text.replace('Parsing Expressions', '解析表达式')
        text = text.replace('Evaluating Expressions', '对表达式求值')
        text = text.replace('Scanning', '词法扫描器')
        text = text.replace('A Bytecode Virtual Machine', '一个字节码虚拟机的实现')
        text = text.replace('Control Flow', '控制流')
        text = text.replace('Functions', '函数')
        text = text.replace('Resolving and Binding', '变量的绑定和查找')
        text = text.replace('Classes', '类')
        text = text.replace('Inheritance', '继承')
        text = text.replace('Statements and State', '语句')
        text = text.replace('Chunks of Bytecode', '字节码')
        text = text.replace('A Virtual Machine', '虚拟机')
        text = text.replace('Compiling Expressions', '对表达式进行编译')
        text = text.replace('Types of Values', '值的类型')
        text = text.replace('Strings', '字符串')
        text = text.replace('Hash Tables', '哈希表')
        text = text.replace('Global Variables', '全局变量')
        text = text.replace('Local Variables', '局部变量')
        text = text.replace('Jumping Back and Forth', '跳转')
        text = text.replace('Closures', '闭包')
        text = text.replace('Garbage Collection', '垃圾收集')
        text = text.replace('Methods and Initializers', '类里的方法和初始化')
        text = text.replace('Superclasses', '超类')
        text = text.replace('Optimization', '优化')
        text = text.replace('Lox Grammar', 'Lox的语法')
        text = text.replace('Design Note', '语言设计笔记')

    with open(file_path, 'w') as fout:
        fout.write(text)
