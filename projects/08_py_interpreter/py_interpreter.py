# encoding:utf-8

# 基于栈的python 解释器

add_two_nums = {
    "instructions":[("LOAD_VALUE",0),
                    ("LOAD_VALUE",1),
                    ("ADD_TWO_VALUES",None),
                    ("PRINT_ANSWER",None)],
    "numbers":[7,5]
}

add_three_num = {
    "instructions":[("LOAD_VALUE",0),
                    ("LOAD_VALUE",1),
                    ("ADD_TWO_VALUES",None),
                    ("LOAD_VALUE",2),
                    ("ADD_TWO_VALUES",None),
                    ("PRINT_ANSWER",None)],
    "numbers":[7,5,8]
}

# 增加变量的概念
# 1 store_name: 存储变量值，将栈顶的内容存入变量中
# 2 load_name
add_variables = {
    "instructions":[("LOAD_VALUE",0),
                    ("STORE_NAME",0),
                    ("LOAD_VALUE",1),
                    ("STORE_NAME",1),
                    ("LOAD_NAME",0),
                    ("LOAD_NAME",1),
                    ("ADD_TWO_VALUES",None),
                    ("PRINT_ANSWER",None),],
    "numbers":[1,2],
    "names":["a","b"]
}


class Interpreter:
    def __init__(self):
        self.stack = []
        # 存储变量映射关系的字典变量
        self.environment = {}

    def STORE_NAME(self,name):
        val = self.stack.pop()
        self.environment[name] = val

    def LOAD_NAME(self,name):
        val = self.environment[name]
        self.stack.append(val)

    def LOAD_VALUE(self,number):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)


    def parse_argment(self,instruction,argmument,what_to_execute):
        # 解析命令参数
        # 使用常量列表的 方法
        numbers = ['LOAD_VALUE']
        names = ["LOAD_NAME","STORE_NAME"]

        if instruction in numbers:
            argmument = what_to_execute["numbers"][argmument]
        elif instruction in names:
            argmument = what_to_execute['names'][argmument]

        return argmument    



    def run_code(self,what_to_execute):
        # 指令列表
        instructions = what_to_execute['instructions']
        # 常数列表
        numbers = what_to_execute['numbers']
        # 遍历指令列表，一个一个执行
        for each_step in instructions:
            # 得到对应的指令和参数
            instruction,argmument = each_step
            argmument = self.parse_argment(instruction,argmument,what_to_execute)

# 方法一 判断遍历
            # if  instruction == 'LOAD_VALUE':
            #     self.LOAD_VALUE(argmument)
            # elif instruction == 'ADD_TWO_VALUES':
            #     self.ADD_TWO_VALUES()
            # elif instruction == 'PRINT_ANSWER':
            #     self.PRINT_ANSWER()
            # elif instruction == 'LOAD_NAME':
            #     self.LOAD_NAME(argmument)
            # elif instruction == 'STORE_NAME':
            #     self.STORE_NAME(argmument)

# 方法二 使用 getattr()方法获取
            bytecode_method = getattr(self,instruction)
            if argmument is None:
                bytecode_method()
            else:
                bytecode_method(argmument)


if __name__ == '__main__':
    interpreter = Interpreter()

    interpreter.run_code(add_two_nums)
    interpreter.run_code(add_three_num)
