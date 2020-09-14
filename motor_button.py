#!/usr/bin/env python3
#import libraries
from gpiozero import Motor
from aiy.board import Board
from aiy.pins import (PIN_A, PIN_B)

#Define the motor
motor = Motor(forward = PIN_A, backward = PIN_B)

#When the button is pressed the motor turns on. When it is released the motor turns off
def main():
    print('Press button to control motor or exit with Ctrl+C')
    with Board as board():
        while True:
            board.button.wait_for_press()
            motor.forward()
            board.button.wait_for_release()
            motor.stop()

if __name__ == '__main__':
    main()
