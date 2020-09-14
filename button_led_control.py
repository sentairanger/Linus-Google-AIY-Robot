#!/usr/bin/env python3

#import libraries
from aiy.board import Board
from gpiozero import LED
from aiy.pins import pin_A

#define led
led_yellow = LED(pin_A)

def main():
    print('Press button to start')
    with Board() as board:
        while True:
            #when button is pressed the led turns on
            board.button.wait_for_press()
            led_yellow.on()
            #when the button is released the led turns off
            board.button.wait_for_release()
            led_yellow.off()

if __name__ == '__main__':
    main()
                
                
            