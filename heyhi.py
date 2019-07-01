import os
import sys
import re
import speech_recognition as sr
import webbrowser
import random


GREET_CMDS = ['what\'s up', 'how are you', 'how you doing', 'greetings']
GREET_RESP = ['wild and free!', 'Livin by the day', 'just chillin you know', 'how you doin']
OFF_CMDS = ['goodbye', 'turn off', 'shut down', 'go to sleep', 'night buddy']
BAD_CMDS = ['f*** you', 'f*** off', 'go to hell', 'motherfucker']
BAD_RESP = ['hey, its not polite', 'wow, its not nice', 'dont say it please']


# Speaks audio passed - voice
def speecher(audio):

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

# Listens for user-commands
def my_command():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    # loop back to continue to listen for commands if unrecognizable speech
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = my_command()

    return command

# if-cases for executing commands
def assistant(command):

    if command in GREET_CMDS:
        random_greeting = random.choice(GREET_RESP)
        speecher(random_greeting)
        
    if command in BAD_CMDS:
        random_greeting = random.choice(BAD_RESP)
        speecher(random_greeting)

    if command in OFF_CMDS:
        speecher('Bye Bye, and Mazal Tov Gal')
        sys.exit()

    if 'open' in command:
        reg_ex = re.search('open (.*)', command)
        app = reg_ex.group(1)
        print("..Searching for application " + app)
        if reg_ex:
            os.system(app)
            print(app + " Opened.")

    if 'go to website' in command:
        reg_ex = re.search('go to website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Opened!')
        else:
            pass


if __name__ == "__main__":

    speecher('Hello, I am Buddy, your friend')
    speecher('Speak your command...')

    while True:
        assistant(my_command())
