import vlc
import time
from gpiozero import Button
from vlc import EventType

vlcInstance = None
player = None
media = None
fadeSpeed = 0.05
premuto = False
# def fadeVolume():
    # vol = player.audio_get_volume()
    # while vol != 0:
        # vol -= 1
        # #setvolume returns -1 if vol is out of range. you never know
        # if player.audio_set_volume(vol) == -1:
            # vol = 0
            # player.audio_set_volume(vol)
        # time.sleep(fadeSpeed)

def resetPlayer():
    player.set_pause(1)
    player.set_position(0.015)
    #player.audio_set_volume(100)


def pressed():
    global premuto
    premuto = True
    print('premuto')
    resetPlayer()
    player.set_pause(0)
    

def inPause(event):
    global premuto
    if(premuto==False):
	player.set_position(0.0)
	player.set_pause(1)
    else:
	premuto = False
    
    
if __name__ == '__main__':
    
    button27 = Button(27)
    button27.when_pressed = pressed

    vlcInstance = vlc.Instance()

    media = vlcInstance.media_new_path('Videos/Museoh265.mp4')
    media.add_option(':play-and-pause')

    player = vlcInstance.media_player_new()
    #player.set_fullscreen(True)
    player.set_media(media)
    player.play()
    time.sleep(0.5)
    player.set_pause(1)
    
    # #event end
    event_manager = player.event_manager()
    event_manager.event_attach(vlc.EventType.MediaPlayerPaused, inPause)
	

    
    

    while True:
        continue


