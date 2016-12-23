class Token:
    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__str__()


class VariableToken(Token):
    name = 'unknown'

    def __str__(self):
        return self.name


class OperationToken(Token):
    pass


class InversionToken(OperationToken):
    def __str__(self):
        return '!'


class ConjunctionToken(OperationToken):
    def __str__(self):
        return '&'


class DisjunctionToken(OperationToken):
    def __str__(self):
        return '|'


class ImplicationToken(OperationToken):
    def __str__(self):
        return '->'


class EquivalenceToken(OperationToken):
    def __str__(self):
        return '<->'


class GroupToken(Token):
    pass


class OpenGroupToken(GroupToken):
    def __str__(self):
        return '('


class CloseGroupToken(GroupToken):
    def __str__(self):
        return ')'
