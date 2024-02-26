import copy


class Stack:
    def __init__(self):
        self.__values = list()

    def is_empty(self):
        return len(self.__values) == 0

    def push(self, c):
        self.__values.append(c)

    def pop(self):
        if len(self.__values) == 0:
            raise Exception("stack is empty")
        return self.__values.pop()

    def print(self):
        for c in self.__values:
            print(c, sep="")


class Result:

    def __init__(self, is_ok, position=0):
        self.is_ok = is_ok
        self.position = position


def is_correct(buf):
    s = Stack()
    opened_brackets = "([{"
    closed_brackets = ")]}"
    i = 0
    while i < len(buf):
        c = buf[i]
        if c in opened_brackets:
            s.push(c)
        elif c in closed_brackets:
            if s.is_empty():
                return Result(False, i)
            pos = closed_brackets.find(c)
            opened_bracket = s.pop()
            if opened_bracket != opened_brackets[pos]:
                return Result(False, i)
        i += 1
    if s.is_empty():
        return Result(True)
    else:
        return Result(False, i)


def print_result(res, buf):
    if res.is_ok:
        print(f"{buf} <- correct")
    else:
        print(f"{buf} <- incorrect")
        print(f"{(' ' * res.position)}"
              "^-- error position")


def main():
    buf = "wefw"
    res = is_correct(buf)
    print_result(res, buf)
    buf = "((wef)wef{wef{wef}few}ef)"
    res = is_correct(buf)
    print_result(res, buf)
    buf = ")"
    res = is_correct(buf)
    print_result(res, buf)
    buf = "((}))wer"
    res = is_correct(buf)
    print_result(res, buf)
    buf = "(we(we{ wefwe)}wer))wer"
    res = is_correct(buf)
    print_result(res, buf)
    buf = "(we(we{ wefwe"
    res = is_correct(buf)
    print_result(res, buf)

    #пример для глубокого копирования
    s1 = Stack()
    s1.push('a')
    s1.push('b')
    s2 = copy.deepcopy(s1)
    s1.pop()
    s1.print()
    print('ffff')
    s2.print()


main()
