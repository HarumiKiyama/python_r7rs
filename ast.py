from abc import ABC, abstractclassmethod
from llvmlite import ir


class Node(ABC):
    @abstractclassmethod
    def eval(self):
        pass


class Number(Node):
    def __init__(self, value) -> None:
        self.value = value

    def eval(self):
        return self.value


class Nil(Node):
    def __init__(self) -> None:
        pass

    def eval(self):
        return None


class Cons(Node):
    def __init__(self, first, second) -> None:
        self.first = first
        self.second = second

    def eval(self):
        return self.first, self.second


class Cond(Node):
    def __init__(self, conditions) -> None:
        self.conditions = conditions

    def eval(self):
        for val, act in self.conditions:
            if val.eval():
                return act.eval()


class Car(Node):
    def __init__(self, pair) -> None:
        self.pair = pair


class Cdr(Node):
    def __init__(self, pair) -> None:
        self.pair = pair


class Define(Node):
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value


class Lambda(Node):
    def __init__(self, args, body) -> None:
        self.args = args
        self.body = body


class Biop(Node):
    def __init__(self, first, second) -> None:
        self.first = first
        self.second = second


class Add(Biop):
    def eval(self):
        return self.first.eval() + self.second.eval()


class Mul(Biop):
    def eval(self):
        return self.first.eval() * self.second.eval()


class Sub(Biop):
    def eval(self):
        return self.first.eval() - self.second.eval()


class Div(Biop):
    def eval(self):
        return self.first.eval() / self.second.eval()
