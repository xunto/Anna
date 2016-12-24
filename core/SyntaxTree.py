from .Tree import Tree
from . import Tokens


def to_string(tree: Tree):
    if len(tree.children) == 2:
        return '(' + to_string(tree.children[0]) + str(tree.data) + to_string(tree.children[1]) + ')'
    elif len(tree.children) == 1:
        return '(' + str(tree.data) + to_string(tree.children[0]) + ')'
    else:
        return str(tree.data)


def create(tokens: dict):
    tree = Tree()

    stack = []
    for token in tokens:
        if isinstance(token, Tokens.OpenGroupToken) or isinstance(token, Tokens.OperationToken):
            stack.append(tree)

            if isinstance(token, Tokens.OperationToken):
                tree.data = token

            branch = Tree()
            tree.children.append(branch)
            tree = branch
        elif isinstance(token, Tokens.CloseGroupToken) or isinstance(token, Tokens.VariableToken):
            if isinstance(token, Tokens.VariableToken):
                tree.data = token

            if len(stack) > 0:
                parent = stack.pop()

                # Fix extra parenthesis
                if tree.data is None:
                    child = tree.children.pop()
                    parent.children.pop()
                    parent.children.append(child)

                tree = parent
        else:
            raise ValueError()

    if tree.data is None:
        tree = tree.children.pop()

    return tree
