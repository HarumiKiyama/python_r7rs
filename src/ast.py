from abc import ABC, abstractmethod


class Env:
    def __init__(self):
        self._env = {}
        self._tmp_env_list = []

    def __getitem__(self, key):
        for d in reversed(self._tmp_env_list):
            if key in d:
                return d[key]
        return self._env[key]

    def set_env(self, key, value):
        self._env[key] = value

    def append_tmp(self, d):
        self._tmp_env_list.append(d)

    def pop_tmp(self):
        self._tmp_env_list.pop()


env_table = Env()


class Node(ABC):
    @abstractmethod
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

    def eval(self):
        return self.pair[0]


class Cdr(Node):
    def __init__(self, pair) -> None:
        self.pair = pair

    def eval(self):
        return self.pair[1]


class Define(Node):
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

    def eval(self) -> None:
        env_table.set_env(self.name, self.value)


class Lambda(Node):
    def __init__(self, args, body) -> None:
        self.args = args
        self.body = body

    def eval(self) -> 'Lambda':
        return self

    def apply(self, real_args):
        if len(real_args) != len(self.args):
            raise ValueError(f'arg list length not equal to parameter list')
        local_table = {k: v for k, v in zip(self.args, real_args)}
        env_table.append_tmp(local_table)
        rv = self.body.eval()
        env_table.pop_tmp()
        return rv


class Apply(Node):
    def __init__(self, func, args) -> None:
        self.func = func
        self.args = args

    def eval(self):
        if not isinstance(self.func, Lambda):
            self.func = env_table[self.func]
        return self.func.apply(self.args)


class Name(Node):
    def __init__(self, name):
        self.name = name

    def eval(self):
        return env_table[self.name]


class Biop(Node):
    def __init__(self, first, second) -> None:
        self.first = first
        self.second = second

    def eval(self) -> None:
        pass


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
