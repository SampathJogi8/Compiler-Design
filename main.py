from Lab1_Lexical_Analyzer.lexical_analyzer import run_lexical
from Lab2_RE_to_NFA.re_to_nfa import run_re_to_nfa
from Lab3_NFA_to_DFA.nfa_to_dfa import run_nfa_to_dfa
from Lab4_Grammar_Transformations.grammar_transform import run_grammar_transform
from Lab5_First_Follow.first_follow import run_first_follow
from Lab6_Predictive_Parsing_Table.predictive_parser import run_predictive_parser

def main():
    while True:
        print("\n--- Compiler Design Lab ---")
        print("1. Lexical Analyzer")
        print("2. RE to NFA")
        print("3. NFA to DFA")
        print("4. Grammar Transformations")
        print("5. FIRST and FOLLOW")
        print("6. Predictive Parsing Table")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            run_lexical()
        elif choice == '2':
            run_re_to_nfa()
        elif choice == '3':
            run_nfa_to_dfa()
        elif choice == '4':
            run_grammar_transform()
        elif choice == '5':
            run_first_follow()
        elif choice == '6':
            run_predictive_parser()
        elif choice == '7':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
