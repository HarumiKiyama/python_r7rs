from llvmlite import ir


class Number:
    def __init__(self, value) -> None:
        self.value = value


class Cons:
    def __init__(self, first, second) -> None:
        self.first = first
        self.second = second


class Cond:
    def __init__(self, conditions) -> None:
        self.conditions = conditions


class Car:
    def __init__(self, pair) -> None:
        self.pair = pair


class Cdr:
    def __init__(self, pair) -> None:
        self.pair = pair


class Define:
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value


class Lambda:
    def __init__(self, args, body) -> None:
        self.args = args
        self.body = body

