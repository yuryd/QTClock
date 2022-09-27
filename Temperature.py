import json
import requests
import datetime
from WeatherTypes import *

class Temperature:
    __TimeFmt = '%Y-%m-%dT%H:00'

    def __init__(self, localConfig):
        self.__lcd = localConfig
        self.__wt = self.GetLcd("wt")
        self.__url = self.GetLcd("url")
        self.__key = self.GetLcd("key")
        self.__daily = self.GetLcd("daily")
        self.__hourly = self.GetLcd("hourly")
        self.__fullUrl = self.GetLcd("fullUrl")
        self.__address = self.GetLcd("address")

        self.__prevTime = None

        self.__prevTemp = None

    def GetTemperature(self):
        if self.__key is None or self.__key == "":
            currHr = datetime.datetime.now().strftime(Temperature.__TimeFmt)
            if self.__prevTime is None or self.__prevTime != currHr:
                self.__prevTime = currHr
                #print(f'Temperature Retrieved at {currHr}')
                resp = requests.get(self.__fullUrl).content
                #print(resp)
                wData = json.loads(resp)
                #print(wData)
                self.__tempCharacter = wData["hourly_units"]["temperature_2m"]
                hrIdx = wData["hourly"]["time"].index(currHr) #find the current hour index
                self.__currTemperature = wData["hourly"]["temperature_2m"][hrIdx]
                self.__trendChar = '\u21C5' if self.__prevTemp is None or self.__currTemperature == self.__prevTemp else '\U0001F815' if self.__currTemperature > self.__prevTemp else '\U0001F817'
                self.__prevTemp = self.__currTemperature
            return (self.__tempCharacter, self.__currTemperature, self.__trendChar)
        return (None, None)
            #https://api.open-meteo.com/v1/forecast?latitude=44.70&longitude=-63.66&hourly=temperature_2m&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone=auto

    def GetTempChar(self):
        return self.__tempCharacter

    def GetTemp(self):
        return self.__currTemperature

    def GetAddress(self):
        return self.__address

    def GetLcd(self, term):
        return self.__lcd[term] if term in self.__lcd else None
