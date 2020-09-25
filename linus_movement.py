#!/usr/bin/env python3
#!/usr/bin/env python3
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# linus_movement.py
# Moves my robot based on several commands
# Modified by Edgardo Peregrino
# 9/24/2020

"""A demo of the Google CloudSpeech recognizer."""
#import libraries
from gpiozero import Robot
from time import sleep
from aiy.pins import (PIN_A, PIN_B, PIN_C, PIN_D)
import aiy.voice.tts

import argparse
import locale
import logging

from aiy.cloudspeech import CloudSpeechClient

#Define the robot
linus = Robot(left = (PIN_A, PIN_B), right = (PIN_C, PIN_D))

#create a function that creates hints to what to say to the box
def get_hints(language_code):
    if language_code.startswith('en_'):
        return ('go forward',
                'go backward',
                'go left',
                'go right',
                'goodbye',
                'shape',
                'attack',
                'dance',
                'spin',
                'twirl')
    return None

#create a function that defines the local language based on location
def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def main():
    #log any issues and print the commands on the terminal
    logging.basicConfig(level=logging.DEBUG)
    # use this if you aren't using English
    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()
    #initialize the cloudspeech API
    logging.info('Initializing for language %s...', args.language)
    hints = get_hints(args.language)
    client = CloudSpeechClient()
    while True:
        #here it detects if your statements match with the hints
        if hints:
            logging.info('Say something, e.g. %s.' % ', '.join(hints))
        else:
            logging.info('Say something.')
        text = client.recognize(language_code=args.language, hint_phrases=hints)
        if text is None:
            logging.info('You said nothing.')
            continue
        logging.info('You said: "%s"' % text)
        # Robot moves based on which ever direction it is told
        text = text.lower()
        if 'go forward' in text:
            aiy.voice.tts.say('Moving up')
            linus.forward()
            sleep(1)
            linus.stop()
        elif 'go backward' in text:
            aiy.voice.tts.say('Moving back')
            linus.backward()
            sleep(1)
            linus.stop()
        elif 'go left' in text:
            aiy.voice.tts.say('going left')
            linus.left()
            sleep(0.3)
            linus.stop()
        elif 'go right' in text:
            aiy.voice.tts.say('going right')
            linus.right()
            sleep(0.3)
            linus.stop()
        elif 'shape' in text:
            aiy.voice.tts.say('Let us groove')
            for i in range(4):
                linus.forward()
                sleep(1)
                linus.right()
                sleep(0.5)
            linus.stop()
        elif 'attack' in text:
            aiy.voice.tts.say('Time to fight')
            linus.forward()
            sleep(1)
            linus.backward()
            sleep(1)
            linus.stop()
        elif 'dance' in text:
            aiy.voice.tts.say('Watch my moves')
            linus.forward()
            sleep(0.5)
            linus.backward()
            sleep(0.5)
            linus.right()
            sleep(0.5)
            linus.left()
            sleep(0.5)
            linus.stop()
        elif 'spin' in text:
            aiy.voice.tts.say('spin time')
            linus.left()
            sleep(2)
            linus.stop()
        elif 'twirl' in text:
            aiy.voice.tts.say('dance time')
            linus.right()
            sleep(2)
            linus.stop()
        elif 'goodbye' in text:
            aiy.voice.tts.say('See you soon')
            linus.stop()
            break

if __name__ == '__main__':
    main()        



