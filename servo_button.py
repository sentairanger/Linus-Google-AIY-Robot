#!/usr/bin/env python3
#import libraries
from aiy.board import Board
from gpiozero import Servo
from aiy.pins import PIN_A

#Define a servo with precisions
servo = Servo(PIN_A, min_pulse_width = 0.0005, max_pulse_width = 0.0019)

#When the button is pressed the servo goes to max but when it is waiting for press, it is at min
def main():
    print('Control motor with button (Press Ctrl+C to exit)')
    with Board() as board:
        while True:
            servo.min()
            board.button.wait_for_press()
            servo.max()
            board.button.wait_for_press()
            

if __name__ == '__main__':
    main()