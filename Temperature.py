import json
import request
from WeatherTypes import *

class Temperature:
    def __init__(self, localConfig):
        self.__wt = localConfig["wt"]
        self.__url = localConfig["url"]
        self.__key = localConfig["key"]
        self.__daily = localConfig["daily"]
        self.__hourly = localConfig["hourly"]
        self.__location = localConfig["location"]
        self.__fullUrl = localConfig["fullUrl"]
        self.__address = localConfig["address"]

    def GetTemperature(self):
        if self.__key == "":
            resp = request.get(self.__fullUrl)
            wData = json.load(resp)
        self.__tempCharacter = wData["hourly_units"]["temperature_2m"]
        currHr = datetime.datetime.now().strftime('%Y-%m-%dT%H:00')
        hrIdx = wData["hourly"]["time"].index(currHr) #find the current hour index
        self.__currTemperature = wData["hourly"].temperature_2m[hrIdx]
        return (self.__tempCharacter, self.__currTemperature)
            #https://api.open-meteo.com/v1/forecast?latitude=44.70&longitude=-63.66&hourly=temperature_2m&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone=auto

    def GetTempChar(self):
        return self.__tempCharacter

    def GetTemp(self):
        return self.__currTemperature

    def GetAddress(self):
        return self.__address
