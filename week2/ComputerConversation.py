"""

:Student: Craig Smith
:Week-2: Conversation with a Computer Assignment
:Course: CMIT-135-40D (Champlain College)
:Professor: Steve Giles

Purpose
-------
This module generates an interactive computer-driven conversation utilizing
one of four random personalities and basic user terminal input.

Constraints
-----------
1. Minimum of 4 unique inputs from the user
2. Inputs must consist of numeric and alphanumeric responses
3. The conversation-bot must utilize 3 of the user inputs as part of its responses
4. The bot must perform some type of arithmetic operation on the inputs
5. The program must include explanatory comments
6. Student must turn in the .py file and a screenshot of the application in use
"""

# Imports
import random
import time

# Personalities
# 1. Alien Responses
# 2. Country Responses
# 3. Surfer Responses
# 4. Dungeon Master Responses


# Constants
GREETINGS = {
    'alien': 'Hello earthling, which way to your leader? North, South, East, or West: ',
    'country': 'Howdy partner, my horse is all tuckered. Which way you heading? '
               'North, South, East, or West: ',
    'surfer': 'Dude.... Like hi and stuff. Which way to the gnarliest waves? '
              'North, South, East, or West: ',
    'dm': 'Greetings brave traveler. You have entered the layer of Malcibot.\n'
          'You are surrounded by four doors. Choose North, South, East, or West: '
}

FIRST_RESPONSE = {
    'alien': 'is what I was thinking. Thank you human. I shall head that way to '
             'meet with your leader.',
    'country': "like a migrating possum. That is what I was thinking. There's a "
               "watering-hole that way.",
    'surfer': 'is a most bodacious choice. Thanks for your tip.',
    'dm': 'door sticks at first, but slowly swings open after some additional '
          'effort on your part.\nYou see a chest on the far end of the room. '
}

SECOND_QUERY = {
    'alien': 'Human, before I traverse, what year is it in "Earth Years": ',
    'country': 'You are kinda cute. How many years under your hat do you have: ',
    'surfer': 'You look like you have seen many waves in your day. How many years'
              ' have you been hitting the surf: ',
    'dm': 'You walk to the chest and inspect it. You see a combination lock with '
          'with three dials each containing the numbers 0 to 9. Above the lock '
          'you see a runic inscription. You consult your memory and work out its'
          ' meaning. "Pythagoras." You must enter a three digit number corresponding '
          'to the settings of the dials to open the lock and reap the rewards: '
}


SECOND_RESPONSE = {
    'alien': " will be the future date of our conquest of your planet.",
    'country': ' more years until you catch up to me.',
    'surfer': ' years for me. Righteous! Rock on with your bad self!'
}

THIRD_QUERY = {
    'alien': 'Puny earthling, does knowing this make you happy or sad: ',
    'country': "What's wrong, does this news make you happy or sad: ",
    'surfer': 'Whoa! Mix vibes dude. You like happy or sad about this: ',
    'dm': 'Thus is the luck of many adventurers. You glance around and see a '
          'runic symbol above a passage-way that looks to be some type of face. Is'
          ' this face happy or sad: '
}

THIRD_RESPONSE = {
    'alien': 'is an interesting emotion. We do not have an equivalent word on my planet.',
    'country': 'is understandable. Many partners may feel that way in this situation.',
    'surfer': '. I get ya. I feel that way on occasion also.',
    'dm': 'is correct. The passage way begins to glow with a brilliant white light.'
}

FOURTH_QUERY = {
    'alien': 'Humanoid, would you like to come with me to visit your leader: ',
    'country': 'Unfortunately my friend, I have to go. You want to tag along: ',
    'surfer': 'Well fellow peop, I gotta go ride a tube. Want to come: ',
    'dm': 'Through the light you see the face of a long forgotten wizard. Do you wish'
          ' to ask a boon of him: '
}

# Helper Functions
def input_validator(person, answer, choices, iferror):
    """
    This function takes the user response and chosen personality to and for the
    first_query and validates the user input against the choices list. The function
    will prompt the user for the correct input with the message in the "iferror"
    until the user returns a correct answer.

    :parameter: **person** string, valid values are 'alien', 'country', 'surfer', 'dm'
    :parameter: **answer** String representing the user response to the query
    :parameter: **choices** list of acceptable strings to compare to the answer
    :parameter: **iferror** string to prompt the user for correct input
    :returns: **list** list containing the validated answer and personality

    """
    while True:
        try:
            assert person.lower() in ['alien', 'country', 'surfer', 'dm'],\
                'Not a Valid Personality'
            if answer.lower() in choices:
                return [answer.lower(), person.lower()]
            else:
                raise ValueError
        except ValueError:
            answer = input(iferror)



