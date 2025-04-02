def switch_example(case):
    switch_dict = {
        1: "Case 1 selected",
        2: "Case 2 selected",
        3: "Case 3 selected"
    }
    return switch_dict.get(case, "Default case: Case not found")

# Example usage
print(switch_example(1))  # Output: Case 1 selected
print(switch_example(4))  # Output: Default case: Case not found
