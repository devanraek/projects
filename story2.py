#   Story one that will be selected randomly from user. This simple program allows
#   user to fill in the missing words to create a full story.
def madLibs():

    company = input("Enter name of company: ")
    offer = input("What does your business offer? : ")
    audience = input("Enter a defined audience: ")
    prob = input("How do you solve a problem? : ")
    secert = input("Enter your secret sauce: ")
    

    print('Startup Company')

    madlib = f"My company, {company}, is developing {offer} to help {audience} {prob} with {secert}."

    print(madlib)