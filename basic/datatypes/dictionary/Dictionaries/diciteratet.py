s_to_t = {}
t_to_s = {}

def zipfunc(s,t) :
    for char_s, char_t in zip(s, t):
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t

        # Check and update t -> s mapping
        # if char_t in t_to_s:
        #     if t_to_s[char_t] != char_s:
        #         return False
        # else:
        #     t_to_s[char_t] = char_s

    print(s_to_t) # {'e': 'a', 'g': 'd'}
    print(t_to_s) # {'a': 'e', 'd': 'g'}

s = "egd"
t = "add"
print(list(zip(s,t))) # [('e', 'a'), ('g', 'd'), ('g', 'd')]

#zipfunc(s,t)

def validateDict(s: str , t:str) -> bool:

    for char_s, char_t in zip(s, t):
        print("Dict elements are  {} {} : ".format(char_s , char_t))

        if char_s in s_to_t:
            print(" {} is present in the dict".format(char_s))
            if s_to_t[char_s] != char_t:
                return False

        else:
            print(" {} is not present in the dict".format(char_s))
            s_to_t[char_s] = char_t

    print(s_to_t)
    return True

print(validateDict(s,t))