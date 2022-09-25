class WeatherTypes:
    __wt = {"0": "open-meteo"}

    @classmethod
    def GetDefaultType(cls):
        return WeatherTypes.__wt["0"]
