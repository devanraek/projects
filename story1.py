#   Story one that will be selected randomly from user. This simple program allows
#   user to fill in the missing words to create a full story.
def madLib():

    per1 = input("Enter person: ")
    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter an adjective: ")
    noun1 = input("Enter an noun: ")
    adj3 = input("Enter an adjective: ")
    noun2 = input("Enter an noun: ")
    adj4 = input("Enter an adjective: ")
    adj5 = input("Enter an adjective: ")
    verb1 = input("Enter an verb: ")
    verb2 = input("Enter an verb: ")
    per2 = input("Enter person: ")
    verb3 = input("Enter verb: ")
    adj6 = input("Enter adjective: ")
    verb4 = input("Enter verb: ")

    print('A day at the park!')

    madlib = f"Yesterday, {per1} and I went to the park. On our way to the\
    {adj1} park, we saw a {adj2} {noun1} on a bike. We also saw big {adj3}\
    balloons tied to a {noun2}. Once we got to the {adj4} park, the sky\
    turned {adj5}. It started to {verb1} and {verb2}. {per2} and I {verb3}\
    all the way home. Tomoorrow we will try to go to the {adj6} park again\
    and hope it doesn't {verb4}!"

    print(madlib)