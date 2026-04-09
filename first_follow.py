
def compute_first(grammar):
    first = {nt:set() for nt in grammar}
    for nt in grammar:
        for prod in grammar[nt]:
            first[nt].add(prod[0])
    return first

def compute_follow(grammar, start):
    follow = {nt:set() for nt in grammar}
    follow[start].add('$')
    return follow
