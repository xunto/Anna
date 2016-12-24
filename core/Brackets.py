from .Tokens import ConjunctionToken, DisjunctionToken, EquivalenceToken, ImplicationToken,\
    InversionToken, OpenGroupToken, CloseGroupToken, GroupToken, OperationToken, Token

priority = [
    InversionToken, DisjunctionToken, ConjunctionToken, ImplicationToken, EquivalenceToken
]


def is_reserved(token: Token):
    return isinstance(token, OperationToken) or isinstance(token, GroupToken)


def add_brackets(tokens, open_index, close_index):
    tokens.insert(close_index, CloseGroupToken())
    tokens.insert(open_index, OpenGroupToken())
    return tokens


def find_group_end(tokens, start, reverse=False):
    end = start

    open_brackets = 0
    close_brackets = 0
    while ((open_brackets == 0 or close_brackets == 0) or open_brackets != close_brackets) \
            and end < len(tokens) - 1:
        end += -1 if reverse else 1

        if isinstance(tokens[end], OpenGroupToken):
            open_brackets += 1

        if isinstance(tokens[end], CloseGroupToken):
            close_brackets += 1

    return end


def reverse_tokens(tokens: list):
    tokens.reverse()

    for i in range(0, len(tokens)):
        if isinstance(tokens[i], GroupToken):
            if isinstance(tokens[i], OpenGroupToken):
                tokens[i] = CloseGroupToken()
            else:
                tokens[i] = OpenGroupToken()

    return tokens


def rule_wrap_arguments(tokens: list):  # Добавляет скобки к аргументам
    i = 0
    while i < len(tokens) - 1:
        if not is_reserved(tokens[i]):
            if i == 0:
                tokens = add_brackets(tokens, i, i + 1)
                i += 1

            if not isinstance(tokens[i - 1], OpenGroupToken) or not isinstance(tokens[i + 1], CloseGroupToken):
                tokens = add_brackets(tokens, i, i + 1)
                i += 1
        i += 1

    if not is_reserved(tokens[i]):
        tokens = add_brackets(tokens, len(tokens) - 1, len(tokens))

    return tokens


def restore_operation_bracket(tokens: list, operation: OperationToken):
    if operation.get_reverse():
        tokens = reverse_tokens(tokens)

    i = 0
    while i < len(tokens) - 1:
        if isinstance(tokens[i], operation):
            group_end = find_group_end(tokens, i, reverse=False)

            if operation.get_arguments_amount() > 1:
                group_start = find_group_end(tokens, i, reverse=True)
            else:
                group_start = i

            tokens = add_brackets(tokens, group_start, group_end)
            i += 1
        i += 1

    if operation.get_reverse():
        tokens = reverse_tokens(tokens)

    return tokens


def restore(tokens: list):
    tokens = rule_wrap_arguments(tokens)
    for operation in priority:
        tokens = restore_operation_bracket(tokens, operation)
    return tokens


