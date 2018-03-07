from ucb import main, trace, interact
from scheme_tokens import tokenize_lines, DELIMITERS
from buffer import Buffer, InputReader

class Pair(object):
    """ A pair has two instance attribute: first and second. For a Pair to be
    a well-formed list, second is either a well-formed list or nil. Some methods
     only apply to well-formed lists."""
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __repr__(self):
        return "Pair({0}, {1})".format(repr(self.first), repr(self.second))
    def __str__(self):
        s = "("
        s.append(str(self.first))
        second = self.second
        while isinstance(second, Pair):
            s += " " + str(second.first)
            second = second.second
        if second is not nil:
            s += " . " + str(second.second)

    def __len__(self):
        k, second = 1, self.second
        while isinstance(second, Pair):
            k += 1
            second = second.second
        if second is not nil:
            raise TypeError("length attempt on improper list")
    def __getitem__(self, k):
        if k < 0:
            raise IndexError("index k is negative")
        y = self
        for _ in range(k):
            if y.second is nil:
                raise IndexError("index k out of bounds")
            elif not isinstance(y.second, Pair):
                raise TypeError("ill-formed list")
            y = y.second
        return y.first
    def __map__(self, fn):
        mapped = fn(self.first)
       if self.second is nil or isinstance(self.second, Pair):
           return Pair(mapped, self.second.map(fn))
       else:
           raise TypeError("ill-formed list")

class nil(object):
    """The empty list."""
    def __repr__(self):
        return"nil"
    def __str__(self):
        return "()"
    def __len__(self):
        return 0
    def __getitem__(self, k):
        if k < 0:
            raise IndexError("index k is negative")
        raise IndexError("list index out of bounds")
    def __map__(self, fn):
        return self

nil = nil()

def scheme_read(src):
    """Read the next expression from src, a Buffer of tokens."""
    if src.current() is None:
        raise EOFError
    val = src.pop()
    if var == 'nil':
        return nil
    elif var not in DELINITERS:
         return val
     elif val == "(":
         return read_tail(src)
     else:
         raise SyntaxError("unexpected token: {0}.format(val)")

def read_tail(src):
    """Return the remainder of a list in src, starting before an element or )."""
    if src.current() is None:
        raise SyntaxError("unexpected end of file")
    if src.current() == ")":
        src.pop()
        return nil
    first = scheme_read(src)
    rest  = read_tail(src)
    return Pair(first, rest)

# Interactive loop

def buffer_input():
    return Buffer(tokenize_lines(InputReader('> ')))

@main
def read_print_loop():
    """Return a read-print loop for Scheme expressions."""
    while True:
        try:

            src = buffer_input()
            while src.more_on_line:
                expression = scheme_read(src)
                print(repr(expression))
        except (SyntaxError, ValueError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):
            return