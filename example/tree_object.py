class Tree:
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches
    def __repr__(self):
        if self.branches:
            return 'Tree({0},{1})'.format(self.entry, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.entry))
    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left  = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return Tree(left.entry + right.entry, (left, right))

def sum_entries(t):
    """Sum the entries of a Tree instance, which may be None."""
    return t.entry + sum([sum_entries(b) for b in t.branches])

    