class AirQuality:
    def __init__(self):
        self._timestamp = None
        self._aqi_US = None
        self._aqi_China = None
        self._main_pollutant_US = None
        self._main_pollutant_China = None
        self._temperature = None
        self._athmospheric_pressure = None
        self._humidity = None
        self._wind_speed = None
        self._wind_direction = None

    def add_data(self, data: dict[str, None | dict[str, float | int | str]]):
        for key in ['pollution', 'weather']:
            if key not in data:
                data[key] = None

        self._timestamp = data['pollution']['ts']
        self._aqi_US = data['pollution']['aqius']
        self._aqi_China = data['pollution']['aqicn']
        self._main_pollutant_US = data['pollution']['mainus']
        self._main_pollutant_China = data['pollution']['maincn']
        self._temperature = data['weather']['tp']
        self._athmospheric_pressure = data['weather']['pr']
        self._humidity = data['weather']['hu']
        self._wind_speed = data['weather']['ws']
        self._wind_direction = data['weather']['wd']

    def get_data(self) -> tuple[str, int, int, str, str, int, int, int, float, int]:
        data = (self._timestamp, self._aqi_US, self._aqi_China, self._main_pollutant_US, self._main_pollutant_China,
                self._temperature, self._athmospheric_pressure, self._humidity, self._wind_speed, self._wind_direction)
        self._timestamp = None
        self._aqi_US = None
        self._aqi_China = None
        self._main_pollutant_US = None
        self._main_pollutant_China = None
        self._temperature = None
        self._athmospheric_pressure = None
        self._humidity = None
        self._wind_speed = None
        self._wind_direction = None
        return data


airQuality = AirQuality()
