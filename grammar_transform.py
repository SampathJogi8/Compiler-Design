def remove_left_recursion(A, productions):
    alpha = []
    beta = []

    for prod in productions:
        if prod.startswith(A):
            alpha.append(prod[len(A):])
        else:
            beta.append(prod)

    if not alpha:
        print("No Left Recursion")
        return

    print(f"{A} ->", " | ".join([b + A+"'" for b in beta]))
    print(f"{A}' ->", " | ".join([a + A+"'" for a in alpha]) + " | ε")

def run_grammar_transform():
    A = input("Enter Non-Terminal: ")
    productions = input("Enter productions separated by space: ").split()
    remove_left_recursion(A, productions)
