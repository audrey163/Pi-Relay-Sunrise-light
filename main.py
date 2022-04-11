from suntracker import Sun
import requests
import vlc
from time import sleep

class AudreysSun(Sun):
    def  __init__(self):
        super().__init__(city="Atlanta",utc_offset=-4)
        self.host = 'http://127.0.0.1:420'
        self.streams = 'http://uk1.internet-radio.com:4086/listen.pls'
    def dusk(self):

        #turn on lamp
        #this makes tells github.com/audrey163/Pi-Relay-Server hosted on my raspberry pi to turn on the lamp
        url = self.host + '/high?ch=1'
        response = requests.get(url)
        print("sun.dusk turn on light [ " + response.text + " ]")

        #radio_bbc = 'http://www.vpr.net/vpr_files/stream_playlists/vpr_bbc_mp3.pls'
        #self.stream_radio(url=radio_bbc,time=15*60)

    def dawn(self):
        response = request.get(self.host+'high?ch=1' )
        sleep(0.5) 
        response = request.get(self.host+'low?ch=1') # I turn the switch on and off to wake up the red bluetooth led lamp
        sleep(0.5)
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
    s.daemon()
