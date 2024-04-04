import copy

from repositories import AirQualityRepository, airQualityRepository

from airQuality import AirQuality, airQuality


class CreateAirQualityController:
    def __init__(self, repository: AirQualityRepository, dto: AirQuality):
        self._repository = repository
        self._dto = dto

    def create(self, airQuality) -> None:
        self._dto.add_data(airQuality)
        data = self._dto.get_data()

        if None in data:
            raise ValueError("Missing arguments")

        self._repository.add_airQuality(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])


class GetAirQualitiesController:
    def __init__(self, repository: AirQualityRepository) -> None:
        self._repository = repository

    def get(self, timestamp: str | None = None):
        airQualities = copy.deepcopy(self._repository.get_airQualities())
        if timestamp is None:
            return airQualities

        for airQuality in airQualities:
            if airQuality['timestamp'] == timestamp:
                return airQuality

        raise ValueError('Invalid timestamp')


create_airQuality_controller = CreateAirQualityController(airQualityRepository, airQuality)
get_airQualities_controller = GetAirQualitiesController(airQualityRepository)
