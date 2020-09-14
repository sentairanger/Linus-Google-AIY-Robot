#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
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
# motor_movement.py
# Moves the motor based on voice commands
# Modified by Edgardo Peregrino
# 9/2/2020

"""A demo of the Google CloudSpeech recognizer."""
#import libraries
from gpiozero import Motor
from time import sleep
from aiy.pins import PIN_A, PIN_B
import aiy.voice.tts

import argparse
import locale
import logging

from aiy.cloudspeech import CloudSpeechClient

#Define the motor
motor = Motor(forward=PIN_A, backward = PIN_B)

#create a function that creates hints to what to say to the box
def get_hints(language_code):
    if language_code.startswith('en_'):
        return ('go forward',
                'go backward',
                'move around',
                'goodbye')
    return None

#create a function that defines the local language based on location
def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def main():
    #log any issues and print the commands on the terminal
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(description='Assistant service example.')
    # use this if you aren't using English
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
        text = client.recognize(language_code=args.language,
                                    hint_phrases=hints)
        if text is None:
            logging.info('You said nothing.')
            continue

        logging.info('You said: "%s"' % text)
        text = text.lower()
        #perform actions based on voice commands
        if 'go forward' in text:
            aiy.voice.tts.say('Okay I will go forward')
            motor.forward()
            sleep(2)
            motor.stop()
        elif 'go backward' in text:
            aiy.voice.tts.say('Okay I will go backward')
        elif 'move around' in text:
            aiy.voice.tts.say('Moving time')
            motor.forward()
            sleep(1)
            motor.backward()
            sleep(1)
            motor.stop
        elif 'goodbye' in text:
            aiy.voice.tts.say('Goodbye')
            motor.stop()
            break

if __name__ == '__main__':
    main()