#This is a simply program that allows the user to input answers to the missing words
#in the madlibs game. The user has the choice between three different madlib choices.
from story_Ran import story1, story2, story3
import random

if __name__ =="__main__":
    r = random.choice([story1, story2, story3])
    r.madLibs()
    
