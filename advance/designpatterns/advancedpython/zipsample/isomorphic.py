"""


"""



def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # Dictionaries for character mappings
    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):
        print("s = {} . t = {}".format(char_s , char_t ))
        # Check and update s -> t mapping
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t

        # Check and update t -> s mapping
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s

    return True

s = "egg"
t = "add"
print(is_isomorphic(s, t))  # Output: True

s = "foo"
t = "bar"
print(is_isomorphic(s, t))  # Output: False