def random_incrementor(resp):
    """
    This function takes the user response to the second_query and increments it
    by a random value.

    :parameter: **resp** an integer response value as a string
    :returns: **string** value incremented by a random integer amount

    """
    while True:
        try:
            number_input = int(resp)
            return str(number_input + random.randint(5, 10))
        except ValueError:
            resp = input("I'm sorry, I did not catch your number, please say again: ")


def pythagorean_chest(combination):
    """
    The function takes the user response to the "dm" personality second_query,
    a string value consisting of three integers that represent the users attempt
    at unlocking the chest and determines if the user entered a pythagorean triple.
    The function returns the outcome of the calculation and the dungeon master's
    response.

    :parameter: **combination** String representing 3 integers. Ex: "123"
    :returns: **string** Dungeon Master's response

    """
    success = 'Well done. You have opened the chest without setting off the trap. '
    failure = 'To your dismay, the chest remains locked and you begin to see a ' \
              'green gas begin to leech out of its sides.'

    while True:
        try:
            if int(combination) < 0 or int(combination) > 999:
                raise ValueError
            num_a, num_b, num_c = combination
            if int(num_a)**2 + int(num_b)**2 == int(num_c)**2:
                solved_value = str(num_a) + "^2 + " + str(num_b) + "^2 = " + str(num_c) + "^2"
                return success + solved_value + " is the correct Pythagorean Triple. You " \
                                                "have earned " + str(int(num_c)**2) + " gold pieces."
            else:
                return failure + " You have " + str(int(num_c)**2) + " seconds to escape."
        except ValueError:
            combination = input('You must enter a positive three digit number corresponding '
                                'to the settings of the dials to open the lock: ')



def fourth_response(person, answer):
    """
    This function takes in two strings. One representing a specific personality
    to represent and the second is an answer to a yes/no question. The function
    returns a response based on the combination of personality and yes/no answer.

    :parameter: **person** string, valid values are 'alien', 'country', 'surfer', 'dm'
    :parameter: **answer** Input from the user, valid values are 'yes' and 'no'
    :returns: **string** response based on personality and yes/no answer

    """
    resp = {
        'yes':
            {
                'alien': 'I am glad you said yes. I promise the probing will not take long.',
                'country': "Yee hah! I am glad you said yes buckaroo. Let's ride!",
                'surfer': 'Totally tubular! Yes it is then! Let us catch a wave!',
                'dm': 'The wizard sees the good in you, heals you of any ailments,'
                      'and gives you a renown sword of fabulous beauty.'
            },
        'no':
            {
                'alien': 'Puny human, while no is understandable, it is not an option.',
                'country': 'I am saddened by your no, but I understand. Happy Trails buckaroo.',
                'surfer': 'Bummer. Sorry to here the no. Perhaps we can share a wave another time.',
                'dm': 'The wizard sees the good in you, heals you of any ailments,'
                      'and proceeds to tell you that you are a key character in a prophecy.'
            }
    }

    while True:
        try:
            assert person.lower() in ['alien', 'country', 'surfer', 'dm'],\
                'Not a Valid Personality'
            if answer.lower() in ['yes', 'no']:
                return resp[answer.lower()][person.lower()]
            else:
                raise ValueError
        except ValueError:
            answer = input("Did you say yes or no: ")


# Main
personality = random.choice(['alien', 'country', 'surfer', 'dm'])

# Initial Greeting and Response
response = input(GREETINGS[personality])
validated_response = input_validator(personality, response, ['north', 'south', 'east', 'west'],
                                     'I do not understand, please restate ')
print()
print(validated_response[0].capitalize(), FIRST_RESPONSE[personality])
print()

# Second Query and Response
response = input(SECOND_QUERY[personality])
print()
if personality != 'dm':
    incremented_years = random_incrementor(response)
    print(incremented_years + SECOND_RESPONSE[personality])
else:
    print(pythagorean_chest(response))

# Third Query and Response
print()
response = input(THIRD_QUERY[personality])
validated_response = input_validator(personality, response, ['happy', 'sad'],
                                     'I am sorry, did you say you were happy or sad: ')
print()
print(validated_response[0].capitalize(), THIRD_RESPONSE[personality])
print()

# Fourth Query and Response
response = input(FOURTH_QUERY[personality])
print()
print(fourth_response(personality, response))
time.sleep(5)



