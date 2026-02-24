grammar = {}

def compute_first(symbol):
    if symbol not in grammar:
        return {symbol}

    result = set()
    for production in grammar[symbol]:
        if production == 'ε':
            result.add('ε')
        else:
            result |= compute_first(production[0])
    return result

def run_first_follow():
    n = int(input("Enter number of productions: "))
    for _ in range(n):
        lhs, rhs = input("Enter production (A->BC): ").split("->")
        grammar.setdefault(lhs, []).append(rhs)

    for non_terminal in grammar:
        print("FIRST(", non_terminal, ") =", compute_first(non_terminal))
