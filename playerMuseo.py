import vlc
import time
from gpiozero import Button
from vlc import EventType

vlcInstance = None
player = None
media = None


#reset player when pressed
def resetPlayer():
    #player.set_pause(1)
    player.set_position(0.015)
    player.audio_set_volume(100)

#pressed button
def pressed():
    resetPlayer()
    player.set_pause(0)
    print('press')

#place at start when ends
def inPause(event):
    player.set_pause(1)	
    player.set_position(0.0)
    
    
if __name__ == '__main__':
   
    button17 = Button(17)
    button17.when_pressed = pressed
    
    #create instance
    vlcInstance = vlc.Instance()
    media = vlcInstance.media_new_path('Videos/museo_press.mp4')
    media.add_option(':play-and-pause')
    player = vlcInstance.media_player_new()
    #player.set_fullscreen(True)
    player.set_media(media)
    player.play()
    player.set_pause(1)
    player.set_position(0.0)
    
    #end video
    event_manager = player.event_manager()
    event_manager.event_attach(vlc.EventType.MediaPlayerPaused, inPause)

    while True:
        continue


