# MuseumPlayer
Media player based on raspberry Pi

Media Player uses vlc-python library to interact with vlc and to play a video on a button press, when the video reaches the end it goes back to strat of the video.

When connected to the power the raspberry automatically run the program after the lxde enviroment is setup.

Important!
Disable screensaver installig xscreensaver

Autostart process:

Create .desktop file to be run after Desktop is loaded

mkdir /home/pi/.config/autostart
nano /home/pi/.config/autostart/player.desktop

Code inside player.desktop:

[Desktop Entry]
Type=Application
Name=Player
Exec=/usr/bin/python /home/pi/player.py

then place python script in /home/pi/player.py

If you want to remove autostart delete player.desktop -> path /home/pi/.config/autostart

