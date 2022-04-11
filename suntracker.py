from astral import LocationInfo
from astral.geocoder import database
from astral.geocoder import lookup
from astral.sun import sun
from datetime import date, timedelta, datetime
from math import floor
from time import sleep
from random import randint
import requests
import vlc

class Sun:
    def __init__(self,city,utc_offset):

        self.city = lookup(city, database())
        self.utc_offset = utc_offset
        self.td = timedelta(hours=utc_offset)

    def summary(self):
        data = self.calc()
        countdown = self.seconds_until()

        for s in list(countdown):
            print(str(s) + ': ' + str(data[s]+self.td) 
                    + '\tin ' + str(floor(countdown[s])) + 's')

    def calc(self):
        return sun(self.city.observer)

    def seconds_until(self):
        now = (datetime.utcnow()+self.td).timestamp()
        data = self.calc()
        return {
                'dawn' : data['dawn'].timestamp() - now,
                'sunrise' : data['sunrise'].timestamp() - now,
                'sunset' : data['sunset'].timestamp() - now,
                'dusk' : data['dusk'].timestamp() - now
            }

    def daemon(self):
        while True:
            daemon_flag = None
            events = self.seconds_until()
            for s in list(events):
                if events[s] > 0:
                    t = round(events[s])
                    print("Sun.daemon will call sun." + str(s) + " in " + str(t) + " seconds")
                    sleep(t)
                    result = eval(s + "()")
                    sleep(randint(1,60))
                    break

    def dawn(self):
        return 0
    def sunrise(self):
        return 0
    def sunset(self):
        return 0
    def dusk(self):
        return 0

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
    s = AudreysSun()
    s.daemon()
