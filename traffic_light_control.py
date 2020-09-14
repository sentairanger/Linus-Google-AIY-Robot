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
# traffic_light_control.py
# Controls LEDs similar to a traffic light
# Modified by Edgardo Peregrino
# 9/2/2020

"""A demo of the Google CloudSpeech recognizer."""
#import libraries
import argparse
import locale
import logging

from aiy.cloudspeech import CloudSpeechClient
from gpiozero import LEDBoard
from aiy.pins import (PIN_A, PIN_B, PIN_C, PIN_D)

#define the traffic light LEDs
traffic_lights = LEDBoard(PIN_A, PIN_B, PIN_C, PIN_D)

#create a function that creates hints to what to say to the box
def get_hints(language_code):
    if language_code.startswith('en_'):
        return ('stop',
                'slow',
                'go',
                'turn',
                'goodbye')
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
        text = client.recognize(language_code=args.language,
                                    hint_phrases=hints)
        if text is None:
            logging.info('You said nothing.')
            continue
        logging.info('You said: "%s"' % text)
        text = text.lower()
        # Here, one of the LEDs will turn on based on the commands
        if 'turn' in text:
            traffic_lights.value = (0, 0, 0, 1)
        elif 'go' in text:
            traffic_lights.value = (0, 0, 1, 0)
        elif 'slow' in text:
            traffic_lights.value = (0, 1, 0, 0)
        elif 'stop' in text:
            traffic_lights.value = (1, 0, 0, 0)
        elif 'goodbye' in text:
            break

if __name__ == '__main__':
    main()