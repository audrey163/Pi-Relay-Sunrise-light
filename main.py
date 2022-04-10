from suntracker import Sun
import requests
import vlc
from time import sleep

class AudreysSun(Sun):
    def  __init__(self):
        super().__init__(city="Atlanta",utc_offset=-4)
        self.host = 'http://10.0.0.203:420'
        self.streams = 'http://uk1.internet-radio.com:4086/listen.pls'
    def dusk(self):

        #turn on lamp
        #this makes tells github.com/audrey163/Pi-Relay-Server hosted on my raspberry pi to turn on the lamp
        url = self.host + '/on?ch=1'
        response = requests.get(url)
        print("sun.dusk turn on light [ " + response.text + " ]")

        radio_bbc = 'http://www.vpr.net/vpr_files/stream_playlists/vpr_bbc_mp3.pls'
        self.stream_radio(url=radio_bbc,time=15*60)

    def stream_radio(self,url,time):
        instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
        #Define VLC player
        player=instance.media_player_new()
        #Define VLC media
        media=instance.media_new(url)
        #Set player media
        player.set_media(media)
        #Play the media
        player.play()
        sleep(time)
        player.stop()

if __name__ == '__main__':
    #s.daemon()
    s = AudreysSun()
    s.dusk()
