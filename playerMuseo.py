#!/usr/bin/python
# -*- coding: utf-8 -*-

import vlc
import time
from gpiozero import Button

#create mediaPlayer object
player = vlc.MediaPlayer('/home/pi/Desktop/VlcPlayer/Videos/1.mp4')
	

#on release of the button	
def released(button):

    global Player

    if button.pin.number == 5:
		#set position to black 
        player.set_position(0.0)
        #pause on
        player.set_pause(1)
        time.sleep(0.2)
        

#on press of the button
def pressed(button):
	
    global Player

    if button.pin.number == 5:
		#resume the video (pause off)
        player.set_pause(0)
    #stop player
    elif button.pin.number == 20:
		player.stop()


if __name__ == '__main__':
	
	#defining button and methods used by the button
    button5 = Button(5)
    button5.when_pressed = pressed
    button5.when_released = released
    
    button20 = Button(20)
    button20.when_pressed = pressed
    
	#initialize video on black position and pause
    player.play()
    player.set_fullscreen(True)
    time.sleep(0.5)
    player.set_pause(1)

    while True:
        continue

