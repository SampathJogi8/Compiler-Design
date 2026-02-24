def epsilon_closure(states, transitions):
    stack = list(states)
    closure = set(states)

    while stack:
        state = stack.pop()
        for next_state in transitions.get((state, 'ε'), []):
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)
    return closure

def run_nfa_to_dfa():
    transitions = {
        (0, 'ε'): [1],
        (1, 'a'): [2]
    }

    start = epsilon_closure({0}, transitions)
    print("DFA Start State:", start)
