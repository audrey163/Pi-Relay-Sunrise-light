from astral import LocationInfo
from astral.geocoder import database
from astral.geocoder import lookup
from astral.sun import sun
from datetime import date, timedelta, datetime
from math import floor
from time import sleep
from random import randint

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

