import json
from geopy.geocoders import Nominatim
import geocoder
import datetime
from WeatherTypes import *

class ConfigError(Exception):
    pass

class Config:
    __MsgPref = "Configuration error: "
    __MsgSuff = " missing"
    __ConfigCount = 0
    __DefaultConfigFile = "Clock5.json"
    __strCV = ["ConfigVersion",[1,0]]
    __strID = ["Identification",[1,0]]
    __strALF = ["ActivityListFile",[1,0]]
    __LocalConfigFile = "Clock5_local.json"

    def __init__(self):
        if Config.__ConfigCount != 0:
            raise ConfigError(Config.__MsgPref + "Config class already instantiated")

        Config.__ConfigCount = 1
        with open(Config.__DefaultConfigFile) as ConfigFile:
            configData = json.load(ConfigFile)

        if not(Config.__strCV[0] in configData):
            raise ConfigError(Config.__MsgPref + Config.__strCV[0] + Config.__MsgSuff)
        self.__ConfigVersion = configData[Config.__strCV[0]] if Config.__strCV[0] in configData else None

        if not(Config.__strID[0] in configData) and Config.__CheckVersion(self.__ConfigVersion, __strID[1]):
            raise ConfigError(Config.__MsgPref + Config.__strID[0] + Config.__MsgSuff)
        if not(Config.__strALF[0] in configData) and Config.__CheckVersion(self.__ConfigVersion, __strALF[1]):
            raise ConfigError(Config.__MsgPref + Config.__strALF[0] + Config.__MsgSuff)

        self.__Identification = configData[Config.__strID[0]] if Config.__strID[0] in configData else None
        self.__ActivityListFile = configData[Config.__strALF[0]] if Config.__strALF[0] in configData else None
        self.GetLocalConfig()

    def GetLocalConfig(self):
        localConfigData = None
        newError = None
        try:
            with open(Config.__LocalConfigFile) as LocalConfigFile:
                localConfigData = json.load(LocalConfigFile)
        except FileNotFoundError:
                pass

        if localConfigData is None:
            loc = Nominatim(user_agent="GetLoc")
            weatherType = WeatherTypes.GetDefaultType()
            url = "https://api.open-meteo.com/v1/forecast"
            key = ""
            daily="daily=weathercode,temperature_2m_max,temperature_2m_min"
            hourly="hourly=temperature_2m"
            timezone = "timezone=auto"
            getLocFull = geocoder.ip("me")
            print(getLocFull.geojson)
            getLoc = getLocFull.geojson["features"][0]["properties"]
            address = getLoc["address"]
            position = f'longitude={getLoc["lng"]}&latitude={getLoc["lat"]}'
            fullUrl = f'{url}?{position}&{hourly}&{daily}&{timezone}'
            localConfigData = {"wt": weatherType, 
                    "url": url, 
                    "key": key,
                    "fullUrl": fullUrl,
                    "daily": daily,
                    "hourly": hourly,
                    "timezone": timezone,
                    "position": position,
                    "address": address}
            with open(Config.__LocalConfigFile, "w") as localConfig:
                json.dump(localConfigData, localConfig, indent=4)
            self.__localConfig = localConfigData
        else:
            self.__localConfig = localConfigData

    @classmethod
    def __CheckVersion(cls, cv, sv): #cv config version data, sv section version
        major = cv["Major"]
        minor = cv["Minor"]
        return sv[0] >= major and sv[1] >= minor

    def ConfigVersion(self, param=None):
        if param is None:
            return self.__ConfigVersion
        return self.__ConfigVersion[param] if param in self.__ConfigVersion else None

    def Identification(self, param=None):
        if param is None:
            return self.__Identification
        return self.__Identification[param] if param in self.__Identification else None

    def ActivityListFile(self, param=None): #param included for future growth, no current param supported
        return self.__ActivityListFile if param is None else None

    def GetLocalConfigData(self):
        return self.__localConfig
