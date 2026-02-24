class State:
    def __init__(self):
        self.edges = {}

class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def symbol_nfa(symbol):
    start = State()
    end = State()
    start.edges[symbol] = [end]
    return NFA(start, end)

def run_re_to_nfa():
    symbol = input("Enter single symbol regex: ")
    nfa = symbol_nfa(symbol)
    print("NFA constructed successfully for:", symbol)
