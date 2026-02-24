def run_predictive_parser():
    parsing_table = {}

    non_terminal = input("Enter Non-Terminal: ")
    terminal = input("Enter Terminal: ")
    production = input("Enter Production: ")

    parsing_table[(non_terminal, terminal)] = production

    print("Parsing Table:")
    for k, v in parsing_table.items():
        print(k, "=>", v)
