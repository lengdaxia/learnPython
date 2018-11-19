from syldb.core import TYPE_MAP

LIKE_SYMBOL = '%'

def __is(data,condition):
    return data == condition

def __is_not(data,condition):
    return data != condition

def __in(data,condition):
    return data in condition

def __not_in(data,condition):
    return data not in condition

def __greater(data,condition):
    return data > condition

def __less(data, condition):
    return data < condition


def __greater_and_equal(data, condition):
    return data >= condition


def __less_and_equal(data, condition):
    return data <= condition

def __like(data,condition):
    tmp = condition.split(LIKE_SYMBOL)
    length = len(tmp)
    if length == 3:
        condition = tmp[1]
    elif length == 2:
        raise Exception('Syntas Error')
    elif length == 1:
        condition = tmp[0]
    return condition in data

def __range(data,condition):
    return condition[0] <= data <= condition[1]

SYMBOL_MAP = {
    'IN':__in,
    'NOT_IN':__not_in,
    '>':__greater,
    '<': __less,
    '=': __is,
    '!=': __is_not,
    '>=': __greater_and_equal,
    '<=': __less_and_equal,
    'LIKE': __like,
    'RANGE': __range
}


class BaseCase:
    def __init__(self,condition,symbol):
        self.condition = condition
        self.symbol = symbol

    def __call__(self,data,data_type):
        self.condition = TYPE_MAP[data_type.value](self.condition)

        if isinstance(self.condition,str):
            self.condition = self.condition.replace("'",'').replace("",'')

        return SYMBOL_MAP[self.symbol](data,self.condition)
class BaseListCase(BaseCase):
    def __call__(self,data,data_type):
        if not isinstance(self.condition,list):
            raise TypeErrpr('condition type error ,value must be %s' data_type)

        conditions = []

        for value in self.condition:
            value = TYPE_MAP[data_type.value](value)

            if isinstance(value,str)
                value = value.replace("'",'').replace("",'')
            conditions.append(value)
        return SYMBOL_MAP[self.symbol](data,conditions)


