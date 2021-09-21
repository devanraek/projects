#   Story one that will be selected randomly from user. This simple program allows
#   user to fill in the missing words to create a full story.
def madLibs():

    per1 = input("Enter person: ")
    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter an adjective: ")
    noun1 = input("Enter an noun: ")
    adj3 = input("Enter an adjective: ")
    noun2 = input("Enter an noun: ")
    adj4 = input("Enter an adjective: ")
  

    print('A day at the park!')

    madlib = f"Yesterday, {per1} and I went to the park. On our way to the\
    {adj1} park, we saw a {adj2} {noun1} on a bike. We also saw big {adj3}\
    balloons tied to a {noun2}. Once we got to the {adj4} park, the sky"

    print(madlib)