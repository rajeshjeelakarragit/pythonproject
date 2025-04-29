from numpy.ma.core import true_divide


def user_choice():
    choice = input("Please enter a number (1-10) :")
    return int(choice)

def user_choiceIn():
   result="WRONG"
   acceptance_value=[1,2,3]
   return (result in acceptance_value)


def user_choiceNotIn():
   result="WRONG"
   acceptance_value=[1,2,3]
   return (result not in acceptance_value)

def user_choice_withloop():

        choice = 'WRONE'
        acceptance_range = range(1,10)
        within_range = False

        while not choice.isdigit() or not within_range: # choice.isdigit() == False !F or F 5
           choice = input("Please enter a number (1-10) :")
           if not choice.isdigit(): # two - !F
               print("Sorry, that is not number")

           if choice.isdigit():
               if int(choice.isdigit()) in acceptance_range:
                   within_range = True
               else:
                   print("Sorry, you are out of acceptable range(0-10)")
                   within_range = False
        return int(choice)

#print(user_choice())

if __name__=='__main__':
    print(user_choice_withloop())