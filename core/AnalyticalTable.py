from .Tree import Tree
from . import Tokens, SyntaxTree


class Table(Tree):
    def __init__(self, data=None, children=None):
        if data is None:
            data = []
        super().__init__(data, children)

    def find_roots(self):
        stack = [self]
        result = []
        while len(stack) > 0:
            item = stack.pop()

            if len(item.children) == 0:
                result.append(item)

            for child in item.children:
                stack.append(child)

        return result


class Presumed:
    def __init__(self, tree: Tree):
        self.tree = tree


class PresumedTrue(Presumed):
    def __str__(self):
        return 't' + SyntaxTree.to_string(self.tree)


class PresumedFalse(Presumed):
    def __str__(self):
        return 'f' + SyntaxTree.to_string(self.tree)


ADD_ACTION = 'add_action'
SPLIT_ACTION = 'split_action'
IGNORE_ACTION = 'ignore_action'


def build(syntax_tree: Tree):
    table = Table()

    result_table = table

    items = [(table, PresumedFalse(syntax_tree))]
    while len(items) > 0:
        table, presumed = items.pop()
        syntax_tree = presumed.tree

        action_type = IGNORE_ACTION
        action_data = []

        # Rules for logical actions
        # Inversion (!)
        if isinstance(syntax_tree.data, Tokens.InversionToken):
            action_type = ADD_ACTION
            if isinstance(presumed, PresumedTrue):
                action_data = [PresumedFalse(syntax_tree.children[0])]
            else:
                action_data = [PresumedTrue(syntax_tree.children[0])]
        # Conjunction (&)
        elif isinstance(syntax_tree.data, Tokens.ConjunctionToken):
            if isinstance(presumed, PresumedTrue):
                # tA tB
                action_type = ADD_ACTION
                action_data = [PresumedTrue(syntax_tree.children[0]), PresumedTrue(syntax_tree.children[1])]
            else:
                # fA | fB
                action_type = SPLIT_ACTION
                action_data = [PresumedFalse(syntax_tree.children[0]), PresumedFalse(syntax_tree.children[1])]
        # Disjunction (|)
        elif isinstance(syntax_tree.data, Tokens.DisjunctionToken):
            if isinstance(presumed, PresumedTrue):
                # tA | tB
                action_type = SPLIT_ACTION
                action_data = [PresumedTrue(syntax_tree.children[0]), PresumedTrue(syntax_tree.children[1])]
            else:
                # fA fB
                action_type = ADD_ACTION
                action_data = [PresumedFalse(syntax_tree.children[0]), PresumedFalse(syntax_tree.children[1])]
        # Implication (->)
        elif isinstance(syntax_tree.data, Tokens.ImplicationToken):
            if isinstance(presumed, PresumedTrue):
                # fA | tB
                action_type = SPLIT_ACTION
                action_data = [PresumedFalse(syntax_tree.children[0]), PresumedTrue(syntax_tree.children[1])]
            else:
                # tA fB
                action_type = ADD_ACTION
                action_data = [PresumedTrue(syntax_tree.children[0]), PresumedFalse(syntax_tree.children[1])]
        # Equivalence (<->)
        elif isinstance(syntax_tree.data, Tokens.EquivalenceToken):
            #
            tree = Tree()
            tree.data = Tokens.ConjunctionToken()

            tmp = Tree(Tokens.ImplicationToken(), [syntax_tree.children[0], syntax_tree.children[1]])
            tree.children.append(tmp)

            tmp = Tree(Tokens.ImplicationToken(), [syntax_tree.children[1], syntax_tree.children[0]])
            tree.children.append(tmp)

            items.append((table, presumed.__class__(tree)))
        elif isinstance(syntax_tree.data, Tokens.VariableToken):
            pass
        else:
            raise ValueError()

        if action_type == ADD_ACTION:
            for item in action_data:
                items.append((table, item))
        elif action_type == SPLIT_ACTION:
            roots = table.find_roots()
            for sub_scope in roots:
                for item in action_data:
                    new_scope = Table()
                    items.append((new_scope, item))
                    sub_scope.children.append(new_scope)
        elif action_type == IGNORE_ACTION:
            pass
        else:
            raise ValueError()

        table.data.append(presumed)
    return result_table
