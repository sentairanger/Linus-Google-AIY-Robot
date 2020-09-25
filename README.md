# Linus-Google-AIY-Robot

This is a project where I created a robot based on voice control using the Google-AIY voice kit V2

## Intro

Hello, this is a project that took me (on and off) two years to complete due to frustration and dead ends. However, I was recently able to get things running and now I am happy to present this project to you all. This is a project that I really wanted to accomplish in order to further my understanding of AI, machine learning and robotics. 

## Note

Here's some things I had to take into consideration:

* The Google Voice Assistant is now depreciated so in order to get it working I had to use the command `pip3 install google-voice-assistant==1.0.0`.
* The Apache License header was added to some of the code to comply with it because even though you can modify it, you must respect the license. In this case, I kept the header in tact but added a few lines to indicate that I had modified the code, and gave the date of when I modified the code. This is important to comply with the license.
* To use the Voice kit, you'll need a 2.1 amp power supply as that is required to power the voice bonnet. 
* The Cloudspeech API changed to the Cloud Speech to Text API so make sure you take that into consideration as well.
* I added the Apache License to conform with legal guidelines

## Dedication

This project is dedicated to the wonderful Mr. Paul F. Cain. He was my AP Physics teacher and my High Q coach. He helped me when I was bullied in school and recruited me for High Q when I was senior. He listened to me, guided me and believed in me. Unfortunately, I've made many mistakes that almost cost me my life and for years felt that I had disappointed him. That feeling got worse when he died 2 years ago. I started this project because of him and as much as I thought I had failed him I had to keep going for him. I am glad I didn't give up and I can finally dedicate this to him as he was my biggest inspiration.

## Getting Started

To get things started here is what I needed to set things up:

* Google AIY Voice Kit V 2.0 (Raspberry Pi Zero W included)
* DC Motors (I used the ones from the Cam Jam Edukit 3)
* Generic Robot Chassis 
* Plasticard
* Risers
* L298N Motor controller
* 2.1 Amp Power Bank
* 4 AA Battery pack
* 4 AA Batteries
* MicroSD Card
* Wheels for the motor

Before I had assembled the robot, I had to get things running. So since I already had my Voice Kit assembled, I installed the latest version of Raspbian available from their repositories. I used [this](https://aiyprojects.withgoogle.com/voice/) link to follow along. After successfully following the instructions, I decided to run the code provided on the microSD card and also ran my own code as well as modifying their `cloudspeech_demo.py` to test out the custom pin headers provided by the Voice Bonnet. Again, I kept the license in tact and added my own lines to indicate when I modified the code and what it does.

## Running Things

After successfully running some of the code I had written and modified, I decided to move on to the robot. First test failed because the battery pack wasn't giving the motors enough power. I thought of adding 9V instead of the 6V but that caused one of my L298N modules to malfunction and a capacitor exploded. So instead I lowered the power to 6V again and with new batteries the motors worked. I then assembled the robot and tested things using my voice. The commands I gave the robot were "go forward", "go backward", "go left", and "go right". The robot would move based on the commands I gave it. However, I will be modifying the code to add more precision. Until then, I can declare that the robot ran very well. 

## Say Hello To Linus

Here is Linus 

![Robot](https://github.com/sentairanger/Linus-Google-AIY-Robot/blob/master/IMG_20200912_124341667.jpg)

## Code Listing

* `button_led_control.py` turns on and off an LED using the Button provided by the Voice kit.

* `cloudspeech_demo_led.py` is a modified version of the demo provided by Google. Again, I made sure to keep the license in tact and made it clear when I modified the code to comply with the Apache License. This turns on, off and blinks the LED using the Cloud Speech to Text API by Google.

* `led_blink_board.py` is also a modified version of the demo provided by Google, but this time it turns on, off and blinks several LEDs using voice commands.

* `motor_button.py` turns on and off a motor also using the same button provided by the Voice Kit.

* `motor_movement.py` makes the motor turn forwards, backwards and move around also based on voice commands using the same API.

* `robot_movement.py` is the main focus of my project. It also is the modified version of the same demo by Google but this time it controls my robot using voice commands. 

* `servo_button.py` controls a servo using the same button by the Voice Kit.

* `traffic_light_control.py` is also another modified verson of the demo by Google but this time the LEDs behave like a traffic light and turn on and off based on voice commands.

* `linus_movement.py` makes Linus dance, spin, twirl, move around in a shape and prepares for battle. I plan to use this for my IT Link cosplay.

## Updates

I will be adding any updates to this section stating which new code has been added as well as any new progress with this project.

* 9/25 update: added the final code for Linus.
