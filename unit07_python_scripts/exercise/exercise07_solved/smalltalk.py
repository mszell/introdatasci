########## SAMPLE SOLUTION FOR EXERCISE 07, TASK 4 ############

# NOTE: there are lots of (also easier) solutions to this task.
# the code below is just an EXAMPLE solution.

########## CONDITIONAL REPLIES STORED IN DICTS ############

# to provide a reply that depends on the user input
# and to have a better overview of the input-reply pairs,
# we store these pairs in a dictionary, 
# all allowed user inputs as keys and the corresponding replies as values

# mood_dict has possible user inputs as keys,
# and possible replies as values
# e.g. if user says "1", the script will reply "Sorry to hear that"
mood_dict = {
    "1" : "Sorry to hear that.", 
    "2" : "Tomorrow is another day!",
    "3" : "I'm also doing so-so.",
    "4" : "That's good to hear!",
    "5" : "That's awesome!"
}

# weather_dict has possible inputs as keys,
# and possible replies as values 
weather_dict = {
    "yes" : "Me too!",
    "no"  : "Me neither!"
}

########## CATCHING ERRORS ############

# to check whether the user input is in an allowed value (and thus in the dict)
# or a forbidden value (and thus needs to be pointed out as wrong input),
# we define 2 short functions:

# function that returns either the value from the mood_dict,
# or an error message if the input was not in the mood_dict keys
def comment_on_mood(m, m_dict):
    if m not in m_dict:   
        return "You should have answered with a number from 1 to 5 :("    
    else:
        return m_dict[m]

# function that returns either the value from the weather_dict,
# or an error message if the input was not in the weather_dict keys
def comment_on_weather(w, w_dict):
    if w not in w_dict:
        return "You should have answered 'yes' or 'no' :("
    else:
        return w_dict[w]

########## ASKING ABOUT THE MOOD ############

# first question: mood; save user input to the variable "mood"
mood = input("How are you doing today, on a scale from 1 to 5?\n")
# get the answer
ans1 = comment_on_mood(m=mood, m_dict=mood_dict)
# display the answer to the user
print(ans1)

########## ASKING ABOUT THE WEATHER ############

# second question: weather; save user input to the variable "weather"
weather = input("Do you like the weather today?\n")
# get the answer
ans2 = comment_on_weather(w=weather, w_dict=weather_dict)
# display the answer to the user
print(ans2)