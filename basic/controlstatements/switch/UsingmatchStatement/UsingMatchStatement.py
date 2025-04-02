def switch_example(case):
    match case:
        case 1:
            return "Case 1 selected"
        case 2:
            return "Case 2 selected"
        case 3:
            return "Case 3 selected"
        case _:
            return "Default case: Case not found"

# Example usage
print(switch_example(2))  # Output: Case 2 selected
print(switch_example(4))  # Output: Default case: Case not found