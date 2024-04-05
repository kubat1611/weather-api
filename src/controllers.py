import copy
from typing import Union, List
from repositories import AirQualityRepository, airQualityRepository

from airQuality import AirQuality


class CreateAirQualityController:
    def __init__(self, repository: AirQualityRepository, dto: AirQuality):
        self._repository = repository
        self._dto = dto

    def create(self, airQuality) -> None:
        self._dto.add_data(airQuality)
        data = self._dto.get_data()

        if None in data:
            raise ValueError("Missing arguments")

        self._repository.add_airQuality(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8],
                                        data[9])


class GetAirQualitiesController:
    def __init__(self, repository: AirQualityRepository) -> None:
        self._repository = repository

    def get(self, timestamp: Union[str, None] = None) -> Union[List[dict], dict]:
        airQualities = copy.deepcopy(self._repository.get_air_qualities())
        if timestamp is None:
            return airQualities

        for airQuality in airQualities:
            if airQuality['timestamp'] == timestamp:
                return airQuality
            if airQuality['temperature'] >= 100 or airQuality['temperature'] <= -100:
                raise ValueError('Invalid temperature')
            if airQuality['athmospheric_pressure'] >= 2000 or airQuality['athmospheric_pressure'] <= 500:
                raise ValueError('Invalid atmospheric pressure')

        raise ValueError('Invalid timestamp')


create_airQuality_controller = CreateAirQualityController(airQualityRepository, AirQuality())
get_airQualities_controller = GetAirQualitiesController(airQualityRepository)
