from pydantic import BaseModel
from typing import Optional


class AirQuality(BaseModel):
    _timestamp: Optional[str]
    _aqi_US: Optional[int]
    _aqi_China: Optional[int]
    _main_pollutant_US: Optional[str]
    _main_pollutant_China: Optional[str]
    _temperature: Optional[int]
    _athmospheric_pressure: Optional[int]
    _humidity: Optional[int]
    _wind_speed: Optional[float]
    _wind_direction: Optional[int]

    def add_data(self, data: dict[str, Optional[dict[str, Optional[float]]]]):
        for key in ['pollution', 'weather']:
            if key not in data:
                data[key] = None

        self._timestamp = data['pollution'].get('ts')
        self._aqi_US = data['pollution'].get('aqius')
        self._aqi_China = data['pollution'].get('aqicn')
        self._main_pollutant_US = data['pollution'].get('mainus')
        self._main_pollutant_China = data['pollution'].get('maincn')
        self._temperature = data['weather'].get('tp')
        self._athmospheric_pressure = data['weather'].get('pr')
        self._humidity = data['weather'].get('hu')
        self._wind_speed = data['weather'].get('ws')
        self._wind_direction = data['weather'].get('wd')

    def get_data(self) -> tuple[str, int, int, str, str, int, int, int, float, int]:
        data = (
            self._timestamp, self._aqi_US, self._aqi_China, self._main_pollutant_US, self._main_pollutant_China,
            self._temperature, self._athmospheric_pressure, self._humidity, self._wind_speed, self._wind_direction
        )
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
